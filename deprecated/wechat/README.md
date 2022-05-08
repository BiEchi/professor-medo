# MaidRobot (on CentOS-6)

## Project Architecture

 We use [`ItChat`](assets/dependencies/ItChat) as the front-end communication tool, [`Chatterbot AI`](assets/dependencies/ChatterBot) as the background machine learning tool, and [`SQLite`](assets/chatbot_learn/) as the background database for storing data. 

When the client (`ItChat`) receives a message, it will judge whether it is image or text. If it’s text, it will transfer that to `Chatterbot AI` for learning, and get the inference back to the WeChat Web version. If it’s image, it will save the image and run [`EasyOCR`](https://github.com/JaidedAI/EasyOCR) locally to recognize the texts inside the image, and then push the image to [Doutula](https://www.doutula.com) RESTful API and download the returned file locally. It will then send this file to `ItChat` and further the WeChat Web version.

![Architecture](http://jacklovespictures.oss-cn-beijing.aliyuncs.com/2021-10-15-085854.png)

### Front-end

| Time      | Version          | Source |
| --------- | ---------------- | ------ |
| 2021/7/14 | ItChat, Bug-free |        |
| 2021/6/10 | ItChat, official |        |

### Back-End

| Time       | Version                          | Source                                       |
| ---------- | -------------------------------- | -------------------------------------------- |
| 2021/11/25 | Intelligent AI ChatBot in Python | https://www.youtube.com/watch?v=1lwddP0KUEg  |
| 2021/7/9   | ChatterBot.py                    | https://chatterbot.readthedocs.io/en/stable/ |
| 2021/6/10  | Turing Chatbot API               | https://tuling123.com                        |



## Next Task

-   (Lyon) Run the whole architecture on the server. The origin server has been shut down, so you need to set up on another server. I’d like to suggest that we use the server bought by yourself for Hepta Workshop, as listed below.
-   (Lyon) Run the whole architecture on your local machine and make a tutorial for the whole process to set up.
-   (Together) Realize the Chatterbot learning part.

## Server Information

```shell
Liyang. Hepta-Server, BB-CWL
IP Public. 101.34.39.209
IP Private. 10.0.4.16
Password. F-A-K-E-D
ssh root@101.34.39.209

MySQL Access
Host. 101.34.39.209
Username. root
Password. bbcwl6666
```

## Set Up The Environment

`install.sh`

```bash
#!/bin/bash
# Your working dir is MaidRobot

# Prerequisites
sudo yum install -y python-pip
pip3 install pyqrcode
pip3 install requests

# install itchat library (if you don't have it)
git clone git@github.com:luvletter2333/ItChat.git ./Installation/ItChat
pip3 install ./Installation/Itchat

# install ChatterBot library
pip3 install pytz -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install chatterbot==1.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple

# install OCR library
pip3 install easyocr -i https://pypi.tuna.tsinghua.edu.cn/simple
# or using a local copy
git clone git@github.com:JaidedAI/EasyOCR.git ./Installation/EasyOCR
pip3 install ./Installation/EasyOCR #CentOS error: memory not big enough

# clone your project git
cd /home/dell
git clone git@github.com:BiEchi/WechatRobot.git

# run the main Python script
cd WechatRobot
python3 main.py
```



## Change the `yum` source of CentOS to Ali Cloud

方法：

1、进入到/etc/yum.repos.d/目录下，备份之前的CentOS-Base.repo地址。

`cd /etc/yum.repos.d/`

`mv CentOS-Base.repo CentOS-Base.repo.bak`

2、下载阿里云yum源

centos6：``wget -O CentOS-Base.repo [http://mirrors.aliyun.com/repo/Centos-6.repo](http://mirrors.aliyun.com/repo/Centos-6.repo?spm=a2c6h.12873639.0.0.40541327CEReRp&file=Centos-6.repo)``

centot5：``wget -O CentOS-Base.repo [http://mirrors.aliyun.com/repo/Centos-5.repo](http://mirrors.aliyuncs.com/repo/Centos-6.repo)``

## Github Setup

`git_install.sh`

```shell
#!/bin/bash

sudo yum install -y git
git config --global user.name biechi
git config --global user.email Haob.19@intl.zju.edu.cn
git config --global user.password "Baihao20010226"
```



