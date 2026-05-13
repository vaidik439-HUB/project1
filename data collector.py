print("Welcome to the Intreactive personal data collector !\n")

name=input("Please enter your name:")
age=int(input("Please enter your age:"))
height=float(input("Please enter your height in meters:"))
fav_number=int(input("Please enter your favorite number:"))

print("\nThank you ! Here is the information we collected:")

print(f"\nName:{name},(Type:{type(name)},Memory Address:{id(name)})")
print(f"Age:{age},(Type:{type(age)},Memory Address:{id(age)})")
print(f"Height:{height},(Type:{type(height)},Memory Address:{id(height)})")
print(f"Favorite number:{fav_number},(Type:{type(fav_number)},Memory Address:{id(fav_number)})\n")

import datetime
current_year=datetime.date.today().year
birth_year=current_year- age
print(f"Your birth year is approximately:{birth_year} (based on your age {age})\n")

print("Thank you for using the personal data collector.Good bye!")