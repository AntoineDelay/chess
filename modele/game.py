import Class as chess_c
def game():
    liste_case = []
    for i in range(8):
        for j in range(8):
            
            liste_case.append(chess_c.Case(i,j))
    board = chess_c.Board(liste_case)
    pion = chess_c.Pion('blanc',board)
    board.get_case(1,2).affecter_piece(pion)
    for case in board.board :
        if case.get_x() == 1 :
            case.affecter_piece(chess_c.Pion('Noir',board))
        if case.get_x() == 6 :
            case.affecter_piece(chess_c.Pion('Blanc',board))
    board.show_board()
    board.get_case(1,1).get_piece().possible_depla()
    print(board.get_case(1,1).get_piece().get_depla())
game()