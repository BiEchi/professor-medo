# Professor Medo
This is the public repo for Medo, a BERT-based chatbot framework for Telegram bots with your own training dataset.



## Installation

```python
# for centos: init server
sudo yum update
sudo dnf install python3
python3 -V
sudo wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
sudo bash Anaconda3-2020.11-Linux-x86_64.sh
sudo -s source /root/anaconda3/bin/activate
export PATH="/root/anaconda3/bin:$PATH"
# for general: init dev env
conda create -n medo-chatbot python=3
conda activate medo-chatbot
pip3 install python-telegram-bot --upgrade
python3 -m pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user pandas
python3 -m pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user openai
python3 -m pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user discord.py
cd Bots/discord
python3 main.py
```

Start your adventure!
