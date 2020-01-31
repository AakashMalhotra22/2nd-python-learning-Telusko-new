#Method Overloading: When you have two  method with same name inside a class but have different arguments.
'''
Example:
class student:
  def aver(self,a,b):
    print((a+b)/2)
  def aver(self,a,b,c):
    print((a+b+c)/3)



But in python, this method overloading is not possible as you cannot create two methods with same name.


'''

# Method Overriding: When you have two method with same name and same parameters but need not to be in same class, can be inherited.
#In this we create two class with same method name and same parameters and inheritant them.

# Method Overloading:

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def add(self,a=None,b=None, c=None):

        s = 0

        if a!=None and b!=None and c!=None:
            s = (a+b+c)

        elif a!=None and b!=None:
            s = (a+b)

        else:
            s = a
        return s



s1 = student(23, 34)
print(s1.add(2))

#2. Method Overriding: Very important topic, heavily used in industry.


class A:

    def show(self):
        print("In A show")

class B(A):

    def show(self):
        print("In B show")

a1 =B()
a1.show()