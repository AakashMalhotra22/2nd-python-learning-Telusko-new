def div(a,b):
    print(a/b)

def smart(func):

    def inner(a,b):
             if a<b:
                 a,b = b,a
             return func(a,b)
    return inner

y = smart(div)

y(2,3)
