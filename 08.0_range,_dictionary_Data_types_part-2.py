#4.

range(0, 10)

r = list(range(12))
print(r)

r = list(range(2,10, 3))
print(r)

n = range(0,10)
print(type(n))

#5. Dictionary:

r = {"navin":"Iphone", "aakash": "samsung"}

print(r.keys())
print(r.values())

print(r["navin"])
print(r.get("navin"))


print(r.get("dda", "not a valid key"))