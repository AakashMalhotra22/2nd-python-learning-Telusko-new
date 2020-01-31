# Dictionary is a unique mapping from keys to values.
'''
Two ways to make the dictionary.
'''


#1.


y = {"phone": "nokia", "cycle": "atlas", "love": "mom"}

'''Operations'''

#1 Print

print(y)

#2 Add value to dictionary

y["childhood"] = "pados"

print(y)

#3 Remove the value and its key.

del y["phone"]

print(y)

#3 check the length

print(len(y))

#4 Check the values in dictionary

ram = {"a":3, "b":4}

#5 print specific keys

print(y["love"])
print(y.get("phone", "not found"))

#6 Print all key and values

for key, val in y.items():
    print(key , "=" ,val)

#7 Get only the keys from dictionary

print(y.keys())
print(y.values())



'''
2. way
'''
# To make a dictionary or call it

#1.
y = dict(a= 8, b =7)
print(y)

#2.

x = dict({"m":8, "n":7} )

print(x)
print("              ")
'''3. Flexiblity of dicitionary and nested dictionaries'''

d = {"k1":123, "k2": [1,2,3], "k3" : dict(a=3, b =4), "k4":{1:"aakash", "r2": "ram"}}
print(d)

print(" ")
print(d["k2"][2])
print(d["k4"]["r2"])
print(d["k4"][1])