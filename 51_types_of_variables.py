'''
There are two types of variables.
1. Instance
2. Class(Static)

'''
'''
1. Instance variable: Which is defined inside a init/ it can be changed.

2. Class variable: Which is defined inside a class/ it is static.
'''
class Car:
    wheels = 4 # This is class variable
    def __init__(self):
        self. mil = 10 # These are instance variable
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8 # Here mil is instance variable.


print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

'''if you want to change the wheel variable n, then it can be changed for all the functions inside the class car, but instance variable
 cannot be changed for all the function inside the class, then also if you want to change it, you have to write the code for each 
 function.'''
print("  ")
Car.wheels = 5
#Car.mil = 10 will not work
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
