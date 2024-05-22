# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022/6/27 16:51
@Author: guozg
@File：api_base.py
"""
import inspect
from threading import RLock

from common.api_all_pub_pkg import *
from common.step_msg import step_msg
from common.handle_depend_data import handle_depend_data
from common.handle_response_data import handle_response_data
# from common.handle_assert_exp import handle_assert_exp,handle_assert
from common.handle_assert import handle_assert_exp
from common.save_log import logger
from common.jsonschema_validate import jschema_validate
from copy import copy

files_str = "files"


class ApiBase():
    ''''''

    __instance_lock = RLock()
    __instance = None

    def __new__(cls, *args, **kwargs):
        raise ImportError("不允许实例化")

    @classmethod
    def get_instance(cls,req_params,desc,asert,resp,dependdata,run,stroy,jschema):
        with cls.__instance_lock:
            if cls.__instance == None:
                cls.__instance = super().__new__(cls)
        cls.__instance.__init(req_params,desc,asert,resp,dependdata,run,stroy,jschema)
        return cls.__instance

    def __init(self,req_params,desc,asert,resp,dependdata,run,stroy,jschema):
        '''
        初始化时需要传入的参数  \n
        :param req_params: 请求参数
        :param desc: 描述/每个case的目的，用于最终的case title
        :param asert: 断言
        :param resp: 响应结果的处理
        :param dependdata: 依赖的数据
        :param run: 是否运行
        :param stroy: 功能模块
        :param jschema: jsonschema 要验证的数据
        # :param confdata: config.yml 数据
        '''
        self.__run = run
        if self.__run == False:
            pytest.skip(f"该用例的run的值为：{run} , 所以不需要执行！！！")

        self.__req_params = req_params
        self.__desc = desc
        self.__asert = asert
        self.__resp = resp
        self.__depend_data = dependdata
        self.__story = stroy
        # 于2023-03-13 添加
        self.__jschema = jschema

    def run_case(self):
        ''''''
        if self.__desc and self.__desc !="":
            # 设置报告中的case的title
            allure.dynamic.title(self.__desc)
        if self.__story and self.__story !="":
            # 设置报告的case的功能名称
            allure.dynamic.story(self.__story)
        # 设置报告中的描述
        allure.dynamic.description(f"""
        传入的请求参数：{self.__req_params}
        传入的依赖数据：{self.__depend_data}
        传入的响应结果动作：{self.__resp}
        传入的断言：{self.__asert}
        传入的jsonschema数据为：{self.__jschema}
        """)

        # ********************* 第一步 ******************************
        msg = "第一步：处理数据依赖."
        req_params = handle_depend_data(self.__req_params, self.__depend_data)
        # step_msg(msg)
        with allure.step(msg):
            pass

        # ********************* 第二步 ******************************
        msg = "第二步：进行接口请求."
        # step_msg(msg)
        files_data = copy(req_params.get(files_str))
        req_params_tmp = copy(req_params)
        if files_data:
            # 如果有上传附件操作，需要单独处理
            req_params_tmp.pop(files_str)
            req_params_tmp = simplejson.dumps(req_params_tmp, ensure_ascii=False, encoding='utf-8', indent=2)
            with allure.step(msg):
                allure.attach(body=req_params_tmp, name="处理后的请求参数(附件数据请看下方)",
                              attachment_type=allure.attachment_type.JSON)
                allure.attach(body=f"{files_data}", name="上传的附件数据", attachment_type=allure.attachment_type.TEXT)

        else:

            req_params_tmp = simplejson.dumps(req_params_tmp, ensure_ascii=False, encoding='utf-8', indent=2)
            with allure.step(msg):
                allure.attach(body=req_params_tmp, name="处理后的请求参数", attachment_type=allure.attachment_type.JSON)

        # ********************* 第三步 ******************************
        req = requests.request(**req_params)
        msg = "第三步：获取接口响应结果."
        # step_msg(msg)
        req_json_tmp = simplejson.dumps(req.json(), ensure_ascii=False, encoding='utf-8', indent=2)
        with allure.step(msg):
            allure.attach(body=req_json_tmp, name="响应结果", attachment_type=allure.attachment_type.JSON)

        # ********************* 第四步 ******************************
        msg = "第四步：处理响应结果."
        handle_response_data(self.__resp, req.json())
        # step_msg(msg)
        with allure.step(msg):
            pass

        # ********************* 第五步 jsonschema 校验******************************
        msg = "第五步: jsonschema 校验."
        validate = jschema_validate(self.__jschema,req.json())
        report_msg = ""
        jschema_flag = 0
        name = "jsonschema 校验结果"
        # 表示验证通过或首次存入jsonschema文件。
        if validate == None:
            report_msg = "jsonschema验证通过或首次存入jsonschema文件"
            jschema_flag=1
            # name = f"{name}--【成功】"
            msg = f"{msg}--【成功】"

        # 表示传入的值为None或validate的值为False
        elif validate == False:
            report_msg = "未进行jsonschema校验,原因: yaml文件中的jschema_validate 的值为None或validate的值为False"
            jschema_flag = 2
            # name = f"{name}--【未校验】"
            msg = f"{msg}--【未校验】"

        # 表示filepath的json文件找不着,暂时不考虑 mysql 与 redis 数据库相关的错。
        elif validate == "fileerror" or validate == "file_error":
            report_msg = "未进行jsonschema校验,原因: 指定的jsonschema文件不存在"
            jschema_flag = 3
            # name = f"{name}--【失败】"
            msg = f"{msg}--【失败】"

        # 表示filepath的json文件存在，但是内容为空。
        elif validate == "filenull" or validate == "file_null":
            report_msg = "未进行jsonschema校验,原因: 指定的jsonschema文件虽然存在,但是内容为空"
            jschema_flag = 4
            # name = f"{name}--【失败】"
            msg = f"{msg}--【失败】"

        # 表示校验未通过
        else:
            report_msg = f"jsonshcema校验失败,原因如下:\n{validate}"
            jschema_flag = 5
            # name = f"{name}--【失败】"
            msg = f"{msg}--【失败】"

        with allure.step(msg):
            allure.attach(body=report_msg,name=name,attachment_type=allure.attachment_type.JSON)

        pytest.assume(jschema_flag<=2)

        # ********************* 第六步 处理断言******************************
        msg = "第六步：处理断言."
        step_msg(msg)
        with allure.step(msg):
            allure.attach(body=simplejson.dumps(self.__asert, ensure_ascii=False, encoding='utf-8', indent=2),
                          name="断言表达式",
                          attachment_type=allure.attachment_type.JSON)
        handle_assert_exp(req, self.__asert)

    def run_case_havelog(self):
        ''''''
        base = inspect.stack()
        filename = base[1].filename
        filename = os.path.basename(filename)
        func_name = base[1].function
        line_no = base[1].lineno
        __log_fmt = f"{filename:<10s}:{line_no:0>3d}:{func_name:<10s}:"
        if self.__desc and self.__desc != "":
            # 设置报告中的case的title
            allure.dynamic.title(self.__desc)
        if self.__story and self.__story != "":
            # 设置报告的case的功能名称
            allure.dynamic.story(self.__story)
        # 设置报告中的描述
        allure.dynamic.description(f"""
        传入的请求参数：{self.__req_params}
        传入的依赖数据：{self.__depend_data}
        传入的响应结果动作：{self.__resp}
        传入的断言：{self.__asert}
        """)

        msg = f"第一步：处理数据依赖"
        req_params = handle_depend_data(self.__req_params, self.__depend_data)
        logmsg = f"{__log_fmt}{msg}"
        logger.info(logmsg)
        step_msg(msg)

        msg = f"第二步：进行接口请求，参数为{req_params}"
        step_msg(msg)
        logmsg = f"{__log_fmt}{msg}"
        logger.info(logmsg)

        req = requests.request(**req_params)
        msg = f"第三步：获取到的接口响应结果：{req.json()}"
        step_msg(msg)
        logmsg = f"{__log_fmt}{msg}"
        logger.info(logmsg)

        msg = f"第四步：处理响应结果"
        handle_response_data(self.__resp, req.json())
        step_msg(msg)
        logmsg = f"{__log_fmt}{msg}"
        logger.info(logmsg)

        msg = "第五步: jsonschema 校验."
        validate = jschema_validate(self.__jschema, req.json())
        report_msg = ""
        jschema_flag = 0
        name = "jsonschema 校验结果"
        # 表示验证通过或首次存入jsonschema文件。
        if validate == None:
            report_msg = "jsonschema验证通过或首次存入jsonschema文件"
            jschema_flag = 1
            # name = f"{name}--【成功】"
            msg = f"{msg}--【成功】"

        # 表示传入的值为None或validate的值为False
        elif validate == False:
            report_msg = "未进行jsonschema校验,原因: yaml文件中的jschema_validate 的值为None或validate的值为False"
            jschema_flag = 2
            # name = f"{name}--【未校验】"
            msg = f"{msg}--【未校验】"

        # 表示filepath的json文件找不着,暂时不考虑 mysql 与 redis 数据库相关的错。
        elif validate == "fileerror" or validate == "file_error":
            report_msg = "未进行jsonschema校验,原因: 指定的jsonschema文件不存在"
            jschema_flag = 3
            # name = f"{name}--【失败】"
            msg = f"{msg}--【失败】"

        # 表示filepath的json文件存在，但是内容为空。
        elif validate == "filenull" or validate == "file_null":
            report_msg = "未进行jsonschema校验,原因: 指定的jsonschema文件虽然存在,但是内容为空"
            jschema_flag = 4
            # name = f"{name}--【失败】"
            msg = f"{msg}--【失败】"

        # 表示校验未通过
        else:
            report_msg = f"jsonshcema校验失败,原因如下:\n{validate}"
            jschema_flag = 5
            # name = f"{name}--【失败】"
            msg = f"{msg}--【失败】"

        with allure.step(msg):
            allure.attach(body=report_msg, name=name, attachment_type=allure.attachment_type.JSON)
        logmsg = f"{__log_fmt}{msg}"
        logger.info(logmsg)
        pytest.assume(jschema_flag <= 2)


        exp_str = handle_assert_exp(req, self.__asert)
        msg = f"第六步：处理断言. 原始表达式为: {self.__asert} ; 处理后的表达式为: {exp_str}"
        step_msg(msg)
        logmsg = f"{__log_fmt}{msg}"
        logger.info(logmsg)
        handle_assert_exp(req, self.__asert)

