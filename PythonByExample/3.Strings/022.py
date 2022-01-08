# Ask the user to enter their first name and surname in lower
# case. Change the case to title case and join them together.
# Display the finished result.

name_lower = input('Enter your name in lowercase: ')
surn_lower = input('Enter your surname in lowercase: ')

name_title = name_lower.title()
surn_title = surn_lower.title()

result = (name_title + ' ' + surn_title)
print(result)