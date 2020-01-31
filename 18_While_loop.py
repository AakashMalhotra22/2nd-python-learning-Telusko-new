# Three imoortant things in while loop
'''
1. Intialization or variable
2. condition
3. Increment or decrement

'''


i = 1
while i<=5:
   print("aakash", i)
   i+=1

for i in range(10):
    print(i, end="")

#Nested while loops
print("                                                      ")
i = 1
j = 1
while i <=5:
    print('aakash')

    while j<=5:
        print("don")
        j+=1
    i += 1

#You can write the condition of first while loop in case of nested while loops in the end.
#2
print("                                                      ")
i = 1
j = 1
while i <=5:
    print(' aakash', end ="")

    while j<=5:
        print(" don", end = "")
        j+=1
    i += 1


#3
print("                                                      ")
i = 1
j = 1
while i <=5:
    print(' aakash', end ="")
    i+=1
    while j<=5:
        print(" don", end = "")
        j+=1
    print("")

#4
print("                                                      ")
i = 1

while i <=5:
    print(' aakash', end ="")
    i+=1
    j = 1
    while j<=5:
        print(" don", end = "")
        j+=1
    print("")
