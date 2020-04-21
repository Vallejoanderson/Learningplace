print('Enter a number')
n = int( input() )
list = []
x = range(2,n)
for i in x :
  if(n%i==0):
    list.append(i)
print(list)
