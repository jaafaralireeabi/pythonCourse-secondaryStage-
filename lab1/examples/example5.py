# Constant (conversion factor) 
CM_PER_METER = 100 

# Read value in meters from user 
value_in_meters = float(input("Enter value in meters:"))

# Convert to centimeters 
value_in_cm = value_in_meters * CM_PER_METER 

# Display result 
print("Value in centimeters:", value_in_cm)