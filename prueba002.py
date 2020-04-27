message = 'This is a test'
count = {}
for i in message:
    print(i)
    prueba(count.setdefault(i,0))
