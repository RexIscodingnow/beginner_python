"""
MixerBox Player URL: https://www.mbplayer.com/

selenium webdriver of MixerBox clicker

Operate Previous, Next, Play/Pause Button
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


CMD_MSG = "cmd (1 ~ 4): 1. 前一首  2. 暫停  3. 下一首  4. exit\n:"


# 設置 Chrome Driver 的檔案路徑
# chrome_options = Options()
# chrome_options.chrome_executable_path = "C:/Users/User/OneDrive/文件/python/學習範例/selenium/chromedriver.exe"
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()


url = "https://www.mbplayer.com/list/182229363"
driver.get(url)
driver.maximize_window()

time.sleep(3)

# class name: Row MuiBox-root css-183miec  css-1wglmvy e1eiglht2
firstSong_element = driver.find_element(By.CLASS_NAME, "exwa4n00")
firstSong_element.click()

while True:
    cmd = input(CMD_MSG)

    if cmd == "1":
        # class name: MuiBox-root css-qorinj
        element = driver.find_element(By.CLASS_NAME, "css-qorinj")
        element.click()

    if cmd == "2":
        # class name: MuiBox-root css-1mw6l2m
        element = driver.find_element(By.CLASS_NAME, "css-1mw6l2m")
        element.click()

    if cmd == "3":
        # class name: MuiBox-root css-1n4h12s
        element = driver.find_element(By.CLASS_NAME, "css-1n4h12s")
        element.click()

    elif cmd == "4":
        print("stop")
        break

    elif cmd.lower() == "cls":
        os.system("cls")



driver.close()