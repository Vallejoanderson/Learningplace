z = [ 
     [1, 1, 1, 3],
     [2, 2, 2, 7],
     [3, 3, 3, 9],
     [4, 4, 4, 13] 
    ]

z[0][-1] = sum( z[0][:-1] )
z[1][-1] = sum( z[1][:-1] )
z[2][-1] = sum( z[2][:-1] )
z[3][-1] = sum( z[3][:-1] )
print(z)