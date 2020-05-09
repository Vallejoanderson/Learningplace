listbikers = []

def doesExist(listbikers, name): #Check if the name is already in the list.
    flag = True
    for bikeryped in listbikers:
        if name in bikeryped:
            flag = False
    return flag 

def addbiker(listbikers): #Agregar un nuevo ciclista en forma de diccionario a la lista
    biker = {}
    c = input(('Ingrese el nombre del nuevo biker: ')) 
    if doesExist(listbikers, c):
        biker[c] = 0
        listbikers.append(biker)
    else:
        print('The bikers is already in the list\n')
    
def sumarpedidos(listbikers, n): #Summar cantidad n de pedidos al biker
    sumped = int(input('Add this amount of deliveries to the biker: '))
    for biker in listbikers[n]:
        listbikers[n].setdefault(biker, 0)
        listbikers[n][biker] = listbikers[n][biker] + sumped

def deleteBiker(listbikers):
    c = int(input('Select the biker you want to remove from the list.'))
    listbikers.remove(c)

#def orderList(): #Se ordena la lista
    
def menu(listbikers): #Menu que muestra los ciclistas disponibles y la cantidad de pedidos
    flag = True  
    while flag:
        l = len(listbikers)
        print('(-1) Add a new biker to list.')
        #Ordenar lista acorde a numero de pedidos
        for pos, bikeryped in enumerate(listbikers):
            print('({:2d}) {}'.format(pos, bikeryped))
        print('({:2d}) Exit.'.format(l))
        print('({:2d}) Delete biker\n'.format(l+1))
        n = int(input())
        if n == l:
            flag = False
        elif( n == -1 ):     
            addbiker(listbikers)
        elif n == l + 1:
            deleteBiker(listbikers)
        elif n < l: #Sumar pedidos al biker
            sumarpedidos(listbikers, n)
        else:
            print('Invalid option, try again.')

menu(listbikers)
#c = list(listbikers[0].keys())[0]
#print(c)
#print(list(listbikers[0].values())[0]) #Prueba que arroja el valor del diccionar en la casilla n de la lista
#pprint.pprint(listbikers)
