# There are two types of variables,
#1. Local variable: These are present inside the function.
#2. Global variable: Which are present outside the function.

a = 10 # This is Global Variable.
print("Outside",a)

def something():
    a = 5 # This is local variable
    b = 6# This is local variable.
    print("Inside", a,b)

'''Scope: This is limit, for example, the scope of the a =5 inside the function is only up to function only, while the variable: a=10
can be used anywhere.
'''

something()

# Some points.
'''1. You can use global variable inside the function, if local variable is absent.'''
print("  ")
c = 5
def some():
    print("Inside",c)

some()

print("outside", c)

'''2.But if there is a local variable, inside the function, then the local variable will be given preference.'''
print(" ")
c = 5
def some():
    c =10
    print("Inside",c)

some()

print("outside", c)

'''3.To make a local variable, you need to write it explicitly'''
print(" ")

d =100
def same():
    global d
    d = 14
    print("Inside", d)

same()
print("outside",d)


'''
Globals: To use both local and global variables, inside the python.
We use the concept of globals.
'''
print(" ")
print("  ")
p = 10
print(id(p))
def samething():
    p = 9
    x = globals()['p']# if you will not use the square brackets, then it will give all the global variables.
    print(id(x))
    print("inside", p)
    globals()['p'] = 12
    print(globals()['p'])

samething()

print("outside", p)
#Thus we have a local variable p and global variable p inside the same function.