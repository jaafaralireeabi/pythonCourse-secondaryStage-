x = int(input("enter x: "))
y = int(input("enter y: "))

print('Number\tsquare')
print('--------------')
for number in range(x, y+1):
       square = number**2
       print(number, '\t', square)
