# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022-6-29 11:31
@Author: test
@File：get_request_params.py
"""
import pytest
from urllib import parse
import simplejson
from string import Template
# from common.get_config_data import GetConfData
from common.upload_files import convert_files_to_stream
from common.get_host import get_host

# class GetReqParams():
#     '''获取接口请求相关的参数,最后会返回[[请求参数,case描述,断言,响应结果的处理,依赖的数据,是否运行,story模块]]'''
#
#     def get_params(self,ymldata:dict,caseymlname:str)->list:
#         '''
#         需要传入yml文件的数据、case对应的yml文件中的key \n
#         返回[[请求参数,case描述,断言,响应结果的处理,依赖的数据,是否运行,story模块],[……]……]
#         :param ymldata:  yml文件的数据。
#         :param caseymlname: case对应的yml文件中的key，如login
#         :return: list[[req,desc,asert,resp,depend,run,story],[req,desc,asert,resp,depend,run,story],……]
#         '''
#
#         if isinstance(ymldata, dict) and len(ymldata) > 1:
#             # self.__ymldata = ymldata
#             pass
#         else:
#             pytest.fail(f"传入的的yml数据错误，内容为：{ymldata}")
#
#         if isinstance(caseymlname, str) and caseymlname.strip() != "":
#             # self.__casename = caseymlname.strip()
#             caseymlname = caseymlname.strip()
#         else:
#             pytest.fail(f"传入的case对应的yml文件中的key的名字错误,值为：{caseymlname}")
#
#         # if isinstance(confobj,GetConfData):
#         #     self.__conf = confobj
#         # else:
#         #     pytest.fail(f"传入的confobj不是GetConfData对象,type为：{type(confobj)}")
#
#         # 获取case对应的yaml数据
#         casedata: dict = ymldata.get(caseymlname)
#         path = casedata['path']
#         # 全局procotol
#         g_procotol = ymldata.get('procotol')
#         # 全局host
#         g_host = ymldata.get('host')
#         # case 自己的host与procotol
#         m_host = casedata.get('host')
#         m_procotol = casedata.get('procotol')
#
#         run = True
#         story = ymldata.get('story')
#         if ymldata.get('run') == False:
#             run = False
#
#         # 判断模块自己的host与procotol
#         # 当模块自己的host为空或None时，使用全局的。暂不考虑使用全局进行替换
#         host = m_host
#         procotol = m_procotol
#         if m_host == None or m_host == "":
#             # 判断全局的host是否也为空
#             if g_host == None or g_host == "":
#                 host = "$host"
#             else:
#                 host = g_host
#
#         if m_procotol == None or m_procotol == "":
#             if g_procotol == None or g_procotol == "":
#                 procotol = "$procotol"
#             else:
#                 procotol = g_procotol
#
#         # if host==None or host == "":
#         #     host="$host"
#         #
#         # if procotol == None or procotol == "":
#         #     procotol = "$procotol"
#
#         # 这里使用模板技术，方便从config.yml 文件中读取host和procotol进行替换。
#         '''
#         1：这里需要注意及确认的是：是每个模块的host 都是一样的，还是说不同的模块的host都不一样？需要找恩强确认
#         2：从jenkins中获取到的host是在此时进行替换，还是在哪里进行替换
#         3：从config.yml 中获取到的host该当怎样处理
#         4：当不同模块的host 不一样时，方案如下：
#             a：将所有的模块全部收集起来，目前有3个，不同模块的host 可以简写，如：V5的登录相关：v5_host,v6_host
#             b：将这些host全部写在每个yaml和config.yml文件中。
#             c：同时要在各个的case yml文件中留module_flag,其值为 不同模块的简写，这样方便后期处理
#             d：各个host的优先级为：jenkins > config.yml > caseyml
#
#         还有另一种解决方案：
#         如果各个模块之前没有关联，或者没有业务上的耦合，或者不进行业务上的交集操作，则可以进行如下操作
#         1：yml文件中 不在写 module_flag，仍然留现在的写法，只有host
#         2：在config.yml 和 jenkins上 配置host
#         3：各个模块的代码(主要是case 和 config.yml) 提交到不同的分支中。
#         host的优先级：
#         jenkins > config.yml > caseyml
#
#         于20220704早会沟通得知：
#         1：接口最后还会投入到灰度与生产环境的验证
#         2：还是要适配各个功能模块的域名。留出相应的扩展
#         '''
#         if "$" in procotol or "$" in host:
#             url = f"{procotol}://{host}/{path}"
#         else:
#             url = parse.urljoin(f"{procotol}://{host}", path)
#
#         depend_list = casedata['depends_on']
#
#         data_str = simplejson.dumps(casedata, indent=4, ensure_ascii=False, encoding='utf-8')
#
#         data_tmp = Template(data_str).safe_substitute(url=url)
#         # 再将str格式的dict数据转化为 dict对象
#         casedata = simplejson.loads(data_tmp, encoding='utf8')
#
#         # 下面进行数据返回***************************
#         request_list: list = casedata['request_params']
#         desc_list: list = casedata['description']
#         assert_list: list = casedata['assert']
#         response_list: list = casedata['response']
#         params_list = []
#         requ_count = len(request_list)
#         resp_count = 0
#         # 判断是否需要处理响应结果。只有当为list时，且长度大于1时，才表示要处理相应的响应结果
#         if isinstance(response_list, list) and len(response_list) > 0:
#             resp_count = len(response_list)
#         # 判断是否是否有数据依赖，逻辑同上
#         depend_count = 0
#         if isinstance(depend_list, list) and len(depend_list) > 0:
#             depend_count = len(depend_list)
#
#         for i in range(requ_count):
#             if i <= (resp_count - 1) and i <= (depend_count - 1):
#                 tmp = [request_list[i], desc_list[i], assert_list[i], response_list[i], depend_list[i],run,story]
#             elif i <= resp_count - 1:
#                 tmp = [request_list[i], desc_list[i], assert_list[i], response_list[i], None,run,story]
#             elif i <= depend_count - 1:
#                 tmp = [request_list[i], desc_list[i], assert_list[i], None, depend_list[i],run,story]
#             else:
#                 tmp = [request_list[i], desc_list[i], assert_list[i], None, None,run,story]
#
#             params_list.append(tmp)
#
#         return params_list

def get_params(ymldata: dict, caseymlname: str) -> list:
    '''
    需要传入yml文件的数据、case对应的yml文件中的key \n
    返回[[请求参数,case描述,断言,响应结果的处理,依赖的数据,是否运行,story模块,jsonschema校验模块],[……]……]
    :param ymldata:  yml文件的数据。
    :param caseymlname: case对应的yml文件中的key，如login
    :return: list[[req,desc,asert,resp,depend,run,story,jschema],[req,desc,asert,resp,depend,run,story,jschema],……]
    '''

    if isinstance(ymldata, dict) and len(ymldata) > 1:
        pass
    else:
        pytest.fail(f"传入的的yml数据错误，内容为：{ymldata}")

    if isinstance(caseymlname, str) and caseymlname.strip() != "":
        caseymlname = caseymlname.strip()
    else:
        pytest.fail(f"传入的case对应的yml文件中的key的名字错误,值为：{caseymlname}")

    # 获取case对应的yaml数据
    casedata: dict = ymldata.get(caseymlname)
    path = casedata['path']
    # 全局procotol,目前未从config.yml 中进行获取procotol的值,后续有可能优先从该config.yml中获取
    # g_procotol = ymldata.get('procotol')
    procotol = ymldata.get('procotol')
    # # 全局host--弃用于20220825
    # g_host = ymldata.get('host')
    # # case 自己的procotol-- 目前yml文件中 未没有该key,先保留该代码,后续根据实际的情况看看是否需要在自己的case中加入procotol
    # # 正常情况下,一个功能模块的协议都是一样的,所以case所对应的yml文件中,一个yml文件中的协议应该是一致的。
    # m_procotol = casedata.get('procotol')

    story = casedata.get('story')
    '''run的逻辑于20230609做了优化,具体看下文'''
    # run = True
    # if casedata.get('run') == False:
    #     run = False

    # run的逻辑也需要进行优化,因为当某个模块进行下线或部分功能下线后,之前的做法是将对应的case相关的参数、校验、依赖……都者注释
    # 现在为了方便就直接将不需要运行的case的run状态标识为false即可。
    # 但是同时需要对原有的run的逻辑进行兼容。
    # ---------- 20230609 对run的逻辑进行优化 ----------
    '''
    由于run在优化之前只有一个结果,现在要考虑run的结果为list的情况
    当为list时,还有考虑长度与其他不一致的情况
    无论是个数不够,还是list中的值是否为bool值,只要不是为False 或 "false" 或 "False",均表示为True
    '''
    '''
    逻辑规则如下:
    1:先检查runlist的类型是否为list,当为list时,再进行如下逻辑判断
        a:判断list元素的值,
            当值的类型为str时进行转换为小写,判断是否为false,只有当为false时,则返回False;其他值均返回True;
            当值的类型的bol时,是啥就返回啥;
            当下标越界时,直接返回True
    2:当传入的值为bool值时,
        a: 若为True,则表示所有的case均运行,均返回True
        b: 若为False,表表示所有的case均不运行,均返回False
    '''
    runlist = True
    runlist_tmp: list = casedata.get('run')
    # 当run的值为list时
    if isinstance(runlist_tmp, list):
        runlist = runlist_tmp
    # 当为str时要判断其值是否为false
    elif isinstance(runlist_tmp, str):
        runlist_tmp = runlist_tmp.lower()
        if runlist_tmp == "false":
            runlist = False
    # 当为bool值时,要检测是否为False
    elif isinstance(runlist_tmp, bool):
        if runlist_tmp == False:
            runlist = False
    # 其他情况均为True
    else:
        pass

    # 这里使用模板技术，方便从config.yml 文件中读取host和procotol进行替换。
    '''
    1：这里需要注意及确认的是：是每个模块的host 都是一样的，还是说不同的模块的host都不一样？需要找恩强确认
    2：从jenkins中获取到的host是在此时进行替换，还是在哪里进行替换
    3：从config.yml 中获取到的host该当怎样处理
    4：当不同模块的host 不一样时，方案如下：
        a：将所有的模块全部收集起来，目前有3个，不同模块的host 可以简写，如：V5的登录相关：v5_host,v6_host
        b：将这些host全部写在每个yaml和config.yml文件中。
        c：同时要在各个的case yml文件中留module_flag,其值为 不同模块的简写，这样方便后期处理
        d：各个host的优先级为：jenkins > config.yml > caseyml 

    还有另一种解决方案：
    如果各个模块之前没有关联，或者没有业务上的耦合，或者不进行业务上的交集操作，则可以进行如下操作
    1：yml文件中 不在写 module_flag，仍然留现在的写法，只有host
    2：在config.yml 和 jenkins上 配置host
    3：各个模块的代码(主要是case 和 config.yml) 提交到不同的分支中。
    host的优先级：
    jenkins > config.yml > caseyml

    于20220704早会沟通得知：
    1：接口最后还会投入到灰度与生产环境的验证
    2：还是要适配各个功能模块的域名。留出相应的扩展

    于20220825定下最终的逻辑规则：
    一: case 自己的module_flag 有值时，则 根据 当前的 环境标记(cur_host_flag)进行如下的逻辑判断：
        1: 优先通过 从config.yml中获取对应的域名
            A: 当config.yml中不存在时，则再case所在的yml文件中获取
                a: 若case 所在的yml文件中 仍然不存在，则使用case自己的host值(后续有可能将逻辑变更为:若是case所在的yaml文件中仍然不存在
                则直接将当前的case置为fail,不在运行该case)
    二: case自己的module_flag 无值时,
        1: 使用case自己的host(后续有可能将逻辑变更为:直接将case置为fail,不在运行)

    module_flag 的值 与 host 环境 key的对应关系如下：
    module_flag: xxxx  对应的host 环境的key 则为：
    xxxx_testhost,xxxx_relhost,xxxx_prodhost
    如：
    module_flag: v5login
    则对应的 host 各个环境的key如下：
    v5login_testhost: xxxxx
    v5login_relhost: xxxx
    v5login_prodhost: xxxxx

    各个host环境的值 优先级：
    jenkins > config.yml > case 所在的yaml文件中的 域名环境  >  case 自己的 host值
    '''
    host = get_host(ymldata, casedata)
    if "$" in procotol or "$" in host:
        url = f"{procotol}://{host}/{path}"
    else:
        url = parse.urljoin(f"{procotol}://{host}", path)

    depend_list = casedata['depends_on']

    data_str = simplejson.dumps(casedata, indent=4, ensure_ascii=False, encoding='utf-8')

    data_tmp = Template(data_str).safe_substitute(url=url)
    # 再将str格式的dict数据转化为 dict对象
    casedata = simplejson.loads(data_tmp, encoding='utf8')

    # 下面进行数据返回***************************
    request_list: list = casedata['request_params']
    # 20220816再次对优化对文件上传，包括批量上传
    count = len(request_list)
    for i in range(count):
        filesdata = request_list[i].get('files')
        if filesdata:
            filesdata_tmp  = convert_files_to_stream(filesdata)
            request_list[i]['files'] = filesdata_tmp

    desc_list: list = casedata['description']
    assert_list: list = casedata['assert']
    response_list: list = casedata['response']
    # 于20230312 添加获取jschema_validate 数据
    jschema_list: list = casedata['jschema_validate']
    # 于20230312 改写返回逻辑
    # params_list = []
    requ_count = len(request_list)
    # resp_count = 0
    # # 判断是否需要处理响应结果。只有当为list时，且长度大于1时，才表示要处理相应的响应结果
    # if isinstance(response_list, list) and len(response_list) > 0:
    #     resp_count = len(response_list)
    # # 判断是否是否有数据依赖，逻辑同上
    # depend_count = 0
    # if isinstance(depend_list, list) and len(depend_list) > 0:
    #     depend_count = len(depend_list)
    #
    # # 于20230312 增加jschema_validate 相关的逻辑判断，逻辑同上。
    # jschema_count = 0
    # if isinstance(jschema_list,list) and len(jschema_list)>0:
    #     jschema_count = len(jschema_list)

    # for i in range(requ_count):
    #     if i <= (resp_count - 1) and i <= (depend_count - 1):
    #         tmp = [request_list[i], desc_list[i], assert_list[i], response_list[i], depend_list[i], run, story]
    #     elif i <= resp_count - 1:
    #         tmp = [request_list[i], desc_list[i], assert_list[i], response_list[i], None, run, story]
    #     elif i <= depend_count - 1:
    #         tmp = [request_list[i], desc_list[i], assert_list[i], None, depend_list[i], run, story]
    #     else:
    #         tmp = [request_list[i], desc_list[i], assert_list[i], None, None, run, story]
    #
    #     params_list.append(tmp)

    # 于20230312 重新改写返回逻辑，更加简洁
    params_list=[[request_list[i],__get_value(desc_list,i),__get_value(assert_list,i),
                  __get_value(response_list,i),__get_value(depend_list,i),__set_run(runlist,i),story,
                  __get_value(jschema_list,i) ] for i in range(requ_count)]

    return params_list


def __get_value(listdata:list,index):
    if listdata == None or listdata == "":
        return None
    count = len(listdata)
    if index <= count-1:
        return listdata[index]
    else:
        return None


def __set_run(runlist:list,index):
    """
    逻辑规则如下:
    1:先检查runlist的类型是否为list,当为list时,再进行如下逻辑判断
        a:判断list元素的值,
            当值的类型为str时进行转换为小写,判断是否为false,只有当为false时,则返回False;其他值均返回True;
            当值的类型的bol时,是啥就返回啥;
            当下标越界时,直接返回True
    2:当传入的值为bool值时,
        a: 若为True,则表示所有的case均运行,均返回True
        b: 若为False,表表示所有的case均不运行,均返回False

    """
    # 设置默认值
    run = True
    if isinstance(runlist,list):
        count = len(runlist)
        if index > count-1:
            return run
        else:
            tmp = runlist[index]
            # 当值的类型为str时
            if isinstance(tmp,str):
                tmp = tmp.lower().strip()
                if tmp == "false":
                    run = False
            # 为bool时
            elif isinstance(tmp,bool):
                if tmp == False:
                    run = False
            # 其他情况均为默认值 True
            return run

    # 表示为bool值
    else:
        # 直接返回该值
        return runlist