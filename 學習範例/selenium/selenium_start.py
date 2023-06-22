'''
Selenium 瀏覽器自動化操作

網頁截圖
'''

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import chromedriver_autoinstaller   # 自動偵測 chrome 版本，並自動安裝 chromedriver


# chromedriver_autoinstaller.install()

# 設置 Chrome Driver 的檔案路徑
# chrome_options = Options()
# chrome_options.chrome_executable_path = "C:/Users/User/OneDrive/文件/python/學習範例/selenium/chromedriver.exe"


# 建立 Driver 物件實體，用程式操作瀏覽器
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

# 打開網頁
# driver.get("https://twitter.com/TorinoAqua/status/1463055944745586692?s=20")
driver.get("https://google.com")

# 視窗最大化
# driver.maximize_window()

# sleep(5)
# 網頁截圖
driver.save_screenshot("foo.png")



# 關閉網頁
driver.close()





