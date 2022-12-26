'''
Python web crawler (俗稱: 網路爬蟲)

解析 HTML 原始碼，使用 Beautiful Soup 模組


**注意 : 盡量模仿一般使用者，進行抓取資料
'''

from urllib import request as req

# url = "https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2Fryvr_ly8f"
url = "https://www.ptt.cc/bbs/Gossiping/index.html"


# 建立一個 Request 物件，附加到 Request Headers 的資訊
# request = req.Request(url, headers={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# })
request = req.Request(url, headers={
    "cookie": "over18=1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
})


with req.urlopen(request) as responce:
    data = responce.read().decode("utf-8")

# print(data)


# 解析原始碼
import bs4


# 解析 HTML 格式文件
root = bs4.BeautifulSoup(data, "html.parser")

# print(root.title)   # 抓取網頁的 <title></title> 內容


# 參數: find_all( HTML_標籤, class_=" class_屬性名稱 " )
# 用途: 找到所有指定的 HTML 標籤之內容
titles = root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)


nextLink = root.find("a", string="‹ 上頁")





