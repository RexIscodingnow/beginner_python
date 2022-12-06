# 初學 Python
# print("hello world!")








# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     if not strs: return ""

#     result = ""
#     temp = ""
#     compare_temp = ""   # 比較 暫存值
#     result = strs[0]    # 取第一個值
#     for i in range(len(strs)):
#         temp = strs[i]
#         min_len = min(result, temp)
#         for j in range(len(min_len)):
#             if temp[j] == result[j]:
#                 compare_temp += temp[j]
#             elif temp[0] != result[0]:
#                 return ""
#             else:
#                 break

#         result = compare_temp
#         compare_temp = ""
    
#     return result


# strs = ["flower","flow","flight"]    # Target Answer is 相同字元 => fl
# result_1 = longestCommonPrefix(strs)

# print(result_1)

# strs = ["cir","car"]
# result_2 = longestCommonPrefix(strs)
# print(result_2)

