def update(x):
    x = 8
    print("x",x)

a = 10
update(a)
print("a",a)
print(id(a))

#There are 2 things,
'''pass by value: In this we pass the value, not the address, As in above example, we have a = 10 and we have passed a =10 in it and get
 x=8, thus in above case, we have used a =10 two times, first to use it in a function and second to use it separately.'''


'''pass by reference:In this you pass the address, mean'''

#In python, none is present.



print("                           ")
def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x",x)

a = 10
print(id(a))
update(a)
print("a",a)

