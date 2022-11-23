from urllib import request

src = "https://www.ntu.edu.tw/"   # 就用 臺大官網 試試

gov_src = "https://data.kcg.gov.tw/dataset/6a02fa74-2f2d-41b4-a88c-7c8230a2bf1d/resource/2b0eacad-5f40-48f1-a310-1ee00f841845/download/20200710-38.csv"

with request.urlopen(src) as responce:
    # 取得(前端)網站原始碼 (HTML, CSS, JS)
    data = responce.read().decode("utf-8")   # decode(utf-8)  =>  文字編碼 轉 utf-8

print(data)




