# def test(arg):
#     # 呼叫回呼函式
#     arg("hello")

# 回呼函式
# def handle(data):
#     print(data)

# test(handle)

def add(n1, n2, cb):
    '''
    cb(n1 + n2)  ==>  handle1((n1 + n2))
    '''
    cb(n1 + n2)

def handle1(result):
    print("結果是: ", result)

# add(3, 4, handle1)

def run(n1, n2, char, cb):
    if char == '+':
        result = n1 + n2
    elif char == '-':
        result = n1 - n2
    elif char == '*':
        result = n1 * n2
    elif char == '/':
        result = n1 / n2
    elif char == '%':
        result = n1 % n2
    elif char == '^':
        result = n1 ** n2

    cb(result)

def print_result(result):
    print("計算結果: ", result)


while True:
    print("+, -, *, /, %(取餘數), ^(次方)\n輸入算式:")
    n1 = int(input())
    char = input()
    n2 = int(input())

    # n1, char, n2 = map(str, input().split())
    
    try:
            
        if char == '0':
            continuer = input("是否繼續計算[Y/N]: ")
            if continuer == 'Y' or continuer == 'y':
                continue
            elif continuer == 'N' or continuer == 'n':
                break
    
        run(n1, n2, char, print_result)
    
    except Exception:
        continue

