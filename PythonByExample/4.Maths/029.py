# Ask the user to enter an integer that is over 500. Work
# out the square root of that number and display it to two
# decimal places.
import math


over500 = int(input("Enter a number over 500: "))
square = math.sqrt(over500)
print(round(square,2))