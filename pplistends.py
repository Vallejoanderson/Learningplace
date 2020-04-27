#Write a program that takes a list
#of numbers (for example,
#a = [5, 10, 15, 20, 25]) and makes
#a new list of only the first and
#last elements of the given list.
#For practice, write this code
#inside a function.

import random
l = []
m = []
for i in range (random.randint(1,20)):
  l.append(random.randint(1,20))
m.append(l[0])
m.append(l[int(len(l))-1])
print(l)
print(m)
