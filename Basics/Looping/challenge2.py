import random as nature
number = nature.randint(1, 10)
count = 0
while count >= 0:
    print('Guess a a number between 1 and 10 :')
    count += 1
    user = input(f'Enter guess #{count}: ')
    if not user.isnumeric():
        print('Numbers only, please!')
    else:
        user = int(user)
        if number == user:
            break
        elif number > user:
            print('Your guess is too low, try again!')
        elif number < user:
            print('Your guess is too high, try again!')


print(f'You guessed it in {count} tries!')
