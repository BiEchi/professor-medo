ps aux|grep python|awk '{print $2}'|xargs kill -9
nohup python3 ./main.py &
nohup python3 ./discord_main.py &
