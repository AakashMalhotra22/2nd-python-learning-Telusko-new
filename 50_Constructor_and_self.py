#Heap memory:
'''It is a memory where you will get all the objects.'''

class computer:# You can not make a class empty, if you want to do so, use pass.
    pass

c1 = computer()
print(id(c1)) # 7077520

c2 = computer() # 7937904
print(id(c2))

#Since, both the objects c1 and c2 are having different id, which means both the objects takes different spaces in hipe memory.
#Size of an object depends on number of variables and size of each variables.
'''
Constructor allocates this memory.
in c2 = computer(), computer() is your constructor.

'''



print("           ")

class computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 24
    def update(self):
        self.age = 12

c1 = computer()
c2 = computer()
c1.name = "rashi"
print(c1.name)
print (c2.name)

c1.update()
'''This is the use of self, you have not told update, which object c1 or c2 should be used to execute commands, but what self will do
it will take c1 to execute commands because you have written c1.update'''

print(c1.age)
print(c2.age)
# Example to show the importance of self.

print("     ")

class computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 24
    def update(self):
        self.age = 12
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = computer()
c2 = computer()


if c1.compare(c2): # Here c1 becomes self, and c2 takes place of other.
    print("They are of same age.")
else:
    print("They are of different age.")
