# 載入內建的 sys 模組並取的資訊
import sys
print(sys.platform)
print(sys.maxsize)
print(sys.path) # 印出模組的搜尋路徑
import sys as s
print(s.platform) 

# 建立 geometry 模組，載入使用
# import geometry
# result = geometry.distance(1,1,5,5)
# print(result)
# result = geometry.slope(1,2,5,6)
# print(result)

# 調整模組搜尋的路徑
# import sys
# sys.path.append("modules") # 增加 modules 資料夾的"搜尋路徑"
# print(sys.path) # 印出模組的路徑
# print("--------------------------")
# import geometry
# print(geometry.distance(1,1,5,5))

# 練習：自訂範圍的亂數產生器
# import sys
# sys.path.append("modules")
# import numRandom
# n2 = int(input("輸入1: "))
# print(numRandom.number(n2))