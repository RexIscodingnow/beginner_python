'''
module => speedtest

測量網速
'''

import speedtest


print("準備中...")

test = speedtest.Speedtest()

# 取得可用於測試的 伺服器列表
server_list = test.get_servers()
# 篩選最佳伺服器
server = test.get_best_server()

print(f"伺服器列表 => \n{server_list}")
print("\n")
print(f"測試用伺服器 => {server}")

print("正在測試...\n")

download_speed = int(test.download() / (1024 ** 2))
upload_speed = int(test.upload() / (1024 ** 2))


print(f"下載速度 => {download_speed} Mbits")
print(f"上傳速度 => {upload_speed} Mbits")

