# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

user = int(input('Enter a decimal value: '))
binstr = bin(user)

def f1():
    user
    print('Your binary number is:', binstr[2::])
    print('Number of bits equal to one:', binstr.count('1'))

f1()
