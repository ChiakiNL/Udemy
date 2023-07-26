height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
cover = 5

import math 
number_of_cans = (height * width) / cover

rounded_cans = math.ceil(number_of_cans)

print(f"You'll need {rounded_cans} cans of paint.")