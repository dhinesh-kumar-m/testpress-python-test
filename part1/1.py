#1
from datetime import date
name = input("Enter the Name :")
age = input("Enter the Age :")

current_year = date.today().year

required_age = 100 - int(age)

years = current_year + required_age

print(f"Hi, {name} you will turn 100 years in {years}")
