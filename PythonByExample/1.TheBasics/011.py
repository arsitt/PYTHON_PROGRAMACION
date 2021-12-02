# Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.

number_100 = int(input('Enter a number over 100: '))
number_10 = int(input('Enter a number over 10: '))
times = number_100 // number_10

print('The second number could fit in the larger one by', times, 'times.')