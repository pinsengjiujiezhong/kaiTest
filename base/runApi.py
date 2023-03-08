#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/8 22:19'

import requests
import os, sys
import json


class runApi:
    def __init__(self):
        pass

    def run_api(self, url, method, headers={}, data={}, params={}, proxy={}, files=None):
        response = requests.request(url, method=method, headers=headers, data=data, params=params, proxy=proxy, files=files)
        try:
            result = json.loads(response.text)
            return result
        except Exception as e:
            print(e)
            return result

