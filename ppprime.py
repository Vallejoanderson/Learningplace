def prime(number):
  i = number - 1
  while( number % i != 0 and i > 1 ):
    i+=-1
  return i == 1
    
m = (int(input()))
print('Is it a prime number?')
print(': ', prime(m))
