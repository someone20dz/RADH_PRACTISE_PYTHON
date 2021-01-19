# Exercise 2
"""Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user."""

# Extras:

"""If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

# First
userNumber = int(input("type is any number: "))

if userNumber % 2 == 0:
    print("Even")
else:
    print("Odd")

# Second
if userNumber % 4 == 0:
    print("is a multiple of 4")
else:
    print("is not a multiple of 4")

# Third
num = int(input("type a number: "))
check = int(input("type a second number: "))

if num % check == 0:
    print("this is Even")
else:
    print("this is Odd")
