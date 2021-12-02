# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third.

number1 = int(input('First Number: '))
number2 = int(input('Second Number: '))
number3 = int(input('Third Number: '))

answer = (number1 + number2) * number3

print('The total is ', answer)