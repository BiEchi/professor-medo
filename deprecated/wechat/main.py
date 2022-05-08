# libraries
import itchat

# submodules
from utils.schedule_reply import schedule_reply
from utils.send_email import send_email
from utils.OCR import OCR_extraction
from utils.get_responses import *

# ********** GLOBAL-VARIABLES ********** #
# Note that all global variables should be BIG_CASE.
COUNTER = 0


# ********** RUNTIME-FUNCTIONS ********** #
# private chatting
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=False, isMpChat=False)
def private_reply(msg):

    # SCHEDULE (BLOCKING) SOLUTION
    schedule_reply(msg)
    reply = get_response_chatterbot(msg['Text'])
    itchat.send_msg(msg=str(reply), toUserName=msg['FromUserName'])

    # E-MAIL SOLUTION
    # itchat.send_msg(msg="你想要给Jack留言吗？可以写下内容，我会转发到他的邮箱去哦～", toUserName=msg['FromUserName'])
    # if second_time_send():
    #     send_email(msg, 'private')
    #     itchat.send_msg(msg="已经转发过去啦～", toUserName=msg['FromUserName'])

    # update the global variable COUNTER
    global COUNTER
    COUNTER += 1
    print(COUNTER)
    return


# private chatting for photos
@itchat.msg_register(itchat.content.PICTURE, isFriendChat=True, isGroupChat=False, isMpChat=False)
def private_reply_picture(msg):
    # download the message to dir ItchatDownloaded/
    msg.download("ItchatDownloaded/" + msg.fileName)
    # receive a picture, read the picture using the key 'Text', and use OCR extraction to extract the words
    message_content = OCR_extraction(msg)
    # send the words to doutula, and save the result in ./DoutulaImages
    get_response_doutula(message_content[0])  # feed in a string
    # send the image in the local place to the frined who sent you the expression/picture
    itchat.send_image(fileDir="./DoutulaImages/doutu.jpg", toUserName=msg['FromUserName'])


# group chatting
@itchat.msg_register(itchat.content.TEXT, isFriendChat=False, isGroupChat=True, isMpChat=False)
def group_reply(msg):
    if msg['isAt'] is True:
        send_email(msg, 'group')
        itchat.send_msg(msg="@他的相关内容已经通过邮件发送给Jack啦，他等下就会来群里查看噢～", toUserName=msg['FromUserName'])


# ********** TRIGGER ********** #
if __name__ == '__main__':
    # parameters for auto_login: enableCmdQR=2 for CMD QR code, hotReload=True for a hot swap
    itchat.auto_login(hotReload=True)
    # execute the whole program, begin listening
    itchat.run()
