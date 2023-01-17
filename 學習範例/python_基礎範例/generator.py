'''
建立 生成器

keyword: yield

一般的函式: 呼叫函式，執行內部程式碼

生成器函式: 由於內部有 yield 關鍵字，內部的程式碼部會被執行
'''

def generator():
    '''
        建立生成器
    '''
    # print("階段 1")
    yield 5
    # print("階段 2")
    yield 3


# 呼叫函式，回傳生成器 (生成器物件)
gen = generator()

# 用 for loop 取得生成器 之 疊代資料
for data in gen:
    '''
    從函式執行到 第 1 個 yield
        把 yield 的值，給 for loop 的 variable: data
    
    取值後，從第 1 個 yield，接著繼續執行到下一個 yield
        再把 yield 的值，給 variable: data

    以此類推，到沒有東西為止
    '''
    # print(data)
    pass


def generate_Even():
    number = 2
    while number < 21:
        yield number
        number += 2
    # yield number


for data in generate_Even():
    print(data)


