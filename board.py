import pprint
board = {'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn', 'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn', 'a1': 'wtower', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen', 'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wtower', 'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn', 'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn', 'a8': 'btower', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen', 'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'btower'} 

#piecespermitted = {'wpawn': 8, 'wtowers': 2, 'wknight': 2 ,'wbishop': 2, 'wqueen': 1, 'wking': 1, 'bpawn': 8, #'btowers': 2, 'bknight': 2 ,'bbishop': 2, 'bqueen': 1, 'bking': 1 }

piecescounted = {}

def squareVerification(boardsquare):
    flag = True
    for i in board:
        if( i[0]<'a' or i[0]>'h' or i[1]<str(1) or i[1]>str(8) ):
            print('No se puede ubicar la pieza', board[i], 'en la casilla', i)
            print('Casilla inexistente')
            flag = False
    return flag
            
def maxPiecesVerif(piecescounted, board):
    flag = True
    for keys, inside in board.items():
        piecescounted.setdefault(inside, 0)
        piecescounted[inside] = piecescounted[inside] + 1
    pprint.pprint(piecescounted)
    if( piecescounted['wpawn'] > 8 or piecescounted['bpawn'] > 8 or piecescounted['wtower'] > 2 or  \
        piecescounted['btower'] > 2 or piecescounted['wknight'] > 2 or piecescounted['bknight'] > 2 or \
        piecescounted['wbishop'] > 2 or piecescounted['bbishop'] > 2 or piecescounted['wqueen'] > 1 or \
        piecescounted['bqueen'] > 1 or piecescounted['wking'] > 1 or piecescounted['bking'] > 1 ): 
        print('La cantidad de piezas es invalida')
        flag = False
    return flag

if (squareVerification(board) and maxPiecesVerif(piecescounted, board)):
    print('La configuracion del tablero es correcta')
else:
    print('La configuracion del tablero es incorrecta')
