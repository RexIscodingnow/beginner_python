"""
title: Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
    * I can be placed before V (5) and X (10) to make 4 and 9. 
    * X can be placed before L (50) and C (100) to make 40 and 90. 
    * C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
    Input: num = 3
    Output: "III"
    Explanation: 3 is represented as 3 ones.

Example 2:
    Input: num = 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.

Example 3:
    Input: num = 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        目標: 正整數 轉 羅馬數字
        """


        """
        另外測試: 代碼重構
        將最初解法重新調整架構與易讀性
        
        數值容許範圍: 0 ~ 9999  (0 不輸出羅馬數字，則為 empty string)
        """
        result = ""
        temp = ""
        multiply = 1    # x * 10 ^ n = 位數 * 倍數，以 10 倍數為單位

        # integer : roman number
        roman_number = {
            1: "I", 4: "IV", 5: "V", 9: "IX",
            10: "X", 40: "XL", 50: "L", 90: "XC",
            100: "C", 400: "CD", 500: "D", 900: "CM",
            1000: "M"
        }

        # 從個位數 ~ 高位數，取每一"位數" 做處理
        while num != 0:
            digit = (num % 10) * multiply

            if digit < 4 * multiply or digit >= 1000:
                if digit != 1 * multiply:
                    key = digit - ((num % 10) - 1) * multiply
                else:
                    key = digit
                
                n = num % 10

            elif digit == 4 * multiply or digit == 5 * multiply or digit == 9 * multiply:
                key = digit
                n = 1

            elif digit > 5 * multiply and digit < 9 * multiply:
                # 介於 5 * (10^n)  <  n  <  9 * (10^n)   之間
                # 
                # 該區間的羅馬數字的組成，可分為 2 個部分
                # 
                #       e.g 1 :   8 =   5  +    3  =>  "V" + "III"
                #       e.g 2 : 700 = 500  +  200  =>  "D" + "CC"
                temp = roman_number.get(5 * multiply)

                key = 1 * multiply
                n = (digit - 5 * multiply) // multiply

            for _ in range(n):
                result = roman_number.get(key) + result

            result = temp + result
            temp = ""

            multiply *= 10
            num //= 10


        return result


        """
        最初解法
        """
        # roman_num = {
        #     "I": 1, "IV": 4, "V": 5, "IX": 9,
        #     "X": 10, "XL":40, "L": 50, "XC": 90,
        #     "C": 100, "CD": 400, "D": 500, "CM": 900,
        #     "M": 1000
        # }

        # numLs = []
        # while num != 0:
        #     # 頭尾反轉，個位數作前
        #     numLs.append(num % 10)
        #     num //= 10
        
        # romanNum_str = ""   # 羅馬數字結果值
        # multiple = 1    # 倍數 (上升一位 x10 倍)
        # for num_digit in numLs:
        #     # 實際數值 = 寫入 List 的數 x 倍數
        #     digit = num_digit * multiple
        #     if digit == 4 * multiple or digit == 5 * multiple or digit == 9 * multiple:
        #         # 反過來寫入 ex: 9 => IX     當下寫入的 => XI
        #         romanNum_str += reverseStr(get_key(roman_num, digit))
            
        #     elif digit > 5 * multiple and digit < 9 * multiple:
        #         # 反過來寫入 ex: 8 => VIII   當下寫入的 => IIIV
        #         for i in range(int((digit / multiple) - 5)):
        #             romanNum_str += get_key(roman_num, 1 * multiple)
        #         romanNum_str += get_key(roman_num, 5 * multiple)
            
        #     elif digit < 4 * multiple or digit >= 1000:
        #         for i in range(int(digit / multiple)):
        #             romanNum_str += get_key(roman_num, 1 * multiple)

        #     multiple *= 10    # 位數算完，上升一位 x10
        
        # # 個位數作前，最大位數作尾端，把 頭尾倒反過來
        # romanNum_str = reverseStr(romanNum_str)
        # return romanNum_str

def get_key(dict, val):
    # 值 (value) 取 鍵 (key)
    for key, value in dict.items():
        if val == value:
            return key
    else:
        return

def reverseStr(s):
    # 字串反轉
    strLs  = []
    for i in range(len(s)-1, -1, -1):
        strLs.append(s[i])
    
    string = ""
    for char in strLs:
        string += char

    return string


solution = Solution()

num = 3
result = solution.intToRoman(num)
print(result)

num = 58
result = solution.intToRoman(num)
print(result)

num = 1994
result = solution.intToRoman(num)
print(result)




class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        '''
        另一種 (The 暴力美學)
            暴力拆解法
            每一個位數，依序由小到大，由左至右，排入 陣列 (or list)
        '''
        m = ["", "M", "MM", "MMM"]   # 1000 ~ 3000
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]    # 100 ~ 900
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]    # 10  ~ 90
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]    # 1   ~ 9
        
        print(num // 10)
        roman_number = m[num // 1000] + c[(num // 100) % 10] + x[(num // 10) % 10] + i[num % 10]

        return roman_number


# solution = Solution()

# num = int(input("=> "))
# result = solution.intToRoman(num)
# print(result)