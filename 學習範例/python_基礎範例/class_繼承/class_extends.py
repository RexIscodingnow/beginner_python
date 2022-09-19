import numpy as array

class Calculator():
    def add(number1, number2):
        return number1 + number2

    def minus(number1, number2):
        return number1 - number2

    def multiply(number1, number2):
        return number1 * number2

    def division(number1, number2):
        return number1 / number2

    def pow(number1, number2):
        return number1 ** number2

    def sqrt(number):
        return number ** 0.5

    def average(*numbers):
        data = 0
        for num in numbers:
            data += num
        result = data / len(numbers)
        return result

# algebra (n.) 代數
class Algebra(Calculator):
    def __init__(self, *algebra):
        '''
        parameter
        : algebra => 代數至多 100 個       
        '''
        self.algebra = array.array(list(algebra))
        self.algebra = algebra
    
    def calculate_1D(self):
        '''
        一元方程式計算
        2x + 3x = 10
        '''
        pass

mode = array.array([
    '"mode_1" : 普通計算機',
    '"mode_2" : 代數計算機'
])

data = array.zeros([3])

