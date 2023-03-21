#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2023/3/19 14:20'

case_root_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=adcce99f-db7a-451f-88aa-405451816266'
text_template = {
    "msgtype": "template_card",
    "template_card": {
        "card_type": "text_notice",
        "main_title": {
            "title": "自动化测试结果"
        },
        "sub_title_text": "desc",
        "card_action":{
            "type": 1,
            "url": "https://work.weixin.qq.com/?from=openApi",
            "appid": "APPID",
            "pagepath": "PAGEPATH"
        }
    }
}