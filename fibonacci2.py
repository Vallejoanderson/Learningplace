def fibonacci(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else:
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
  m = fibonacci(int(i))
  print(m, end=', ')

