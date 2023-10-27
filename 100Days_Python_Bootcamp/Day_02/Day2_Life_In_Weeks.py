age = input("What is your current age? ")

your_age = int(age)
age_days = (90 - your_age) * 365
age_weeks = (90 - your_age ) * 52
age_months = (90 - your_age ) * 12

print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")