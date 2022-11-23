'''
    python 的 class 之 操作
'''
class Calculate:
    '''
    class 的結構，不外乎 3 種組成
    
    1. 成員變數
    2. 方法 (method) 、 又名 函式 (function)
    3. 建構子 (Constructor)  => Java, C#... 是與 class 同名
            但 Python 是以 __init__(self) 呈現
        *註 : self 好比像 Java, C#, JS... 的 this.成員變數 的用法
    '''
    # def __init__(self, number1, number2):
    #     self.number1 = number1
    #     self.number2 = number2
    
    # def sum(self):
    #     return self.number1 + self.number2

    # def minus(self):
    #     return self.number1 - self.number2

    # def multply(self):
    #     return self.number1 * self.number2

    # def division(self):
    #     return self.number1 / self.number2

    def sum(number1, number2):
        return number1 + number2

    def minus(number1, number2):
        return number1 - number2

    def multply(number1, number2):
        return number1 * number2

    def division(number1, number2):
        return number1 / number2

'''
    使用 class

    class 名稱 . 底下的成員變數 or 方法 (函式)
    
    如下表示:
            className.method()
            className.memberVariable
'''
# try:
#     num1 = float(input("Enter First Integer: "))
#     num2 = float(input("Enter Second Integer: "))

#     print("sum => ", Calculate(num1, num2).sum())
#     print("minus => ", Calculate(num1, num2).minus())
#     print("multply => ", Calculate(num1, num2).multply())
#     print("division => ", Calculate(num1, num2).division())

# except:
#     print("輸入錯誤")

'''
    class 的繼承 與 使用

    class Name(被繼承的 class):
        ..........
        ..........
'''
class Phone(Calculate):
    def __init__(self, is_waterProof, os, price):
        self.is_waterProof = is_waterProof
        self.os = os
        self.price = price

    def water_proof(self):
        if self.is_waterProof == True:
            return True
        else:
            return False

    def is_ios(self):
        if self.os == "ios":
            return True
        
        else:
            return False

    def compare_price(self):
        if self.price > 7000:
            return True
        
        else:
            return False

# phone1 = Phone(True, "android", 8000)
# phone2 = Phone(False, "ios", 2000)

# phone1.compare_price()
# phone2.compare_price()



