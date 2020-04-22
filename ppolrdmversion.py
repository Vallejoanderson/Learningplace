import random
a = []
b = []
c = []
for i in range(random.randint(1,20)):
  a.append(random.randint(1,20))
for i in range(random.randint(1,20)):
  b.append(random.randint(1,20))
print(a)
print(b)
for i in range(int(len(a))):
    if a[i] in b and a[i] not in c:
        c.append(a[i])
print(c)
