word = input()
reverse = ''
llist = word.split()
x = int(len(llist)) - 1
for i in range(x, -1, -1):
  reverse = reverse + llist[i] + ' '
print(reverse)

