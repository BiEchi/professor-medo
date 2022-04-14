#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------File Info-----------------------
Name: web.py
Description: web api support
Author: GentleCP
Email: me@gentlecp.com
Create Date: 2021/6/19
-----------------End-----------------------------
"""
import argparse
from fastapi import FastAPI
from fastapi import Response, Request
from WXBizMsgCrypt3 import WXBizMsgCrypt
from xml.etree.ElementTree import fromstring
import uvicorn
import openai
from corpwechatbot.chatbot import CorpWechatBot

f = open("./openai.key")
lines = f.read()
openai.api_key = lines
f.close()

f = open("./wecom/wecom.key")
lines = f.read()
bot = CorpWechatBot(key='e8c7cdd7-448b-4245-a0be-4907f1bfa6e3')
f.close()

app = FastAPI()

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--port', '-p', default=12000, type=int, help="port to build web server")
    arg_parser.add_argument('--token', '-t', type=str, help='token set in corpwechat app')
    arg_parser.add_argument('--aeskey', '-a', type=str, help='encoding aeskey')
    arg_parser.add_argument('--corpid', '-c', type=str, help='your corpwechat id')
    args = arg_parser.parse_args()
    return args

args = parse_args()
wxcpt = WXBizMsgCrypt(args.token, args.aeskey, args.corpid)

@app.get("/")
async def verify(msg_signature: str,
                 timestamp: str,
                 nonce: str,
                 echostr: str):
    '''
    验证配置是否成功，处理get请求
    :param msg_signature:
    :param timestamp:
    :param nonce:
    :param echostr:
    :return:
    '''
    ret, sEchoStr = wxcpt.VerifyURL(msg_signature, timestamp, nonce, echostr)
    if ret == 0:
        return Response(content=sEchoStr.decode('utf-8'))
    else:
        print(sEchoStr)

@app.post("/")
async def recv(msg_signature: str,
               timestamp: str,
               nonce: str,
               request: Request):
    '''
    接收用户消息，可进行被动响应
    :param msg_signature:
    :param timestamp:
    :param nonce:
    :param request:
    :return:
    '''
    body = await request.body()
    ret, sMsg = wxcpt.DecryptMsg(body.decode('utf-8'), msg_signature, timestamp, nonce)
    decrypt_data = {}
    for node in list(fromstring(sMsg.decode('utf-8'))):
        decrypt_data[node.tag] = node.text
    # 解析后得到的decrypt_data: {"ToUserName":"企业号", "FromUserName":"发送者用户名", "CreateTime":"发送时间", "Content":"用户发送的内容", "MsgId":"唯一id，需要针对此id做出响应", "AagentID": "应用id"}
    # 用户应根据Content的内容自定义要做出的行为，包括响应返回数据，如下例子，如果发送的是123，就返回hello world

    # get response from openai
    response = respond(decrypt_data['Content'])
    reply_broadcast1 = decrypt_data['FromUserName'] + ' said: ' + decrypt_data['Content']
    reply_broadcast2 = 'Medo said: ' + response
    bot.send_text(content=reply_broadcast1)
    bot.send_text(content=reply_broadcast2)

    sRespData = """<xml>
   <ToUserName>{to_username}</ToUserName>
   <FromUserName>{from_username}</FromUserName> 
   <CreateTime>{create_time}</CreateTime>
   <MsgType>text</MsgType>
   <Content>{content}</Content>
</xml>
""".format(to_username=decrypt_data['ToUserName'],
           from_username=decrypt_data['FromUserName'],
           create_time=decrypt_data['CreateTime'],
           content=response)
    ret, send_msg = wxcpt.EncryptMsg(sReplyMsg=sRespData, sNonce=nonce)
    if ret == 0:
        return Response(content=send_msg)
    else:
        print(send_msg)

def respond(message):
    """Forward OpenAI messages."""
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="Q:" + message + "\nA:",
        temperature=1,
        max_tokens=200,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["Q: ", "A: "]
    )
    # clean the response
    caption = response.choices[0].text.strip()
    return caption

if __name__ == "__main__":
    uvicorn.run("wecom_main:app", port=args.port, host='0.0.0.0', reload=False)
