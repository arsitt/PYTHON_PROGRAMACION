# Ask the user to type in the first
# line of a nursery rhyme and
# display the length of the string.
# Ask for a starting number and an
# ending number and then display
# just that section of the text
# (remember Python starts
# counting from 0 and not 1).

phrase = input("Enter a the start of a nursery rhyme: ")
length = len(phrase)
print("This has",length,"letters.")
startin = int(input("Enter the number where it should start printing:"))
finish = int(input("Enter the number where it should finish: "))
print(phrase[startin:finish])
