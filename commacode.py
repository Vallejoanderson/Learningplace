spam = ['apples', 'bananas', 'tofu', 'cats'] 
def rewrite(list):
    char = ''
    for i in range( int(len(list)) ):
      char = char + list[i] + ','
    return(char)
char = rewrite(spam)
print('\'' + char[0:int(len(char))-1] + '\'')

