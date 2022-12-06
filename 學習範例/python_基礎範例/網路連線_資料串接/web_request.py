from urllib import request

# src = "https://www.ntu.edu.tw/"   # 就用 臺大官網 試試


# with request.urlopen(src) as responce:
#     # 取得(前端)網站原始碼 (HTML, CSS, JS)
#     data = responce.read().decode("utf-8")   # decode(utf-8)  =>  文字編碼 轉 utf-8 (支援中文)

# print(data)


'''
    取得資料 以 API 的方式存取
'''

import json    # 處理 json 資料格式

src = "https://www.cdc.gov.tw/TravelEpidemic/ExportJSON"    # 以 Python 解讀是 [{}, {}, ...]

# 開啟網址
with request.urlopen(src) as response:
    data = json.load(response)

# print(data)

# 取得 目標資料

for i in range(len(data)):
    result = data[i]['headline']
    
    print(result)


