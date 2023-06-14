#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
import json
import traceback
import weChat
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/send", methods=['POST'])
def send():
    try:
        content = request.data
        # print(content)
        json_re = json.loads(content)
        print(json_re)
        # 获取微信号
        wx_nos = json_re['weChatNums']
        wx_msg = json_re['weChatMsg']
        # 获取接收者类型，是发消息给好友还是发消息到群，如果key为空，默认是好友
        msg_type = json_re.get('receiverType', 'friend')
        # print(msg_type)
        if msg_type == 'friend':
            for wx_no in wx_nos:
                # print(wx_no)
                weChat.send_friend_msg(wx_no, wx_msg)
        else:
            for wx_no in wx_nos:
                # print(wx_no)
                weChat.send_group_msg(wx_no, wx_msg)
    except Exception as e:
        # print(e.message)
        print(traceback.print_exc())
        return json.dumps({'coed': '500', 'success': 'false', 'message': repr(e)})
    else:
        return json.dumps({'coed': '200', 'success': 'true', 'message': 'Send weChat message successfully'})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
