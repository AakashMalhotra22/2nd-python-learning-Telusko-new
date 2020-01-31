#Function can be described by some other ways also.

def square(a):
    return a*a
result = square(5)
print(result)

# This method can only be used when you have only one expression.

f = lambda a : a*a
result = f(5)

print(result)

g = lambda a,b : a+b # You can pass any number of arguments, bu the  expression should be one.
result = g(1,3)
print(result)


aakash = lambda a,b,c,d: a+b-c*d

result = aakash(100,2,34,2)
print(result)

