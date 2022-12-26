# 計算機 *練習*
num1 = float(input("輸入數字1: "))
num2 = float(input("輸入數字2: "))
op = input("運算符號 +,-,x,/,**平方,*1/2根號x1: ")
continuer = input("繼續(t)/不用(f): ")

if op == "+":
    ans = num1 + num2
elif op == "-":
    ans = num1 - num2
elif op == "x":
    ans = num1 * num2
elif op == "/":
    ans = num1 / num2

if continuer == "t":
    if op == "+" or op == "-" or op == "x" or op == "/":
        print(ans)
        num3 = float(input("輸入數字3: "))
        op2 = input("運算符號 +,-,x,/,**平方,*1/2根號x1: ")
        if op2 == "+":
            ans2 = ans + num3
        elif op2 == "-":
            ans2 = ans - num3
        elif op2 == "x":
            ans2 = ans * num3
        elif op2 == "/":
            ans2 = ans / num3
        print(ans2)

elif continuer == "f":
    print(ans)        