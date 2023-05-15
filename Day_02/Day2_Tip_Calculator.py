print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
ppl = int(input("How many people to split the bill? "))

tip_percent = tip / 100
tip_1 = bill * tip_percent
bill_and_tip = bill + tip_1

result_per_person = bill_and_tip / ppl

result = round(result_per_person, 2)
result = "{:.2f}".format(result_per_person)

print(f'{"Each person should pay: $"}{result}')