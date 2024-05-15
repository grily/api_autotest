# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022-6-27 11:58
@Author: test
@File：testdemo.py.py
"""
import pytest
import allure
from common.get_caseyml_data import get_ymlfile_data
from common.get_request_params import get_params
from common.api_base import ApiBase

ymldata,feature = get_ymlfile_data()


class TestDemo():
    # def setup(self):
    # pytest 7.2版本之后的写法,之前的写法在后续版本中将会被彻底弃用。
    def setup_method(self):
        if feature and feature!="":
            allure.dynamic.feature(feature)

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'login'))
    def test_login(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'checklogin'))
    def test_checklogin(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()




