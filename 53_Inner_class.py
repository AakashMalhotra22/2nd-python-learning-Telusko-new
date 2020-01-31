
class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self. laptop() # This is the object of the inner class.

    def show(self):
        print(self.name, self.rollno)
    class laptop():

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8"


s1 = student("Aakash", 12)
s2 = student("Ram", 23)

print(s1.name, s1.rollno)

s1.show()

print(s1.lap.brand)
print("   ")

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))
# Since, lap1 and lap2 are having different ids, thus they are different.

print("  ")
'''You can also create the object of the inner class outside the outer class as,'''
class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)
    class laptop():

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8"
        def show(self):
            print(self.brand, self.cpu, self.ram)




lap5 = student.laptop()
print(lap5.brand)
(lap5.show())


