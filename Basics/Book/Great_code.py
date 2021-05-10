print('Hello world')
# Creating length-N  
four_nones = [None]*4
print(four_nones)
#lists are immutable therefor better to use append
four_nones  = [[] for _ in range(4)]
four_nones[0].append('Ni')
print(four_nones)

#read us

import sys

print(sys.path)


# from modu import*         x = sqrt(4)     very bad
# from modu import sqrt     x = sqrt(4)     better
# import modu               x = sqrt(4)     best