l = [['.', '.', '.', '.', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['.', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.']]
row = int( len(l) )
column = int( len(l[0]) )
print(row)
print(column)
  
for i in range( column  ):
  for j in range( row  ):
    print( str(l[j][i]), end='' )
  print('\n')
