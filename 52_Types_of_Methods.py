'''
There are three types of Methods
1. Class Method
2. Static Method
3. Instance Method

'''
class student():
    school = "Aakash"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self): # This is instance method/function
        return (self.m1+self.m2+self.m3)/3



s1 = student(1,2,3)# m1, m2 and m3 are instance variable.
s2 = student(4,5,6)

print(s1.average())
print(s2.average())

print("   ")
'''Instance method are of two types:
1. Accessor Methods - for getting the values.
2. Mutators Methods - for setting the values.

'''

print(s1.m1)# This is accessor, as you are getting the valuess.
s1.m1 = 100 # this is mutators, as you are setting the values.
print(s1.m1)

"One more example of accessors and mutators are:"

class student():
    school = "Aakash"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self): # This is instance method/function
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self, value):
             self.m1 = value
print("  ")
s1 = student(1,2,3)
print(s1.get_m1())


'''In above examples, m1, m2,m3 are instance variable, which can be used with instance method'''

# 2. Class method:
print("    ")
class student():
    school = "Aakash" # This is class variable

    @classmethod # This is required decorators before the class method.
    def info(cls):# For class method, use cls instead of self.
        return cls.school

s1 = student()
s2 = student()
#Here you cannot change it from here like as in instance method

#s1.info() = "Ram" # It will not work
print(student.info())

#student.info() = "Aakash" # This will also not work

# 3. Static Method

class student():
    @staticmethod # This is required decorators, before static method.
    def info(): # In this we does not pass anything.
        print("Hello Aakash")

(student.info())

# If you want to do something different in the class, then use static method