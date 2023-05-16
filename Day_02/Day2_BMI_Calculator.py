height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)
new_weight = float(weight)

result = new_weight / (new_height * new_height)

new_result = int(result)

print(new_result)