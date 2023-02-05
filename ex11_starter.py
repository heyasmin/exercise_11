#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# hyphen times the length of the string, the commas are part of the string
print("-"*len(Belgium))
# this method needs 2 arguments, so the first is the comma to get rid of (belongs to the string), and the second is the one that will replace
# string.replace(oldvalue, newvalue)
print(Belgium.replace(',',':'))

# this is the slicing method
belgium_population = Belgium[8:16]
print(belgium_population)
brussels_population = Belgium[26:32]
print(brussels_population)


