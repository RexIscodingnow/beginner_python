'''
Python web crawler (俗稱: 網路爬蟲)
'''

from urllib import request as req

url = "https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2Fryvr_ly8f"

# 建立一個 Request 物件，附加到 Request Header 的資訊
request = req.Request(url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

with req.urlopen(request) as responce:
    data = responce.read().decode("utf-8")

print(data)

# 解析原始碼




