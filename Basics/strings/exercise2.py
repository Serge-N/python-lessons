user = input('Would you like to continue? ')
if(user=='no' or user =='No' or user == 'NO' or user=='n'):
    print('Exiting')
elif (user=='yes' or user =='Yes' or user == 'YES' or user=='y'):
    print('Continuing...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no') 