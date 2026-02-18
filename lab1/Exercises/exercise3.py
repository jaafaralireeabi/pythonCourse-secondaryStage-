"""
    write program to calculate age from birth date from user input
"""

#solve

print("enter your birth date in format:\n")
brith_year = input("year: ")
brith_month = input("month: ")
brith_day = input("day: ")

age_year = 2026 - int(brith_year) # Current year - brith_year
age_month = 2 - int(brith_month) # Current month - brith_month 
age_day = 8 - int(brith_day) # current day - brith_day

print("your age is: ", age_year, "years", age_month, 
      "months", age_day, "days")