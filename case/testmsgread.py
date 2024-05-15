# -*- coding: UTF-8 -*-
# 设置utf-8  显示中文
"""
@Create Time: 2022-6-27 11:58
@Author: QinTianren
@File：testmsgread.py
"""
import pytest
import allure
from common.get_caseyml_data import get_ymlfile_data
from common.get_request_params import get_params
from common.api_base import ApiBase

ymldata,feature = get_ymlfile_data()

class Testmsgread():
    def setup_method(self):
        if feature and feature!="":
            allure.dynamic.feature(feature)

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",get_params(ymldata,'login'))
    def test_login(self,req_params,desc,asert,resp,depend,run,story,jschema):
        api_base = ApiBase.get_instance(req_params,desc,asert,resp,depend,run,story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classcreate'))
    def test_classcreate(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'stujoinclass'))
    def test_stujoinclass(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classupdate'))
    def test_classupdate(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'resourcelist'))
    def test_resourcelist(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'createcomment'))
    def test_createcomment(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'commentlist'))
    def test_commentlist(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'createcommentson'))
    def test_createcommentson(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'loginclassmsg'))
    def test_loginclassmsg(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'logincommentmsg'))
    def test_logincommentmsg(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'loginsystemmsg'))
    def test_loginsystemmsg(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'loginmsgread'))
    def test_loginmsgread(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'classrelease'))
    def test_classrelease(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'loginunreadmsg'))
    def test_loginunreadmsg(self, req_params, desc, asert, resp, depend, run, story,jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story,jschema)
        api_base.run_case()