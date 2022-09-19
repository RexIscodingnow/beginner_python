# def test(arg):
#     # 呼叫回呼函式
#     arg("hello")

# # 回呼函式
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

continuer = []
while True:
    print("+, -, *, /, %(取餘數), ^(次方)\n輸入算式:")
    n1 = int(input())
    char = input()
    n2 = int(input())

    if continuer == 'n' or continuer == 'N':
        break

    if char == '0':
        continuer = input("是否繼續計算[Y/N]: ")

    run(n1, n2, char, print_result)

