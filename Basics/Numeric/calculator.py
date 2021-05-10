print ('Simple Calculator!')
first_number = input ('First number ?')
operation = input ('Operation ?')
second_number = input ('Second number ?')

if not first_number.isnumeric() or not second_number.isnumeric():
    print('One of the inputs is not a number.')

operation = operation.strip()

if operation == '+' :
    first_number = int(first_number)
    second_number = int (second_number)
    print(f'Sum of {first_number} + {second_number} = {first_number+second_number}')
elif operation =='-':
     first_number = int(first_number)
     second_number = int (second_number)
     print(f'Difference of {first_number} - {second_number} = {first_number-second_number}')
elif operation =='*':
     first_number = int(first_number)
     second_number = int (second_number)
     print(f'Product of {first_number} * {second_number} = {first_number*second_number}')
elif operation =='/':
     first_number = int(first_number)
     second_number = int (second_number)
     print(f'Dividend of {first_number} / {second_number} = {first_number/second_number}')
elif operation =='**':
     first_number = int(first_number)
     second_number = int (second_number)
     print(f'{first_number} power {second_number} = {first_number**second_number}')
elif operation =='%':
     first_number = int(first_number)
     second_number = int (second_number)
     print(f'Modulus of {first_number} % {second_number} = {first_number%second_number}')
elif operation:
    print('Operation not recognized.')