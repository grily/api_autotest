# -*- coding: UTF-8 -*-
# 设置utf-8  显示中文

import pytest
from jsonpath import jsonpath
import json
import re


def handle_assert_exp(req, assert_exps):
    # 脚本中的变量名称和函数中定义的一致 才能执行eval
    # 1.接口响应状态200 2.响应值中的某一个字段等于 2.响应值中的某一个数组的长度
    print(assert_exps)
    req_json = req.json()
    if isinstance(assert_exps, list):
        for asert_exp in assert_exps:
            if "$$" in asert_exp:
                asert_exp = assume_and_exec(asert_exp)
                print(type(asert_exp))
                print(asert_exp)
            eval(asert_exp)
    else:
        eval(assert_exps)

def parse_and_extract_value(expression):
    # 解析表达式
    parts = expression.split('::')
    file_path = parts[1]
    path = "C:/Users/EEO/PycharmProjects/nb_api_autotest_lrg/nb_api_autotest/response_data/"
    path = path+file_path
    key = parts[2]

    key = key.split('$$')[0]

    # 读取 JSON 文件
    with open(path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 提取具体值
    extracted_value = json_data.get(key)

    return extracted_value


# 定义一个函数来替换占位符并执行断言
def assume_and_exec(expression):
    # 解析并提取值
    expected_value = parse_and_extract_value(expression)
    #使用expected_value替换$$$$ 中间部分内容
    pattern = r'\$\$(.*?)\$\$'
    new_string = re.sub(pattern, f"{expected_value}", expression)
    return new_string
