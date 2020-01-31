class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")

class B(A):# Here we inheritane all the feature of A in B
    def feature3(self):
        print("feature3 is working.")
    def feature4(self):
        print("feature4 is woryuking.")

a1 = A()
b1 = B()

b1.feature1()
'''Here A is superclass/ Parent class of B or B is the sub class or child class of A'''

# There are two types of inheritance.
'''
1. Single level inheritance.:Above example was of this one.
2. Multi level inheritance.
'''

class C(A):
    def feature5(self):
        print("feature 5 working")

c1 = C()
c1.feature1()

