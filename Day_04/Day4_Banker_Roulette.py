import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names) - 1
random_number = random.randint(0, length)

print(f"{names[random_number]} is going to buy the meal today!")