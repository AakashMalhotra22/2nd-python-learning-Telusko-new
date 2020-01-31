#Break: means it will take out from a loop, when a certain condition occurs

available  = 4
x = int(input("How many candies do you want? "))

i =1
while i<=x:

    if i >= available:
        print("Out of stock")
        break

    print("Candy")
    i +=1

print("Get out")

#2. continue: It skip the statements, it does not close the loop.

# Ist way by use of continue.[Calculation of numbers from 0 to 10 which are not divisible by 3 and 5]
print("              ")

for i in range (1,11):

    if i%5 == 0 or i%3 == 0:
        continue
    print(i)

# 2nd way own style
print("              ")

for i in range (1,11):

    if i%5 != 0 and i%3 != 0:
        print(i)

# 3 pass: means this is not valid, pass it to else without giving any output in if.
print("              ")
for i in range(1,10):
    if i%2!= 0:
        pass
    else:
        print(i)
