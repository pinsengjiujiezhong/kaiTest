#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/11 14:46'
import os
import sys
sys.path.append('E:\\Pycharm\\autoTest\\kaiTest')

import pytest
import allure
from customcase.base.apiBase import ApiBase
from .module_params import *
import random
import logging


class TestProject:

    def setup_class(self):
        """
        平台登录
        :return:
        """
        apiBase = ApiBase()
        self.projectApi = apiBase.getProjectApi()

    def new_project(self):
        host = '127.0.0.%d'% random.randint(1, 100)
        port = random.randint(1000, 60000)
        title = '这个是主机名称%d'% random.randint(10000, 90000)
        remark = '这个是备注%d'% random.randint(10000, 90000)
        self.projectApi.add_project_api(host=host, port=port, title=title, remark=remark)
        return title

    def get_project_list(self):
        return self.projectApi.get_project_list_api()['data']['projectList']

    @allure.story('新建项目数据')
    def test_new_project(self):
        """
        新建项目数据
        :return:
        """
        host = '127.0.0.%d'% random.randint(1, 100)
        port = random.randint(1000, 60000)
        title = '这个是主机名称%d'% random.randint(10000, 90000)
        remark = '这个是备注%d'% random.randint(10000, 90000)
        logging.info('发送添加项目数据请求--这个是日志')
        result = self.projectApi.add_project_api(host=host, port=port, title=title, remark=remark)
        assert result['code'] == 0
        project_list = self.projectApi.get_project_list_api()['data']['projectList']
        assert project_list[0]['title'] == title
        return title

    @allure.story('获取项目数据列表')
    def test_get_project_list(self):
        """
        获取项目数据列表
        :return:
        """
        old_total = self.projectApi.get_project_list_api()['data']['total']
        title = self.new_project()
        result = self.projectApi.get_project_list_api()['data']
        assert result['total'] - 1 == old_total
        assert result['projectList'][0]['title'] == title
        return result['projectList']

    @allure.story('搜索项目数据列表')
    def test_search_project_list(self):
        """
        获取项目数据列表
        :return:
        """
        title = self.test_new_project()
        project_list = self.projectApi.get_project_list_api(keyword=title)['data']['projectList']
        for project in project_list:
            assert title in project['title']

    @allure.story('修改项目数据')
    def test_update_project(self):
        project = self.test_get_project_list()[0]
        pid = project['id']
        host = '127.0.0.%d'% random.randint(1, 100)
        port = str(random.randint(1000, 60000))
        title = '这个是主机名称%d'% random.randint(10000, 90000)
        remark = '这个是备注%d'% random.randint(10000, 90000)
        logging.info('this send request')
        result = self.projectApi.update_project_api(id=pid, host=host, port=port, title=title, remark=remark)
        assert result['code'] == 0
        new_project = self.projectApi.get_project_detail_api(pid=pid)['data']
        assert new_project['host'] == host
        assert new_project['port'] == port
        assert new_project['title'] == title
        return new_project['id'], host, port, title

    @allure.story('获取项目详情')
    def test_get_project_detail(self):
        pid, host, port, title = self.test_update_project()
        new_project = self.projectApi.get_project_detail_api(pid=pid)['data']
        assert new_project['host'] == host
        assert new_project['port'] == port
        assert new_project['title'] == title

    @allure.story('删除项目数据')
    def test_del_project(self):
        old_info = self.projectApi.get_project_list_api()['data']
        pid = old_info['projectList'][0]['id']
        title = old_info['projectList'][0]['title']
        result = self.projectApi.del_project_api(pid)
        assert result['code'] == 0
        new_info = self.projectApi.get_project_list_api()['data']
        assert old_info['total'] - 1 == new_info['total']
        assert not [title for item in new_info['projectList'] if title == item['title']]





