def sort(l):
    for i in range(len(l)-1):
        minvalue = i
        for j in range(i, len(l)):
            if l[j]<l[minvalue]:
                minvalue = j

        temp = l[i]
        l[i] = l[minvalue]
        l[minvalue]= temp




list = [6,5,114,3,2,1]

sort(list)

print(list)

L1 =[0,1,1]
L2 = [1,0,1]

