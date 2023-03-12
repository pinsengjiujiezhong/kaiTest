#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/11 15:02'
import os

from autoCase.kaiPlatform.customapi.project import ProjectApi
from autoCase.kaiPlatform.customapi.public_params import PublicParamsApi
from .params import username, password, domain, login_headers
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)


class ApiBase:

    def init(self):
        self.login()

    def login(self):
        data = {
            'username': username,
            'password': password
        }
        res = self.base.run_api(path='/users/login', data=data, thick=True)
        cookies = res.cookies.get_dict()
        self.base.headers['Cookie'] = '; '.join(['{}={}'.format(key, cookies[key]) for key in cookies])
        print(self.base.headers)

    def getProjectApi(self) -> ProjectApi:
        self.base = ProjectApi(domain, login_headers)
        self.init()
        return self.base

    def getPublicParamsApi(self) -> PublicParamsApi:
        self.base = PublicParamsApi(domain, login_headers)
        self.init()
        return self.base
