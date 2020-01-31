'''
1. Filter
'''

nums = [3,2,6,8,4,6,2,9]

#Filter is used to filter a particular sequence and gives the certain number of values, as demanded.

#It takes two parameters, one is function and second is lst or the sequence.

# Way-1
def is_even(n):
    return n%2==0

evens = list(filter(is_even, nums))

print(evens)

print(" ")
# Way-2

is_evens = lambda n: n%2 == 0

evens = list(filter(is_even, nums))

print(evens)

# Way -3
evens = list(filter(lambda n: n%2 ==0, nums))
print(evens)


''' 
2. Map
'''
print(" ")
# It is used to change the values of the list, by applying the demanded operation.

doubles = list(map(lambda n: n*2, nums))
print(doubles)

'''
3. Reduce: You need to import reduce.
'''

from functools import reduce
print("")
print(nums)

sum = reduce(lambda a,b : a+b, nums)

print(sum)