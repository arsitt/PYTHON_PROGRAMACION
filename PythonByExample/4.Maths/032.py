# Ask for the radius and the depth of a cylinder
# and work out the total volume (circle
# area*depth) rounded to three decimal
# places.
import math

radius = float(input("Enter the radius of your circle: "))
depth = float(input("Enter the depth of your circle: "))
area = (radius ** 2) * math.pi
volume = area * depth
print(round(volume,3))
