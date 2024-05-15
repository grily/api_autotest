# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022-8-08 11:59
@Author: zhangxicheng
@File：testclassandstu.py
"""
import pytest
import allure
from common.get_caseyml_data import get_ymlfile_data
from common.get_request_params import get_params
from common.api_base import ApiBase

ymldata,feature = get_ymlfile_data()

class TestDemo():
    def setup_method(self):
        if feature and feature!="":
            allure.dynamic.feature(feature)

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'login'))
    def test_login(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    # @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'checklogin'))
    # def test_checklogin(self, req_params, desc, asert, resp, depend, run, story,jschema):
    #     api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
    #     api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classcreate'))
    def test_classcreate(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classmyandjoinlist'))
    def test_classmyandjoinlist(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classupdate'))
    def test_classupdate(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classintroduce'))
    def test_classintroduce(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'stujoinclass'))
    def test_stujoinclass(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'studentlist'))
    def test_studentlist(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'studentrename'))
    def test_studentrename(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'studentquit'))
    def test_studentquit(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'studentremove'))
    def test_studentremove(self, req_params, desc, asert, resp, depend, run, story,jschema):
        print(req_params)
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classrelease'))
    def test_classrelease(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()