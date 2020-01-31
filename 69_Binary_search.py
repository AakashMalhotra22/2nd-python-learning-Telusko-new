
n = int(input("Enter any number: "))
x = ""
def search(n, list):
   l =0
   u = len(list) -1
   while l<= u:
           mid = (l+u)//2

           if list[mid] == n:
               globals()['x'] = mid

               return True
           else:
               if mid<n:
                   l = mid+1


               else:
                   u = mid-1

list = [1,2,3,4,5,6]

if search(n, list):
    print("found at ", x+1)

else:
    print("Not found")



