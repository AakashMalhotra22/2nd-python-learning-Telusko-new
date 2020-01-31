lst = []

def fib(n):
    a = 0
    b = 1
    if n == 0:
       pass
    elif n < 0:
        print("Invalid Input")
    else:
        for i in range(2, n):
            c = a+b
            a = b
            b =c
            if c < n:
                lst.append(c)
        print(max(lst))
fib(10000)