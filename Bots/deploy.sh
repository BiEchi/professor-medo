# conda install pip
# conda create --name py38 python==3.8.0
# conda activate py38
# pip install -r requirements.txt

# install node on CentOS
# wget http://nodejs.org/dist/v16.10.0/node-v16.10.0-linux-x64.tar.gz
# sudo tar --strip-components 1 -xzvf node-v* -C /usr/local
# npm -i ./slack/

# kill all running processes using Python3
ps aux|grep python|awk '{print $2}'|xargs kill -9
# kill all running processes using node
ps aux|grep node|awk '{print $2}'|xargs kill -9

nohup python3 ./telegram/telegram_main.py &
nohup python3 ./discord/discord_main.py &
nohup python3 wecom/wecom_main.py \
    --port=12000 \
    --token="tRGPCQmQvNJCwzf" \
    --aeskey="lQXxszVAmlrxmK1GZMix6jeqRFtgJ2GINnvwzxwalJU" \
    --corpid="ww40b242172d1e2a3f" \
    &
nohup node slack/index.js &
