# Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user-friendly format.

#We will ask the amount of slices the user had bought, then we will ask how many of them have been eaten by himself and we will identify how many are left
pizza_start = int(input('How many slices have u bought: '))
pizza_eat = int(input('How many pizza slices have you eaten: '))
pizza_left = (pizza_start - pizza_eat)

print('You have', pizza_left, 'slices left.')