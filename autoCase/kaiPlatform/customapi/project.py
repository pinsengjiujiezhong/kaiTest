#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/11 14:46'
from base.runApi import runApi


class ProjectApi(runApi):

    def get_project_list_api(self, keyword='', page=1, limit=10):
        """
        搜索项目数据
        :param keyword: 关键字
        :param page: 页数
        :param limit: 分页大小
        :return:
        """
        params = {
            'keyword': keyword,
            'page': page,
            'limit': limit
        }
        path, method, headers = '/project/info/', 'GET', {}
        return self.run_api(path, method, headers, params=params)

    def get_project_detail_api(self, pid):
        """
        获取详情
        :param pid: 项目id
        :return:
        """
        params = {
            'pid': pid
        }
        path, method, headers = '/project/detail/', 'GET', {}
        return self.run_api(path, method, headers, params=params)

    def add_project_api(self, host, port, title, remark=""):
        """
        添加项目
        :param host: 主机地址
        :param port: 端口
        :param title: 名称
        :param remark: 备注
        :return:
        """
        data = {
            'host': host,
            'port': port,
            'title': title,
            'remark': remark
        }
        path, method, headers = '/project/info/', 'POST', {}
        return self.run_api(path, method, headers, data=data)

    def update_project_api(self, id, host, port, title, remark):
        """
        编辑项目
        :param host: 主机地址
        :param port: 端口
        :param title: 名称
        :param remark: 备注
        :return:
        """
        data = {
            'id': id,
            'host': host,
            'port': port,
            'title': title,
            'remark': remark
        }
        path, method, headers = '/project/detail/', 'POST', {}
        return self.run_api(path, method, headers, data=data)

    def del_project_api(self, pid):
        """
        删除项目
        :param pid: 项目id
        :return:
        """
        data = {
            'pid': pid
        }
        path, method, headers = '/project/detail/', 'DELETE', {}
        return self.run_api(path, method, headers, data=data)
