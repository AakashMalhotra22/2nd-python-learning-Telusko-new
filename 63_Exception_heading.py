#Errors
'''
Types of Error:
1. Compile Error
2. Logical Error
3. Run time

'''

'''1.Compile time Error: When you do syntax mistakes. These are called syntactical Errors'''
# Easy to find


'''2.Logical Error: When you don't get correct output, for example you give 2+2, and you get 3. This is logical errors'''
# Easy to find

'''3. Run time Error: When you dont getting output instead your output gets compiled and also no logical errors, ex: divide by zero.'''
# These types of errors are done by users as you are getting input from users.
# These are difficult to find.

# So what is required, even if you are getting an error, then also you should not get any error, to do so we use try except.


# Example1

a = 2
b=0
try:
    print(a/b)
except Exception:
    print("Hey, you cannot divide a number by zero.")

print("bye")

# When you also want to find the error.

a = 3
b =0

try:
    print(a/b)
except Exception as e:
    print("Hey, you cannot divide a number by zero.", e)

print("bye")

# New term finally.
print("   ")

a =3
b =1
try:
    print("resource open.")
    print(a/b)
except Exception as e:
    print("Hey you cannot divide a number by zero,",e)

finally:
    print("resource closed.")


# When you use many programs.
print("            ")
print("            ")

a =3
b =0
try:
    print("resource open.")
    print(a/b)


except ZeroDivisionError as e:
    print("Hey you cannot divide a number by zero,",e)

try:
    k = int(input("Enter a number: "))
    print(k)


except ValueError as e:
    print("Invalid input,", e)
except Exception:
    print("Something went wrong...")

finally:
    print("resource closed.")


