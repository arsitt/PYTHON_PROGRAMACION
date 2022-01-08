# Ask the user to enter their first name. If the length
# of their first name is under five characters, ask
# them to enter their surname and join them
# together (without a space) and display the name
# in upper case. If the length of the first name is five
# or more characters, display their first name in
# lower case.

firstn = input("Enter your name please: ")
if len(firstn) < 5:
    surn = input("Please enter your surname, name too short: ")
    combo = firstn + surn
    print(combo.upper())
else:
    print(firstn.lower())