import datetime
import itchat


# On work days, apply the schedule reply first
def schedule_reply(msg):
    current_time = datetime.datetime.now()
    # When in sleep
    if current_time.hour >= 23 or current_time.hour <= 2:
        itchat.send_msg(msg="Jack估计已经休息啦，早上再来联系吧～", toUserName=msg['FromUserName'])
    elif current_time.hour <= 9:
        itchat.send_msg(msg="Jack还没有起床哦，九点钟以后再来问问吧～", toUserName=msg['FromUserName'])
    # When available
    elif current_time.hour <= 10:
        itchat.send_msg(msg="正在通知Jack～请稍等一下", toUserName=msg['FromUserName'])
    # When busy
    elif current_time.hour <= 12:
        itchat.send_msg(msg="Jack正在忙哦，有什么事可以等下来找他～", toUserName=msg['FromUserName'])
    # When available
    elif current_time.hour <= 13:
        itchat.send_msg(msg="正在通知Jack～请稍等一下", toUserName=msg['FromUserName'])
    # When having a lunch break
    elif current_time.hour <= 14:
        itchat.send_msg(msg="Jack正在午休哦，有什么事可以两点钟以后来联系他～", toUserName=msg['FromUserName'])
    # When busy
    elif current_time.hour <= 17:
        itchat.send_msg(msg="Jack正在忙哦，有什么事可以等下来找他～", toUserName=msg['FromUserName'])
    # When available
    else:
        itchat.send_msg(msg="正在通知Jack～请稍等一下", toUserName=msg['FromUserName'])

    return