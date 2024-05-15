# -*- coding: UTF-8 -*-
# 设置utf-8  显示中文
"""
@Create Time: 2022-8-11 11:58
@Author: fengzixuan
@File：test_resources.py
"""
import pytest
import allure
from common.get_caseyml_data import get_ymlfile_data
from common.get_request_params import get_params
from common.api_base import ApiBase

ymldata,feature = get_ymlfile_data()

class Test_resources_list():
    def setup_method(self):
        if feature and feature!="":
            allure.dynamic.feature(feature)

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'login'))
    def test_login(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'checklogin'))
    def test_checklogin(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'tree'))
    def test_tree(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'knowledge'))
    def test_knowledge(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'list'))
    def test_list(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'category'))
    def test_category(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'detail'))
    def test_detail(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'recommend'))
    def test_recommend(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'operate'))
    def test_operate(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()




