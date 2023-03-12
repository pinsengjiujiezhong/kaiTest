#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/11 22:12'

import pytest
import allure
from customcase.base.apiBase import ApiBase
from .module_params import *
import random


class TestProject:

    def setup_class(self):
        """
        平台登录
        :return:
        """
        apiBase = ApiBase()
        self.paramsApi = apiBase.getPublicParamsApi()

    @allure.story('新建参数数据')
    def test_new_params(self):
        """
        新建参数数据
        :return:
        """
        name = 'username%d'% random.randint(10000, 90000)
        data = random.randint(1000, 60000)
        result = self.paramsApi.add_params_api(name=name, data=data)
        assert result['code'] == 0
        params_list = self.paramsApi.get_params_list_api()
        assert params_list['data']['paramsList'][0]['name'] == name
        return result['info']

    @allure.story('获取参数数据列表')
    def test_get_params_list(self):
        """
        获取参数数据列表
        :return:
        """
        old_total = self.paramsApi.get_params_list_api()['data']['total']
        name = self.test_new_params()['name']
        result = self.paramsApi.get_params_list_api()['data']
        assert result['total'] - 1 == old_total
        assert result['paramsList'][0]['name'] == name
        return result['paramsList']

    @allure.story('搜索参数数据列表')
    def test_search_params_list(self):
        """
        获取参数数据列表
        :return:
        """
        name = self.test_new_params()
        result = self.paramsApi.get_params_list_api(keyword=name)
        for params in result['data']['paramsList']:
            assert name in params['name']

    @allure.story('修改参数数据')
    def test_update_params(self):
        params = self.test_get_params_list()[0]
        pid = params['id']
        name = 'username%d'% random.randint(10000, 90000)
        data = str(random.randint(1000, 60000))
        new_params = self.paramsApi.update_params_api(id=pid, data=data, name=name)['info']
        assert new_params['name'] == name
        assert new_params['data'] == data
        return pid, name, data

    @allure.story('获取参数详情')
    def test_get_params_detail(self):
        pid, name, data = self.test_update_params()
        new_params = self.paramsApi.get_params_detail_api(pid=pid)['info']
        assert new_params['name'] == name
        assert new_params['data'] == data
        return new_params

    @allure.story('删除参数数据')
    def test_del_params(self):
        old_info = self.paramsApi.get_params_list_api()['data']
        pid = old_info['paramsList'][0]['id']
        name = old_info['paramsList'][0]['name']
        result = self.paramsApi.del_params_api(pid)
        assert result['code'] == 0
        new_info = self.paramsApi.get_params_list_api()['data']
        assert old_info['total'] - 1 == new_info['total']
        assert not [name for item in new_info['paramsList'] if name == item['name']]





