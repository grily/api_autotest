# -*- coding: UTF-8 -*-
# 设置utf-8  显示中文

import pytest
from jsonpath import jsonpath


def handle_assert_exp(response, assert_exps):
    # 脚本中的变量名称和函数中定义的一致 才能执行eval
    # 1.接口响应状态200 2.响应值中的某一个字段等于 2.响应值中的某一个数组的长度
    print(assert_exps)
    resp_json = response.json()
    if isinstance(assert_exps, list):
        for asert_exp in assert_exps:
            eval(asert_exp)
    else:
        eval(assert_exps)

