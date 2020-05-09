import random
import string
a = ''
for i in range(4):
    a.append(random.choice(string.ascci_lowercase))
    a.append(random.choice(string.ascci_uppercase))
    a.ppend(random.choice(string.digits))
    a.appen(random.choice(string.puctuation))
print(a)
