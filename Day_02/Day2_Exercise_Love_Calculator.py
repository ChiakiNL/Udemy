print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

t_name1 = int(lower_case_name1.count("t"))
t_name2 = int(lower_case_name2.count("t"))

r_name1 = int(lower_case_name1.count("r"))
r_name2 = int(lower_case_name2.count("r"))

u_name1 = int(lower_case_name1.count("u"))
u_name2 = int(lower_case_name2.count("u"))

e_name1 = int(lower_case_name1.count("e"))
e_name2 = int(lower_case_name2.count("e"))

true_number = t_name1 + t_name2 + r_name1 + r_name2 + u_name1 +  u_name2 + e_name1 + e_name2
ten_times_true_number = 10 * true_number

l_name1 = int(lower_case_name1.count("l"))
l_name2 = int(lower_case_name2.count("l"))

o_name1 = int(lower_case_name1.count("o"))
o_name2 = int(lower_case_name2.count("o"))

v_name1 = int(lower_case_name1.count("v"))
v_name2 = int(lower_case_name2.count("v"))

e_name1 = int(lower_case_name1.count("e"))
e_name2 = int(lower_case_name2.count("e"))

love_number = l_name1 + l_name2 + o_name1 + o_name2 + v_name1 +  v_name2 + e_name1 + e_name2

result = ten_times_true_number + love_number

if result <= 10 or result >= 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result <= 50 and result >= 40:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")