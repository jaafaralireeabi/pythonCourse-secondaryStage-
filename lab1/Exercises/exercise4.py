"""

    Write a program in python that converts from miles to kilometers. 
    Your program shoul d have a reasonable prompt for the user to enter 
    a number of miles. Hint: There are 1.60 9 kilometers to the mile
    
"""

#solve

miles = input("enter the number of miles: \n")
kilometers = float(miles) * 1.609
print(miles, "miles is equal to", kilometers, "kilometers")