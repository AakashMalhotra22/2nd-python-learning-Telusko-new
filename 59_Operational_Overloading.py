class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)

        return s3
    def __gt__(self, other):
        m1 =self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1 > m2:
            return True
        else:
            return False
    def __str__(self):
        return'{} {}'.format(self.m1, self.m2)


s1 = student(23, 34)
s2 = student(32, 37)

student1 = s1 + s2 # This add sign means that Student.__add__(s1,s2)

print(student1.m1)




if s1>s2:
    print("s1 is good")
else:
    print("s1 is not good")

print(s1) # it will give the address of s1 not the value, as it is a string.

'''To print the value, we have to define this inside the class'''