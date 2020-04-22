#Let’s say I give you a list
#saved in a variable: 
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Write one line of Python that takes this
#list a and makes a new list that has only
#the even elements of this list in it.

import random
n = random.randint(1,20)
l1 = []
l2  = []
for i in range(n):
  l1.append(random.randint(1,20))
  if l1[i]%2==0:
    l2.append(l1[i])
print(l1)
print(l2)
