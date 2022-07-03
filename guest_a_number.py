from calendar import c
import random

def guess():
    y = int(input('Enter the rang you want to guess the number : '))
    random_number = random.randint(1, y)
    guess = 0
    times = 1
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {y} : '))
        if guess < random_number:
            times = times + 1
            print(f'Sorry, guess again. Too Low.')
        elif guess > random_number:
            times = times + 1
            print(f'Sorry, Guess again. Too High')
    print(f'Congratulations you guess the number using {times} times.The number = {random_number} ')

def com_guess():
    high = int(input(' what range are you think the guess the number '))
    low = 1
    times =2
    number = 0
    mind_number = ''
    while mind_number != 'c' :
        number = int(random.randint(low, high))
        mind_number = input(f'Is {number} Correct (C) , too low (L) or too high (H) ?   ').lower()
        if mind_number == 'l':
            low = number + 1
            times = times + 1
        elif mind_number == 'h':
            high = number - 1
            times = times + 1
        elif mind_number == 'c':
            print(f'Congratulations computer guess the number using {times} times.Your number = {number} ')

print('********** Guess the Number Game **********')
print('Guess the computer number (1) , Computer guess your number (2)')
x = int(input('Enter game number? '))
if x == 1:
    guess()
elif x == 2:
    com_guess()
