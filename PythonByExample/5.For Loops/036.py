# Alter program 035 so that it will ask the user to enter their
# name and a number and then display their name that
# number of times.

name = input("Enter your name: ")
times = int(input("Enter the amount of times you want to repeat your name: "))

for i in range(0,times):
    print(name)