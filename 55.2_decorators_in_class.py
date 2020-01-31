class smalldivisor:
    def div(self,a,b):
        return a/b

    def smart(self,func):
            def change(a,b):
               if a<b:
                   a,b = b,a
               return func(a,b)
            return change


com1 = smalldivisor()

y=com1.smart(com1.div)
x = y(2,3)
print(x)