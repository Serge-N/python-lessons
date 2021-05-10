#capitalize
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())
print('\n\n\n\n')
#lower and upper case
message2 = 'hello world'
print(message2.lower())
print(message2.upper())

message2 = message2.title()
print(message2)
print(message2.swapcase())
print('\n\n\n\n')

#letter count
location = 'Mississipi'
print (location.count('s'))

print(len('how many letters in this string?'))
print('\n\n\n\n')

#ended on string inspection

message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

print('\n\n\n\n')

message='The quick brown fox jumps over the lazy dog'
print(message.find('q'))
print(message.find('t'))
print(message.find('T'))

print('\n\n\n\n')

message = ' middle '

print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')

print('\n\n\n\n')

message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

print('\n\n\n\n')

message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '_'))