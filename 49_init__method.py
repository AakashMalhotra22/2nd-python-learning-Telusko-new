#Special method - __init__

class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def confi(self):
        print("confi is" , self.cpu ,self.ram)

com1 = computer("i5", 16)
com2 = computer("i7", 100)
com1.confi()
com2.confi()

print("                  ")
print(com1.ram)
print(com2.ram)