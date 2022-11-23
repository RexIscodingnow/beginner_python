# 初學 Python
# print("hello world!")




# 羅馬數字轉換器

def ramanToInt(string):
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num = 0
    temp = 0

    for i in string:
        if roman_num[i] > temp:
            num += roman_num[i] - (temp * 2)
        else:
            num += roman_num[i]
        
        temp = roman_num[i]

    return num

ans = ramanToInt(input("num => "))
print(ans)

    
