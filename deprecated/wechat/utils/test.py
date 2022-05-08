import requests

apiUrl = 'http://api.yanxi520.cn/api/bucket.php'
data = {
    'msg': '草泥马'
}
r = requests.get(apiUrl, params=data).content.decode('utf-8')
print(r)
