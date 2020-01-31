#Iterators are used to fetch one value at a time, or to fetch values one at a time.

l = [1,2,3,4]

it = iter(l) # or you can also use y = l.__iter__()

print(it.__next__())
print(next(it))
for i in l:
    print(i)

print("                    ")

print("                    ")
'''When you are creating your own iterator class, you need to two methods, first is iterator method and next method'''
class topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    def __next__(self):


        if self.num <= 10:
               value = self.num
               self.num+=1
               return value
        else:
            raise StopIteration

t1 = topten()

print(t1.__next__())


print(t1.__next__())

for i in t1:
    print(i)

