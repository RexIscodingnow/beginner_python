'''
python web crawler  =>  cookie 操作
'''

from urllib import request as req

# url = "https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2Fryvr_ly8f"
url = "https://myself-blog.deta.dev/gentleman"

# 建立一個 Request 物件，附加到 Request Headers 的資訊
# request = req.Request(url, headers={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# })
request = req.Request(url, headers={
    "cookie": "session",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
})


with req.urlopen(request) as responce:
    data = responce.read().decode("utf-8")

# print(data)


# 解析原始碼
import bs4

root = bs4.BeautifulSoup(data, "html.parser")

print(root.title)   # 抓取網頁的 <title></title> 內容

# for i in range(1, 4):
#     text = root.find("p", class_=f"talk-trash-{i}")
#     print(text)