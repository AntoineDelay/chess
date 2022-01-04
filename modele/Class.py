
class Case :
    def __init__(self,x,y):
        self.id = str(x)+','+str(y)
        self.x = x
        self.y = y
        self.piece = None
        
    def check_case(self):
        """renvoie la piece si la case est occupé,renvoie -1 sinon """
        if(self.piece != None):
            return self.piece
        return -1
    def affecter_piece(self,piece):
        self.piece = piece
        
        self.piece.case_affectation(self)
        
    def desaffecter_piece(self):
        if self.piece != None :
            self.piece = None
    def show(self):
        if self.piece != None and self.piece.case != None :
            return "| "+str(self.piece.point)+" |"
        else :
            return "| 0 |"
    def get_piece(self):
        return self.piece   
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class Board : 
    def __init__(self,liste_case):
        self.board = liste_case
    def get_case(self,x,y):
        for i in range(len(self.board)):
            if self.board[i].x == x and self.board[i].y == y:
                return self.board[i]
        return -1
    def show_board(self):
        x = 0
        s_board = ""
        for case in self.board :
            if case.x > x :
                s_board += "\n"
                x+=1
            s_board += case.show()
        print(s_board)

class Piece :
    def __init__(self,name,color,point,board):
        self.name = name
        self.color = color
        self.point = point
        self.case = None
        self.board = board
        self.depla = []
        
   
    def possible_depla(self):
        """calcule les déplacement actuellement possible sans contrainte externe, resultat dans depla"""
        pass
    def case_affectation(self,case):
        self.case = case
    def get_depla(self):
        return self.depla
class Pion(Piece) :
    def __init__(self,color,board):
        super().__init__('Pion',color,1,board)
    def possible_depla(self):
        id_case = str(self.case.get_x())+','+str(self.case.get_y()+1)
        id_case_2 = None
        if self.case.get_y() == 2 :
            id_case_2 =  str(self.case.get_x())+','+str(self.case.get_y()+1)
        for case in self.board.board:
            if case.id == id_case and case.piece == None :
                self.depla.append(case)
            if id_case_2 != None and case.id == id_case_2 and case.piece == None:
                self.depla.append(case) 
 
       

        
class Roi(Piece):
    def __init__(self,color,board):
        super().__init__('Roi',color,1000,board)
class Dame(Piece) : 
    def __init__(self,color,board):
        super().__init__('Dame',color,9,board)
