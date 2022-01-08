# Change program
# 037 to also ask for a
# number. Display
# their name (one
# letter at a time on
# each line) and
# repeat this for the
# number of times
# they entered.

name = input("Enter your name: ")
times = int(input("Enter the amount of times you want to have a letter: "))

for x in range(0,times):
    for i in name:
        print(i)