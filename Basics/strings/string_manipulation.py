#check if strings are equal
first_string = 'A literal string'
second_string = "A literal string"
print(first_string == second_string)
print('use \\ \' for escaping characters!')
print('\n')
#use r to print literal characters without escaping
nineth_string = r"A literal string with a \n line character printed raw"
print(nineth_string)
#verbatim string
tenth_string = '''A literal string
on more than one line
sometimes known as a verbatim string\n\n'''

eleventh_string = """Another literal string
     on more than one line
using double quotes"""

print(tenth_string)
print(eleventh_string)
print('\n')
#using the print function()
first = 'Conrad'
second = 'Grant'
third = 'Bob'

print(first, second)
print (first, second, third)
print (first, second, third, sep = '-')
print (first, second, third, sep = '-', end='.')
print('\n')