'''
Python 與 arduino 連線

使用模組 => serial

讀取 => readline()  # 讀取一行

傳送 => write()  # 參數型別為 Bytes (位元組)
'''
import serial
from time import sleep


COM_PORT = 'COM9'   # arduino 的連接埠
BAUT_RATES = 2000000     # arduino 傳輸鮑率

ser_data = serial.Serial(COM_PORT, BAUT_RATES)


try:
    while True:
        while ser_data.in_waiting:   # 若接收到資料

            choice = input("停止按 0\n間隔 0.5 秒印出 10 筆資料，按 1\n間隔 1 秒印出 20 筆資料，按 2\n>>> ")

            if choice == '0':
                print('結束執行!')
                break

            elif choice == '1':
                for i in range(10):
                    data_raw = ser_data.readline()  # 讀取一行
                    data_decode = data_raw.decode()
                    print('原始資料 => ', data_raw)   # 資料型別: Bytes
                    print('編碼後資料 => ', data_decode)
                    sleep(0.5)

            elif choice == '2':
                for i in range(20):
                    data_raw = ser_data.readline()  # 讀取一行
                    data_decode = data_raw.decode()
                    print('原始資料 => ', data_raw)
                    print('編碼後資料 => ', data_decode)
                    sleep(1)

            else:
                print('輸入錯誤')


except KeyboardInterrupt:
    ser_data.close()
    print('結束執行!')







