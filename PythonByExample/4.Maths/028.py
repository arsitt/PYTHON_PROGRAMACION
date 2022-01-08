# Update program 027 so that it will display the answer to
# two decimal places.

number = float(input("Enter a decimal number with many of them: "))
total = number*2
dec2 = round(total, 2)
print(dec2)