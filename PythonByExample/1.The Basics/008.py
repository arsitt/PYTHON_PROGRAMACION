# Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

diner_price = float(input('What is the total amount of the diner: '))
diner_people = int(input('How many are you?: '))
diner_split = diner_price / diner_people

print('Each person have to pay', diner_split)