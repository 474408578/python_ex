from wxpy import *


bot = Bot(cache_path='wxpy.pkl', console_qr=True)
my_friends = bot.friends(update=False)
print(my_friends.stats_text())

nick_name = ''
wx_signature = ''

for friend in my_friends:
    # friend.raw得到一个字典
    nick_name += friend.raw['NickName']
    wx_signature += friend.raw['Signature']



print(nick_name, wx_signature)
embed()