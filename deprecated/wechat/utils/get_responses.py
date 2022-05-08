# libraries
import requests
import urllib.request

# submodules
from utils.chatbot import chatbot

# ********** GLOBAL-VARIABLES ********** #
# Note that all global variables should be BIG_CASE.
KEY = 'bafb088e33ec404b917baf9aaae34eac'


# ********** COMMON-FUNCTIONS ********** #
# get the response from Turing API
def get_response_turing(msg):
    global KEY
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')


# get the response from the deep learning ChatterBot
def get_response_chatterbot(text):
    chatbot_object = chatbot(text)
    return chatbot_object.chatbot_caller()


# get the response from doutula
def get_response_doutula(msg):
    # get the response using the turing robot
    response = get_response_turing(msg)  # type(response) == str

    # use the response to get the according picture from doutula
    apiUrl = 'http://api.yanxi520.cn/api/bucket.php'
    data = {
        'msg': response
    }
    r = requests.get(apiUrl, params=data)
    imgurl = r.content.decode('utf-8')
    urllib.request.urlretrieve(imgurl, "./DoutulaImages/doutu.jpg")  # 保存图片名为doutu.jpg的本地图片

    return
