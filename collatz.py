def collatz(n):
    if n%2==0:
        return( n // 2 )
    else:
        return( 3 * n + 1 )

flag = True
print('Write a number')
try:
  m = int(input())    
  while flag:
    m = collatz(m)
    print('El retorno es de: ', end='')
    print(m)
    if m == 1:
      flag = False
except ValueError:
    print('Must enter a integer number')
