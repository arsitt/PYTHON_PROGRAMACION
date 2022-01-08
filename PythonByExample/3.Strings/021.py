# Ask the user to enter their first name and then ask them to
# enter their surname. Join them together with a space between
# and display the name and the length of whole name.

usern = input('Enter your first name: ')
users = input('Enter your surname: ')

user = (f'{usern} {users} ')
userlen = len(user)

print(user + str(userlen))
