# Exercise 1

"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old."""

# Extras
"""Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)"""

# userInput
user_name_input = input("What is your name? ")
user_age_input = int(input("How old are you? "))
current_year = int(input("what year are you in? "))

# when will turn 100 years old
turn_year = 100

# calculating the year
the_year = (current_year - user_age_input) + turn_year

print(f"hey {user_name_input} you will turn {turn_year} years when you reach the year {the_year}".format(user_name_input,turn_year,the_year))
