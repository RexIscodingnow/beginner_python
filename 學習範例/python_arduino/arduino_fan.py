'''
    Python 與 Arduino
    
    風扇控制
'''

import serial
from time import sleep

port_choice = int(input("連接埠 => COM"))
print("\n")

COM_PORT = "COM" + str(port_choice)
BAUT_RATES = 2000000

ser_data = serial.Serial(COM_PORT, BAUT_RATES)

msg = "開啟，按 [O]\n關閉，按 [C]\n" + \
    "加大風量，按 [H]\n減少風量，按 [L]\n往右邊擺頭，按 [R]\n往左邊擺頭，按 [E]\n結束執行程式，按 [S] 或 [Ctrl + C]\n>>> "

print("連線中，梢等幾秒...\n")
try:
    sleep(1)
    while True:
        choice = input(msg)
        if choice == 'O' or choice == 'o':
            print('開啟風扇\n')
            ser_data.write(b'1\n')
        elif choice == 'C' or choice == 'c':
            print('關掉風扇\n')
            ser_data.write(b'0\n')

        elif choice == 'H' or choice == 'h':
            print('風量 ++\n')
            ser_data.write(b'H\n')
        elif choice == 'L' or choice == 'l':
            print('風量 --\n')
            ser_data.write(b'L\n')

        elif choice == 'R' or choice == 'r':
            print('擺頭: 往右\n')
            ser_data.write(b'l\n')
        elif choice == 'E' or choice == 'e':
            print('擺頭: 往左\n')
            ser_data.write(b'r\n')
        

        elif choice == 'S' or choice == 's':
            ser_data.write(b'0\n')
            ser_data.close()
            print("結束操作!")
            break

        else:
            print("\n")
            ser_data.write(b'N\n')
            ser_data.write(b's\n')

except KeyboardInterrupt:
    ser_data.write(b'0\n')
    ser_data.close()
    print("結束操作!")
