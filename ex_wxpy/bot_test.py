from wxpy import *
import time
import requests
import json

bot = Bot(cache_path='wxpy.pkl', console_qr=True) # 启用缓存，保存登录状态

# bot.file_helper.send("hello, I'm Felix") # 文件助手

# 发送指定消息
# my_friend = bot.friends().search('xiangsong')[0]
# my_friend.send("I'm a bot")
# my_friend.send_image("images\\andr.jpg")
# my_friend.send_video("a.mp4")
# my_friend.send_file("b.txt")



# 群发
# my_friends = bot.friends(update=False) # 获取所有好友
# my_friends.pop(0)
# print(my_friends[:3])
# for i in range(2):
#     friend = my_friends[i]
#     friend.send('Good Job!')
#     time.sleep("don't reply")


# 获取活跃微信群数
# groups = bot.groups(update=False)
# print(len(groups))
# for group in groups:
#     print(group)



# 个人聊天机器人
# my_friend = bot.friends().search('xiangsong')[0]
# my_friend.send("I'm a bot")
#
# @bot.register(my_friend)
# def my_friend_message(msg):
#     print('[received message]' + str(msg))
#     if msg.type !='Text':
#         ret = "I can't understand"
#     elif "where are you from?" in msg:
#         ret = "I come from China"
#     else:
#         ret = "I don't know"
#     print(ret)
#     return ret


# 图灵聊天机器人，http://www.tuling123.com/ 创建机器人以获取api_key
# tuling = Tuling(api_key='8960499d6b3e4ef2abefb4cb40a61699')
# print('Start Tuling')
my_friend = bot.friends().search('xiangsong')[0]
my_friend.send('给我发个消息试试！')


def auto_ai(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "8960499d6b3e4ef2abefb4cb40a61699"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "userid"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result['text']

@bot.register(my_friend)
def my_friend_message(msg):
    print('[received]' + str(msg))
    if msg.type != 'Text':
        ret = 'I am so stupid!'
    else:
        ret = auto_ai(msg.text)
    print('[send]' + str(ret))
    return ret


# @bot.register(my_friend)
# def reply_my_friend(msg):
#     tuling.do_reply(msg)

embed() # 进入命令行之后阻塞线程