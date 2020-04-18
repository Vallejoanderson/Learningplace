def factorial(m):
  if( m != 1 ):
    return factorial( m - 1 ) * m
  else:
    return 1

n = input()
print(factorial(int(n)))
