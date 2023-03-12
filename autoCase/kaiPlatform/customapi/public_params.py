#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/11 22:12'
from base.runApi import runApi


class PublicParamsApi(runApi):
    def get_params_list_api(self, keyword='', page=1, limit=10):
        """
        搜索公共参数数据
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
        path, method, headers = '/public/params/', 'GET', {}
        return self.run_api(path, method, headers, params=params)

    def get_params_detail_api(self, pid):
        """
        获取公共参数详情
        :param pid: 项目id
        :return:
        """
        params = {
            'pid': pid
        }
        path, method, headers = '/public/params/detail/', 'GET', {}
        return self.run_api(path, method, headers, params=params)

    def add_params_api(self, name, data, type='String', content=''):
        """
        添加项目
        :param name: 参数名称
        :param type: 参数类型
        :param data: 数据
        :param content: 备注
        :return:
        """
        data = {
            'name': name,
            'type': type,
            'data': data,
            'content': content
        }
        path, method, headers = '/public/params/', 'POST', {}
        return self.run_api(path, method, headers, data=data)

    def update_params_api(self, id, name, data, type='String', content=''):
        """
        编辑参数
        :param name: 参数名称
        :param type: 参数类型
        :param data: 数据
        :param content: 备注
        :return:
        """
        data = {
            'id': id,
            'name': name,
            'type': type,
            'data': data,
            'content': content
        }
        path, method, headers = '/public/params/detail/', 'POST', {}
        return self.run_api(path, method, headers, data=data)

    def del_params_api(self, pid):
        """
        删除参数
        :param pid: 项目id
        :return:
        """
        data = {
            'pid': pid
        }
        path, method, headers = '/public/params/detail/', 'DELETE', {}
        return self.run_api(path, method, headers, data=data)
