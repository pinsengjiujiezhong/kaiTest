#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/19 11:59'
from data.wechat_data import case_root_url, text_template

import requests


headers = {
    "Content-Type": "text/plain"
}


def send_wechat(total=1, passed=1, failed=1, error=1, skipped=1):
    desc = ' 运行数: {total}条 \n 成功数: {passed}条 \n 失败数: {failed}条 \n 错误数: {error}条 \n 跳过数: {skipped}条'. format(
        total=total, passed=passed, failed=failed, error=error, skipped=skipped)
    text_template['template_card']['sub_title_text'] = desc
    response = requests.post(case_root_url, json=text_template, headers=headers)
    print(response.text)


if __name__ == '__main__':
    send_wechat()
