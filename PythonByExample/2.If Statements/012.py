#Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.

number1 = int(input('First number: '))
number2 = int(input('Second number: '))

if number1 > number2:
    print(number2, number1)
else:
    print(number1, number2)