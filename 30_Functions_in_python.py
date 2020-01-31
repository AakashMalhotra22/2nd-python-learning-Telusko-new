# : is used to write multiple statements.
def greet(): # greet is function name, round bracket is used to tell that the greet is not a variable, it is a function.
    print("hello")
    print("Good Morning")

greet()

def sum(num1, num2): # num1, num2 are two arguments of the function.
    print(num1+num2)

sum(1,2)

sum(3,15)

# Return Statement
def sum(num1, num2):
    return num1+num2

result = sum(3,4)
print(result)

# To return two values
def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(10,2)
print(result1, result2)
