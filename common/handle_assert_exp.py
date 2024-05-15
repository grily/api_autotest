# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022-7-4 11:19
@Author: test
@File：handle_assert_exp.py
"""
import re
import pytest
import simplejson
from jsonpath import jsonpath
from common.get_json_filepath import get_json_filepath
from common.online_data import OnlineData


def handle_assert_exp(request, assert_exps, request_params) -> str:
    '''
    处理断言表达式，将表达式转化为正确的方便查阅的结果  \n
    :param request: requests.request() request请求。
    :param assert_exps: 原始断言表达式。
    :return: 处理后的表达式,如pytest.assume(200== 200)。
    '''

    req = request
    req_json = None
    req_text = req.text
    try:
        req_json = req.json()
    except Exception as e:
        msg = f"在获取request的响应json结果时，发生了异常，信息为：{e}"
        pytest.fail(msg)
    # # 表达式中是否有[0]的标识
    # flag0=False
    # # 表达式中是否有状态码比较的标识
    # codeflag = False

    # 处理后的表达式
    exp_list = []

    # 判断断言表达式是否为列表，即一个case有多重断言
    if isinstance(assert_exps, list) and len(assert_exps) > 0:

        for asert_exp in assert_exps:
            # exp_str = _extract_exp_content(req, asert_exp)
            # exp_list.append(exp_str)
            content_list = _extract_exp_content(req, asert_exp)
            suffix = content_list[0]
            # print(f"suffix's type is: {type(suffix)}")
            prefix = content_list[1]
            prefix = _handle_prefix_content(request_params, prefix)
            if isinstance(suffix, str):
                exp_str = f'pytest.assume( {prefix} "{suffix}")'
            else:
                exp_str = f"pytest.assume( {prefix} {suffix})"
            exp_list.append(exp_str)

    else:
        # exp_str = _extract_exp_content(req, assert_exps)
        # exp_list.append(exp_str)
        content_list = _extract_exp_content(req, assert_exps)
        suffix = content_list[0]
        prefix = content_list[1]
        prefix = _handle_prefix_content(request_params, prefix)
        if isinstance(suffix, str):
            suffix = f"{suffix}"
            exp_str = f'pytest.assume( {prefix} "{suffix}")'
        else:
            exp_str = f"pytest.assume( {prefix} {suffix})"

        exp_list.append(exp_str)

    return exp_list


def _extract_exp_content(req, asert_exp) -> str:
    '''
    提取表达式中的内容
    :param req: request请求
    :param asert_exp: 断言表达式
    :return: 返回拼接好的，提取后的内容。
    '''
    # 表达式中有这些变量
    req_text = req.text
    req_json = req.json()
    # 对标识重新赋值
    flag0 = False
    codeflag = False
    if "(jsonpath(" in asert_exp:
        # 提取表达式前半段内容
        exp_content_prefix = re.findall(r"pytest\.assume\((.+?)\(jsonpath", asert_exp)
        # 检测是否是[0]
        # 要使用)[0] 进行判断,防止和前面的表达式中的[0]重合,这样就会导致提取的数据有误
        if ")[0]" in asert_exp:
            # 提取表达式后半段内容，主要是jsonpath中的表达式内容
            exp_content_suffix = re.findall(r"\(jsonpath\((.+?)\)\[0\]\)\)", asert_exp)
            # 设置标识
            flag0 = True
        # 表示没有[0]
        else:
            # 提取jsonpath中的表达式内容
            exp_content_suffix = re.findall(r"\(jsonpath\((.+?)\)\)\)", asert_exp)

    elif "jsonpath(" in asert_exp:
        # 提取表达式的前半段内容
        exp_content_prefix = re.findall(r"pytest\.assume\((.+?)jsonpath", asert_exp)
        # 要使用)[0] 进行判断,防止和前面的表达式中的[0]重合,这样就会导致提取的数据有误
        if ")[0]" in asert_exp:
            # 提示jsonpath中的表达式内容
            exp_content_suffix = re.findall(r"jsonpath\((.+?)\)\[0\]\)", asert_exp)
            flag0 = True
        else:
            exp_content_suffix = re.findall(r"jsonpath\((.+?)\)\)", asert_exp)

    # 判断是否进行了状态码比较。
    elif "req.status_code" in asert_exp:
        codeflag = True
        exp_content_prefix = re.findall(r"pytest\.assume\((.+?)req\.status_code", asert_exp)

    # 当进行状态码比较时
    if codeflag:
        value = req.status_code

    elif flag0:
        value = jsonpath(*eval(exp_content_suffix[0]))[0]

    else:
        value = jsonpath(*eval(exp_content_suffix[0]))
    # # 拼接表达式
    # exp_str = f"pytest.assume({exp_content_prefix[0]} {value})"

    # return [exp_str,exp_content_prefix[0]]
    return [value, exp_content_prefix[0]]


def handle_assert(request, asert_exps) -> None:
    '''
    处理断言  \n
    :param request: request请求
    :param asert_exps: 断言表达式
    :return: None
    '''
    req = request
    req_text = req.text
    req_json = req.json()
    if isinstance(asert_exps, list):
        for asert_exp in asert_exps:
            eval(asert_exp)
    else:
        eval(asert_exps)


def _handle_prefix_content(request_param: dict, prefix_content: str) -> str:
    ''''''
    params = request_param
    # 要从请求参数中提取字段值 标识
    req_param_str = "req_param"
    # 表达要通过 getattr() 来获取字段值 标识
    online_data_str = "online_data"
    # 表达 要读取json文件来获取字段值 标识
    json_file_str = "json_file"
    # 参数化的标记
    param_flag = "$$"
    # 表达式内的分割符 标记
    split_flag = "::"

    # 断言中的前半部分的 表达式。
    content = prefix_content
    # 先判断是否有表达式的标识
    if param_flag in prefix_content:
        '''
        表达式如下： 
        $$req_param::$.params.username::[0]$$  或 $$req_param::$.params.username::0$$ 
        $$online_data::token$$
        $$json_file::0016.json::token$$
        '''

        # 判断是否为request_param 参数
        content_list = content.split(param_flag)
        # 前半部分中真正的表达式所在的位置
        content_tmp = content_list[1]
        content_list_tmp = content_tmp.split(split_flag)
        count = len(content_list_tmp)
        m_content_tmp = content

        if req_param_str in content_list_tmp[0]:
            ''''''
            # content_list_tmp = content_tmp.split(split_flag)
            # count = len(content_list_tmp)
            # m_content_tmp = content

            # 再判断个数
            if count == 2:
                ''''''
                m_content_tmp = jsonpath(params, content_list_tmp[1])

            # 表示有下标
            elif count == 3:
                if '[' in content_list_tmp[-1] or ']' in content_list_tmp[-1]:
                    # 将str转为list,如 '[0]' 转化为 [0]
                    last_value = eval(content_list_tmp[-1])
                elif '[' not in content_list_tmp[-1] and ']' not in content_list_tmp[-1]:
                    # 提取数字,要将str转化为int
                    last_value = [eval(content_list_tmp[-1])]
                m_content_tmp = eval(f'{jsonpath(params, content_list_tmp[1])}{last_value}')
            # return m_content_tmp

        elif json_file_str in content_list_tmp[0]:
            ''''''
            # content_list_tmp = content_tmp.split(split_flag)
            # count = len(content_list_tmp)
            # m_content_tmp = content

            # 不考虑多key的情况，因为在存response数据时，会将该response的会用到的数据逐一的保存到json文件的不冲突的key中。
            if count == 3:
                file = content_list_tmp[1]
                key = content_list_tmp[2]
                fp = get_json_filepath(file)

                with open(fp, encoding='utf-8', mode='r') as ff:
                    fp_data = simplejson.loads(ff.read(), encoding='utf-8')
                m_content_tmp = fp_data[key]
            # return m_content_tmp

        elif online_data_str in content_list_tmp[0]:
            ''''''
            # content_list_tmp = content_tmp.split(split_flag)
            # count = len(content_list_tmp)
            # m_content_tmp = content

            if count == 2:
                key = content_list_tmp[1]
                m_content_tmp = getattr(OnlineData, key)
            # return m_conternt_tmp

        return f'{content_list[0]}{m_content_tmp}{content_list[2]}'
    else:
        return content