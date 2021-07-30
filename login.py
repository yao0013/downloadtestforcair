import requests

def logincair():
    urls = "https://cair.cambricon.com/sharecloud-boot/sys/login"
    json = {"username": "admin", "password": "Hello123!@#", "remember_me": "false", "checkKey": 1627454606165}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9', 'Content-Type': 'application/json;charset=UTF-8'
    }
    re = requests.post(url=urls, json=json, headers=headers)
    return re.text