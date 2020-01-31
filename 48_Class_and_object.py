
#Class are used to create objects.
#Class consists of the attributes - variables, and behaviour- methods(Function)

class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

a = "8" # Here a is object of type/class string
b = 7 # here b is object of type/class int
print(type(a))

com1 = Computer()# This means com1 is a variable of tye/class computer which belongs to module main(means class and object).
print(type(com1))


#
print("                  ")

class Computer:
    def config(self): # here self is the object that you are passing.
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)
print("  ")
com1.config() #These are used normally
com2.config()
