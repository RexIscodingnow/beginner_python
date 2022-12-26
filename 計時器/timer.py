import time
from datetime import datetime
import keyboard


def key_event():
    flag = False
    while True:
        read_key = keyboard.read_hotkey()
        if read_key == "space" and flag == True:
            flag = False
            break
        elif read_key == "space" and flag == False:
            print("開始計時")
            flag = True
    loop(flag)

def loop(flag):
    while flag:
        i = 0
        i += 1


start = time.time()
now = datetime.utcnow()
key_event()
end = time.time()

result_time = end - start
print(result_time)


# print(keyboard.read_key())
