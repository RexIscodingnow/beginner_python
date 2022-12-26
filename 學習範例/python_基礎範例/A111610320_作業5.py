class DoSomething:
    def __init__(self, num1=9, num2=9, quantity=72):
        self.num1 = num1
        self.num2 = num2
        self.quantity = quantity

    def multiply99(self):
        for i in range(1, self.num1+1):
            for j in range(1, self.num2+1):
                if j % 9 == 0:
                    print(f"{i} x {j} =", i * j, end='  ')
                    print("\n")
                else:
                    print(f"{i} x {j} =", i * j, end='  ')
        
        print("Done")
        print('\n')

    
    def printStar(self):
        for i in range(self.quantity):
            if i % 10 == 0:
                print("@", end='')
                print('\n')
            print("@", end='')
        
        print('\n')
        print("Done")
        print('\n')


doSomething = DoSomething()
doSomething.printStar()
doSomething.multiply99()

