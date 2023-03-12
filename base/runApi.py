#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/8 22:19'

import requests
import os, sys
import json


class runApi:
    def __init__(self, domain='', headers={}):
        self.headers = headers
        self.domain = domain

    def request(self, method, url, headers, data, params, proxies, files):
        response = response = requests.request(method, url, data=data, params=params, headers=headers, proxies=proxies, files=files)
        return response

    def run_api(self, path, method="POST", headers={}, data={}, params={}, proxies=[], files=None, thick=None, error=False):
        url = self.domain + path
        data = json.dumps(data)
        self.headers.update(headers)
        response = self.request(method, url, headers=self.headers, data=data, params=params, proxies=proxies, files=files)
        if thick:
            return response
        try:
            return json.loads(response.text)
        except Exception as e:
            print(e)
            return response.text

    def get_cookies(self):
        pass

