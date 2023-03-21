#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/19 11:20'
import pytest
import logging
import datetime
from utils.send_wechat import send_wechat
import os
import sys


@pytest.fixture(scope='session', autouse=True)
def send_mail():
    logging.info('发送邮件了')


def pytest_sessionfinish(session):
    result = session.exitstatus
    print('result: ', result)
    print('session: ', session)
    print('os.getcwd(): ', os.getcwd())
    curr_path = os.getcwd()
    report_path = curr_path + '\\report\\report.html'
    # with open(report_path, 'r', encoding='utf-8') as f:
    #     text = f.read()
    # text = text.replace('assets/style.css', 'http://49.235.95.49:8085/media/images/20230320/style.css')
    # with open(report_path, 'w', encoding='utf-8') as f:
    #     f.write()


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # 执行原始 pytest_terminal_summary 函数
    yield
    # 获取测试结果的摘要信息
    stats = terminalreporter.stats
    total = terminalreporter._numcollected
    passed = len(stats.get('passed', []))
    failed = len(stats.get('failed', []))
    error = len(stats.get('error', []))
    skipped = len(stats.get('skipped', []))
    duration = stats.get('duration', 0)
    send_wechat(total, passed, failed, error, skipped)


def pytest_html_report_title(report):
    curr_time = datetime.datetime.now()
    report.title = u"自动化测试报告 {}".format(curr_time)
    print('执行到这里了')
    print('report.title: ', report.title)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if item.function.__doc__ is None:
        report.description = str(item.function.__name__)
    else:
        report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("unicode_escape").decode("utf-8")


