# Generators are used to get iterators without use of a iter and next function,
def topten():

    yield 1 # here yield is used to create iterator.
    yield 2
    yield 3
    yield 4

values = topten()

print(values.__next__())
print(values.__next__())

for i in values:

    print(i)


# Perfect squares
print("                   ")




def SQUARE():

    n =1
    while n<=10:
        sq = n*n
        yield sq
        n += 1

val = SQUARE()

print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))

for i in val:
    print(i)


# Creating Generators by use of list Comprehension:

y = (x*x for x in [1,2,3,4])
print(y) # This will print generator object and its address.
print(next(y)) # this will print the next values
print(next(y))

for i in y:
    print(i)

'''If you want your output in the form of list then'''
y = (x*x for x in [1,2,3,4])
print(list(y))

