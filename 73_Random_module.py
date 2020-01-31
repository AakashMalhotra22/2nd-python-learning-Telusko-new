import random

y = random.random()
print(y)

# To get values in certain range

y = random.uniform(1,10)

print(y)

# To get random integers

y = random.randint(1,6)

print(y)

# When you want random values from list

greet = ["hello", "hi", "hey", "hei"]

y = random.choice(greet)

print(y + " aakash! ")


# When you want more than 1 random outcomes from the list.

colors = ["red", "black", "Green"]

y = random.choices(colors, k = 10)

print(y)

# When you give the probabilities to the elements of the list

colors = ["red", "black", "Green"]

y = random.choices(colors, weights = [18,18,2], k = 10)

print(y)


# shuffle

deck = list(range(1,53))
random.shuffle(deck) # It will shuffle the list.
print(deck)


# Sample method

deck = list(range(1,53))
hand = random.sample(deck, k=5) # sample gives the unique values, it never gives the same values.
print(hand)



print("  ")
print("  ")
#
