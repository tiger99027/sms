# -*- coding: utf-8 -*-
from wxpy import *

# 启动微信机器人
#bot = Bot()
bot = Bot(console_qr=2, cache_path=True)
# bot = Bot(console_qr=-1, cache_path=None)


# 发送消息至好友
def send_friend_msg(wx_num, message):
    print('The weChat number is:'+wx_num)
    print('The weChat message is:'+message)
    # bot.file_helper.send(message)
    # 查找用户,通过电话号码是查不到的，只能通过备注名称找
    # print(bot.friends())
    it_chart_friend = bot.core.search_friends(name=wx_num)[0]
    # print(it_chart_friend)
    # 找到改用户的备注名
    user_name = it_chart_friend['UserName']
    # print('The user name:'+user_name)
    bot.core.send(message, user_name)
    # my_friend = bot.friends().search(remark_name)[0]
    # my_friend.send(message)


# 发送消息至微信群中
def send_group_msg(group_name, message):
    print('The group name is:'+group_name)
    print('The weChat message is:'+message)
    # print(bot.groups())
    # 查找分组
    group = bot.groups().search(group_name)[0]
    # 发送文本消息
    # group.send(u'@Lys ' + message)
    group.send(message)


