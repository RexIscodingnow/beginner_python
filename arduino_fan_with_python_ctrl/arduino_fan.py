'''
    Python 與 Arduino
    
    風扇控制
'''

import os
import serial
import msvcrt
from time import sleep


def fan_control(choice: str):
    '''
    Arduino 風扇控制
    param choice: 輸入字串，風扇的控制選項
    '''
    str_len = len(choice)
    choice = choice[0]
    cmd_item = ""
    command = {
        "ON": b'1\n',   # 開電源 (馬達用)
        "OFF": b'0\n',    # 關電源 (一樣馬達用)
        "SPEED_UP": b'H\n',    # 加轉速
        "SPEED_LOW": b'L\n',    # 減轉速
        "RIGHT": b'l\n',    # 往右擺頭
        "LEFT": b'r\n',    # 往左擺頭
        "SPEED_STOP_CHANGE": b'N\n',    # 轉速不動
        "STOP_MOVE": b's\n'  # 不擺頭 (手動調整)
    }
    if choice == 'O' or choice == 'o':
        cmd_item = "ON"
        print('開啟風扇\n')
    elif choice == 'F' or choice == 'f':
        cmd_item = "OFF"
        print('關掉風扇\n')
    elif choice == 'W' or choice == 'w':
        cmd_item = "SPEED_UP"
        print('風量 ++\n')
    elif choice == 'S' or choice == 's':
        cmd_item = "SPEED_LOW"
        print('風量 --\n')
    elif choice == 'D' or choice == 'd':
        cmd_item = "RIGHT"
        print('擺頭: 往右\n')
    elif choice == 'A' or choice == 'a':
        cmd_item = "LEFT"
        print('擺頭: 往左\n')


    if cmd_item:
        for i in range(str_len):
            ser_data.write(command[cmd_item])

def get_FanSpeed(switch: bool):
    if switch:
        if ser_data.in_waiting:
            angle_bytes = ser_data.readline()
            angle = angle_bytes.decode()
            print(angle)

restart_times = 0   # 計算重新連線次數
while True:
    try:
        port_choice = int(input("連接埠 => COM"))   # 輸入 Arduino 連接的 USB 插口
        print("\n")

        global ser_data
        ser_data = None
        COM_PORT = "COM" + str(port_choice)   # 傳輸 COM PORT 以字串做參數
        BAUT_RATES = 2000000    # 在 Arduino 設置 Serial.begin( 傳輸鮑率 );  是多少就設一樣的值
        ser_data = serial.Serial(COM_PORT, BAUT_RATES)   # ( COM PORT, 傳輸鮑率  )
        print("連線中，梢等幾秒...\n")
        sleep(2)

        try:
            running = True
            restart_times = 0
            while running:
                msg = "開啟，按 [O]\n關閉，按 [F]\n" + \
                    "加大風量，按 [W]\n減少風量，按 [S]\n" + \
                    "往右邊擺頭，按 [D]\n往左邊擺頭，按 [A]\n" + \
                    "結束執行程式，按 [E] 或 [Ctrl + C]\n" + \
                    "清理視窗 [cls], [CLS]\n" + \
                    ">>> "
                choice = input(msg)
                if choice:
                    fan_control(choice)

                # 結束執行
                if 'E' in choice or 'e' in choice:
                    ser_data.write(b'0\n')
                    ser_data.close()    # 關閉該連接埠連接
                    print("結束操作!\n\n按任意鍵結束")
                    ord(msvcrt.getch())
                    running = False
                
                # 清理視窗
                if 'cls' in choice or 'CLS' in choice:
                    os.system("cls")
            
            if running == False:
                break

        except KeyboardInterrupt:
            '''
            把 KeyboardInterrupt 當作 Ctrl + C 使用，結束程式執行
            '''
            ser_data.write(b'0\n')
            ser_data.close()    # 關閉該連接埠連接
            print("結束操作!\n\n按任意鍵結束")
            ord(msvcrt.getch())
            break

    except Exception:
        restart_times += 1
        if restart_times >= 3:
            print("重新連接次數 3 次 (或超過)，是否終止操作 [Y/N]")
            option = input(">>> ")
            if option == 'Y' or option == 'y':
                break
            elif option == 'N' or option == 'n':
                restart_times = 0
                print("繼續嘗試~~\n")
                if ser_data:
                    ser_data.close()   # 關閉該連接埠連接

        print("連接失敗，連接埠可能使用中，或無法使用")