# Display the following message:

# 1)Square
# 2)Triangle

# Enter a number:

# If the user enters 1, then it should ask them for
# the length of one of its sides and display the
# area. If they select 2, it should ask for the base
# and height of the triangle and display the area. If
# they type in anything else, it should give them a
# suitable error message.
import os

print("1)Square")
print("2)Triangle")
select= int(input("\nEnter a number: "))
os.system("cls")

if select == 1:
    print("You selected Square.\n")
    sq_side = int(input("Enter the side of the square: "))
    print("\nThe total area of the square it's",(sq_side**2), "cm².")
elif select == 2:
    print("You selected Triangle.\n")
    tri_base = int(input("Enter the base of the triangle: "))
    tri_hei = int(input("Enter the height of the triangle: "))
    print("\nThe total area of the triangle it's",(tri_base * tri_hei)//2, "cm².")