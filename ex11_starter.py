#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# turned the belgium variable into a list to then find the index
Belgium_list = Belgium.split(',')
# hyphen multiply the length of the string, the commas are part of the string

print("-"*len(Belgium))

# this method needs 2 arguments, so the first is the comma to get rid of (belongs to the string),
# and the second is the one that will replace

# string.replace(oldvalue, newvalue)

print(Belgium.replace(',', ':'))

# this is the slicing method, returning a certain string using a start index and an end index.

# belgium_population = int(Belgium[8:16])
# print(belgium_population)
#
# brussels_population = int(Belgium[26:32])
# print(brussels_population)

# created two variables to obtain 2 different parts of the string and using the index to find in the list.

belgium_population = int(Belgium_list[1])
print(belgium_population)

brussels_population = int(Belgium_list[3])
print(brussels_population)

# had to add the int() to turn the string into an integer

total_population = belgium_population + brussels_population
print(f'The total population is: {total_population}')

# used the shorthand formatting method called string interpolation
