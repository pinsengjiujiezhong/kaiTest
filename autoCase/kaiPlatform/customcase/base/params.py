#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/11 16:29'
import platform
username = '13533630193@163.com'
password = 'zhang001'
domain = 'http://127.0.0.1:8000'
if platform.system().lower() == 'linux':
    domain = 'http://49.235.95.49:8085'
if platform.system().lower() == 'windows':
    domain = 'http://127.0.0.1:8000'
login_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '57',
    'Content-Type': 'application/json',
    'envtag': 'yzg',
    'Host': '127.0.0.1:8000',
    'Origin': 'http://127.0.0.1:8000',
    'Pragma': 'no-cache',
    'Referer': 'http://127.0.0.1:8000/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) =Chrome/110.0.0.0 Safari/537.36'
}
