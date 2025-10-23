import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print(' What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input() #I fixed this bug by turning string into integer here. "int(input())"
if int(answer) == number1 + number2: #Book suggests fixing here. "int(answer)"
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))