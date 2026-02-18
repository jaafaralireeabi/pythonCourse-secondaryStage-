test1 = int(input('Enter the score for test 1: ' ))
test2 = int(input('Enter the score for test 2: ' ))
test3 = int(input('Enter the score for test 3: ' ))
# Calculate the average test score.
average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is', average)
HIGH_SCORE = 90
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')
