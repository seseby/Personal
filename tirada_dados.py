# Tirada de dados

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2 

user_guess = 0

while user_guess != total:
    print(f'What is the total (2-12)? ')
    user_guess = int(input('Enter your guess: '))

print('You got it')

