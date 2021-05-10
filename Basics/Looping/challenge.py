import random as nature
number = nature.randint(1, 5)
count = 0
while count >= 0:
    user = int (input('Guess a a number between 1 and 5 :'))
    count += 1
    if number == user:
        break

print(f'You guessed it in {count} tries!')