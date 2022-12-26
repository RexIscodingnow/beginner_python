'''
    python 的 class 之 操作
'''
class Calculate:
    '''
    第一種 class

    class 的結構，不外乎 3 種組成
    
    1. 成員變數
    2. 方法 (method) 、 又名 函式 (function)
    3. 建構子 (Constructor)  => Java, C#... 是與 class 同名
            但 Python 是以 __init__(self) 呈現
        *註 : self 好比像 Java, C#, JS... 的 this.成員變數 的用法
    '''
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def sum(self):
        return self.number1 + self.number2

    def minus(self):
        return self.number1 - self.number2

    def multply(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 / self.number2


    '''
    第 2 種寫法，無建構子 (__init__ 函式)
    '''
    # def sum(number1, number2):
    #     return number1 + number2

    # def minus(number1, number2):
    #     return number1 - number2

    # def multply(number1, number2):
    #     return number1 * number2

    # def division(number1, number2):
    #     return number1 / number2

'''
    使用 class

    class 名稱 . 底下的成員變數 or 方法 (函式)
    
    如下表示:
            className.method()
            className.memberVariable
'''
# while True:
#     try:
#         num1 = float(input("Enter First Integer: "))
#         num2 = float(input("Enter Second Integer: "))

#         print("sum => ", Calculate(num1, num2).sum())
#         print("minus => ", Calculate(num1, num2).minus())
#         print("multply => ", Calculate(num1, num2).multply())
#         print("division => ", Calculate(num1, num2).division())
#         break

#     except:
#         print("輸入錯誤")

'''
    class 的繼承 與 使用

    class Name(被繼承的 class):
        ..........
        ..........
'''
class Products(Calculate):
    def __init__(self, price: int, product: str, year: int, month: int):
        self.price = price
        self.product = product
        
        self.year = year
        self.month = month
        self.products = {
            "smartphone": {
                "median_price": 5000,
                "year": self.year,
                "month": self.month,
            },
            "novel": {
                "median_price": 150,
                "year": self.year,
                "month": self.month,
            },
            "clothes": {
                "median_price": 200,
                "year": self.year,
                "month": self.month,
            }
        }

    def product_info(self, infomation):
        for product_info in self.products.keys:
            if self.product in product_info:
                target_info = self.products[self.product]
                
                if infomation is int:
                    if target_info["median_price"] < infomation:
                        return "貴~"
                    elif target_info["median_price"] > infomation:
                        return "便宜~~"
                    else:
                        return "emmm..."

                return target_info[infomation]

            else:
                return


product1 = Products(5500, "smartphone", 2020, 12)
product2 = Products(12000, "smartphone", 2022, 3)

price1 = product1.product_info(product1.price)
print(price1)

