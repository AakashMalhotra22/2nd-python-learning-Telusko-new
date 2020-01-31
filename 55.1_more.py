# super feature can also be used to call methods not only the constructor.

class B():
    def __init__(self):  # Constructor
        print("in B init")
    def feature3(self):
        print("feature3 is working.")

    def feature4(self):
        print("feature4 is working.")


class C(B):
    def __init__(self):
        super().__init__()# It will call the constructor of A in accordance with method of method resolution order.
        print("in C init")
    def feat(self):
        super().feature3()

print(" ")

a1 = C
a1.feat()
