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


class TestKnowledgePoints():
    def setup_method(self):
        if feature and feature!="":
            allure.dynamic.feature(feature)

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'login'))
    def test_login(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'knowledgePoints'))
    def test_knowledgePoints(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'knowledge-topic-content'))
    def test_knowledgeTopicContent(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()


