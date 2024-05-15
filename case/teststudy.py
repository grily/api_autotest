# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2022/8/1 19:27
@Author: yuanhuanhuan
@File：teststudy.py
"""
import pytest
import allure
from common.get_caseyml_data import get_ymlfile_data
from common.get_request_params import get_params
from common.api_base import ApiBase

ymldata, feature = get_ymlfile_data()


class TestStudy():
    def setup_method(self):
        if feature and feature != "":
            allure.dynamic.feature(feature)

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'login'))
    def test_login(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'uploadfile'))
    def test_uploadfile(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'experiment'))
    def test_experiment(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'study'))
    def test_study(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'editstudy'))
    def test_edit_study(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'duplicate'))
    def test_duplicate(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'study_list'))
    def test_study_list(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'my_info'))
    def test_my_info(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'create_class'))
    def test_create_class(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'join_class'))
    def test_join_class(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    # 前端已经去除精品学案直接发布作业功能，学案相关接口不再请求精品学案
    # @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
    #                          get_params(ymldata, 'resource_study_list'))
    # def test_resource_study_list(self, req_params, desc, asert, resp, depend, run, story, jschema):
    #     api_base = ApiBase.getinstance(req_params, desc, asert, resp, depend, run, story, jschema)
    #     api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'publish_study'))
    def test_publish_study(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'class_study_list'))
    def test_class_study_list(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'class_study_info'))
    def test_class_study_info(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'submit_homework'))
    def test_submit_homework(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'homework_list'))
    def test_homework_list(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'homework_info'))
    def test_homework_info(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'study_class_list'))
    def test_study_class_list(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'revoke_study'))
    def test_revoke_study(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema",
                             get_params(ymldata, 'release_class'))
    def test_release_class(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()

    @pytest.mark.parametrize("req_params,desc,asert,resp,depend,run,story,jschema", get_params(ymldata, 'delete_study'))
    def test_delete_study(self, req_params, desc, asert, resp, depend, run, story, jschema):
        api_base = ApiBase.get_instance(req_params, desc, asert, resp, depend, run, story, jschema)
        api_base.run_case()
