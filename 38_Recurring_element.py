
p = "BAB"
l = 0
k = "$"
for i in p:
   if k != "$":
       break
   l += 1
   for n in p[l:]:

        if i==n:
            print("The recurring elment is", i)

            k = i
            break





