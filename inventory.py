dictionary = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    sum = 0
    print('\nInventory: \n')
    for k, v in dictionary.items():
        print(v,k,'\n')
        sum+=dictionary[k]
    print('Total number of items: ' + str(sum))

displayInventory(dictionary)

#************** ADD ITEMS SECTION ********************************

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addtoInventory(inventory, addedItems):
    for i, inside in enumerate(dragonLoot):
        inventory.setdefault(inside, 0)
        inventory[inside] = inventory[inside] + 1
        
addtoInventory(dictionary, dragonLoot)
displayInventory(dictionary)
