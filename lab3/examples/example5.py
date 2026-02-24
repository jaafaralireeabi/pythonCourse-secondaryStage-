start = int(input('Enter the starting number: '))
end = int(input('Enter n'))
# Print the table headings
print()
print('Number\tSquare')
print('--------------')
for number in range(start, end + 1):
      square = number**2
      print(number, '\t', square)
