# 亂數產生器 random
# import random
# data = random.sample([54,1551,15,54,1],3)
# print(data)
#  方塊代號題目產生器
import random

# data = [["F","F'","B","B'","R","R'","L","L'","U","U'","D","D'"],
#         ["Fw","Fw'","Bw","Bw'","Rw","Rw'","Lw","Lw'","Uw","Uw'","Dw","Dw'"]]
data1 = [" F "," F2 "," F' "," B "," B2 "," B' "," R "," R2 "," R' "," L "," L2 "," L' "," U "," U2 "," U' "," D "," D2 "," D' "]
data2 = [" Fw "," Fw2 "," Fw' "," Bw "," Bw2 "," Bw' "," Rw "," Rw2 ","Rw' "," Lw "," Lw2 "," Lw' "," Uw "," Uw2 "," Uw' "," Dw "," Dw2 "," Dw' "]

sc_quantity = int(input("3x3輸入0 ; 4x4輸入7以上 =>"))

def SC(quantity):
    if quantity == 0:
        threelayer = random.sample(data1 + data1, 10)
        print(threelayer)
    elif quantity >= 7:
        fourlayer = random.sample(data1 + data2, quantity + 7)
        print(fourlayer)
    else:
        print("wrong input")

SC(sc_quantity)