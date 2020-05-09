import sys
if len(sys.argv) == 3:
    if( int(sys.argv[1])>0 and int(sys.argv[1])<10 and int(sys.argv[2])>0 and int(sys.argv[2])<10 ):
        none = int(sys.argv[1])
        ntwo = int(sys.argv[2])
        for i in range(none):
            for j in range(ntwo):
                print('**', end='')
            print('\n')    
    else:
        print('Los argumentos no cumplen con los requisitos necesarios 0 <  x < 10')
else:
    print('La cantidad de argumentos es incorrecta, comprueba que esta usando dos argumentos validos')
