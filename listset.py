import random

def listy(list):
  n = random.randint(1,20)
  for i in range(n):
    list.append(random.randint(1,20))

list = []
listy(list)
names = set(list)
print(list)
print(names)
