# 初學 Python
# print("hello world!")




class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        position = 0

        for i in range(len(nums)):
            if target == nums[i]:
                position = i
                break
            
            else:
                if target > nums[i]:
                    position = len(nums)
                else:
                    if (i == 0 and target < nums[0]) or (i > 0 and target > nums[i-1] and target < nums[i]):
                        position = i

        return position


solution = Solution()

nums = [2, 5]
nums = [-1, 3, 5, 6]
nums = [1, 3, 5, 6]
target = 2
result = solution.searchInsert(nums, target)
# print(result)




class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        目標: 正整數 轉 羅馬數字
        """
        roman_num = {
            "I": 1, "IV": 4, "V": 5, "IX": 9,
            "X": 10, "XL":40, "L": 50, "XC": 90,
            "C": 100, "CD": 400, "D": 500, "CM": 900,
            "M": 1000
        }

        numLs = []
        while num != 0:
            # 頭尾反轉，個位數作前
            numLs.append(num % 10)
            num //= 10
        
        romanNum_str = ""   # 羅馬數字結果值
        multiple = 1    # 倍數 (上升一位 x10 倍)
        for num_digit in numLs:
            # 實際數值 = 寫入 List 的數 x 倍數
            digit = num_digit * multiple
            if digit == 4 * multiple or digit == 5 * multiple or digit == 9 * multiple:
                # 反過來寫入 ex: 9 => IX     當下寫入的 => XI
                romanNum_str += reverseStr(get_key(roman_num, digit))
            
            elif digit > 5 * multiple and digit < 9 * multiple:
                # 反過來寫入 ex: 8 => VIII   當下寫入的 => IIIV
                for i in range(int((digit / multiple) - 5)):
                    romanNum_str += get_key(roman_num, 1 * multiple)
                romanNum_str += get_key(roman_num, 5 * multiple)
            
            elif digit < 4 * multiple or digit >= 1000:
                for i in range(int(digit / multiple)):
                    romanNum_str += get_key(roman_num, 1 * multiple)

            multiple *= 10    # 位數算完，上升一位 x10
        
        # 個位數作前，最大位數作尾端，把 頭尾倒反過來
        romanNum_str = reverseStr(romanNum_str)
        return romanNum_str

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

# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
        
#         '''
#             暴力拆解法
#             每一個位數，依序由小到大，由左至右，排入 陣列 (or list)
#         '''
#         m = ["", "M", "MM", "MMM"]   # 1000 ~ 3000
#         c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]    # 100 ~ 900
#         x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]    # 10  ~ 90
#         i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]    # 1   ~ 9
        
#         print(num // 10)
#         roman_number = m[num // 1000] + c[(num // 100) % 10] + x[(num // 10) % 10] + i[num % 10]

#         return roman_number


solution = Solution()

# num = int(input("=> "))
# result = solution.intToRoman(num)
# print(result)



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        逐字元比對，找最長 且 不一樣的字元 (字母)，作為一組
        結果值最長的
        '''
        str_length = len(s)

        if str_length == 0:
            return 0
        elif str_length == 1:
            return 1

        i, j = 0, 1
        container_1 = []     # 先放入 (打頭陣)
        container_2 = []     # 篩選結果 儲存器 (類似暫存器效果)
        
        container_1.append(s[0])
        while j < str_length:
            if s[i] != s[j] and s[j] not in container_1:
                container_1.append(s[j])
            else:
                break
            i += 1
            j += 1

        if len(container_1) < str_length:
            i = j
            j += 1
            container_2.append(s[i])
            while j < str_length:
                if s[i] != s[j] and s[j] not in container_2:
                    container_2.append(s[j])
                else:
                    break
                i += 1
                j += 1

            # print("------------------------")
            # print(container_1)
            # print("------------------------")
            # print(container_2)
            # print("------------------------")

            container_1_len = len(container_1)
            container_2_len = len(container_2)
            return max(container_1_len, container_2_len)
        
        return len(container_1)

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int

#         By ChatGPT
#         """
#         window = {}  # Hash map to store the characters in the current window
#         max_length = 0  # Variable to store the maximum length found so far
#         start = 0  # Start of the sliding window
#         for i, c in enumerate(s):
#             # If the current character is already in the window, update the start of the window
#             if c in window:
#                 start = max(start, window[c] + 1)
#             # Update the maximum length and add the current character to the window
#             max_length = max(max_length, i - start + 1)
#             window[c] = i
#         return max_length


# test case
# solution = Solution()
# s = "bbbbbbbbb"
# result = solution.lengthOfLongestSubstring(s)
# print(result)
# s = "abcabcaa"
# result = solution.lengthOfLongestSubstring(s)
# print(result)
# s = "pwwkew"
# result = solution.lengthOfLongestSubstring(s)
# print(result)






