# -*- coding: UTF-8 -*-
# 设置utf-8  显示中文
"""
@Create Time: 2023/2/7 15:27
@Author: liruige
@File：test_knowledgePoints.py
"""
import pytest
import allure
from common.get_caseyml_data import get_ymlfile_data
from common.get_request_params import get_params
from common.api_base import ApiBase


ymldata, feature = get_ymlfile_data()


class TestExam():
    def setup_method(self):
        if feature and feature!="":
            allure.dynamic.feature(feature)

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'appLogin'))
    def test_login(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'userExamList'))
    def test_userExamList(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()
    # @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'comprehensiveStatistics'))
    # def test_comprehensive(self, req_params, desc, asert, resp, depend, run, story, jschema):
    #     api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
    #     api_base.run_case()
    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'singleStatistic'))
    def test_singleStatistic(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()


