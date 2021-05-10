fahrenheit = input ('What is the temperature in fahrenheit? ')

if fahrenheit.isnumeric():
    fahrenheit = int (fahrenheit)
    celsius = int((fahrenheit - 32) * 5/9)
    print(f'Temperature in celsius is {celsius}')
else :
    print('Input is not a number.')
