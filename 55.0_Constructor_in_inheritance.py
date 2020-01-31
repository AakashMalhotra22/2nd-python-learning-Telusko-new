class A:

    def __init__(self): # Constructor
        print("in A init")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")

class B(A):
    def feature3(self):
        print("feature3 is working.")
    def feature4(self):
        print("feature4 is working.")

a1 = B() # It is calling the constructor of A.
'''Since, we dont have any constructor in B, that's why it is calling constructor of A otherwise, it will not call, as shown in next
example.'''


class A:

    def __init__(self): # Constructor
        print("in A init")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")

class B(A):
    def __init__(self): # Constructor
        print("in B init")
    def feature3(self):
        print("feature3 is working.")
    def feature4(self):
        print("feature4 is working.")

a1 = B() # It is calling the constructor of A.
print("  ")
# IF you want to call the constructor of A inspite of having constructor in B. then use super.


class A:

    def __init__(self): # Constructor
        print("in A init")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")

class B(A):
    def __init__(self): # Constructor
        super().__init__()
        print("in B init")
    def feature3(self):
        print("feature3 is working.")
    def feature4(self):
        print("feature4 is working.")

a1 = B() # It is calling the constructor of A.


# When you call super then it will first call constructor of Super class first then call init of sub class.

print("    ")
#Other example

class A:
    def __init__(self):  # Constructor
        print("in A init")
    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")


class B():
    def __init__(self):  # Constructor
        print("in B init")
    def feature3(self):
        print("feature3 is working.")

    def feature4(self):
        print("feature4 is working.")


class C(A, B):
    def __init__(self):
        super().__init__()# It will call the constructor of A in accordance with method of method resolution order.
        print("in C init")
    def feature5(self):
        print("feature 5 working")
a1 = C()

'''MRO first finds the constructor of itself, then prefer order'''

# This MRO also follows for methods/ functions, if two class have same function then it will prefer order which is coming first.

