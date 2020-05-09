import sys
if len(sys.argv)==2:
    n = int(sys.argv[1])
    unidad = 1
    while n>0:
        modulito = n%10
        print('{:10d}'.format(modulito*unidad))
        unidad*=10
        n//=10
else:
    print('Debe ingresar un argumento para usar el script.')
