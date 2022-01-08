# Ask the user to enter two numbers.
# Use whole number division to divide
# the first number by the second and
# also work out the remainder and
# display the answer in a user-friendly
# way (e.g. if they enter 7 and 2 display
# “7 divided by 2 is 3 with 1
# remaining”).
import os

f_num = int(input("Enter first number: "))
s_num = int(input("Enter second number: "))

divide = int(f_num/s_num)
rest = int(f_num%s_num)

os.system("cls")

print(f_num, "divided by", s_num, "it's", divide, "\nThe rest is", rest)