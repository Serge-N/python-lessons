first_value  = input ('First Number: ')
second_value = input ('second Number: ') 

if second_value.isnumeric() == False or first_value.isnumeric() == False:
    print ('Value is not a number.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum '+ str(sum))

