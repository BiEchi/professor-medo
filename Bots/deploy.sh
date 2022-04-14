# conda install pip
# conda create --name py38 python==3.8.0
# conda activate py38
# pip install -r requirements.txt

ps aux|grep python|awk '{print $2}'|xargs kill -9

nohup python3 ./telegram/telegram_main.py &
nohup python3 ./discord/discord_main.py &
nohup python3 wecom/wecom_main.py \
    --port=12000 \
    --token="tRGPCQmQvNJCwzf" \
    --aeskey="lQXxszVAmlrxmK1GZMix6jeqRFtgJ2GINnvwzxwalJU" \
    --corpid="ww40b242172d1e2a3f" \
    &
