# Name: Jeffrey
import random
class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__ (self, width, height) :
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

    def __repr__ (self) :
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = '\n'   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        for col in range(0, W) :
            s += " " + str(col%10)
        
        return s+"\n"       # the board is complete, return it
    def addMove (self, col, ox):
        for i in range (0, self.height):
            if self.data[i][col] != " " :
                self.data[i-1][col] = ox
                return None
        self.data[self.height-1][col] = ox
    def clear (self) :
        self.data = [[' ']*self.width for row in range(self.height)]
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
    def allowsMove (self, c) :
        if c < 0 or c >= self.width :
            return False
        if self.data[0][c] != ' ' :
            return False
        return True
    def isFull (self) :
        for i in self.data :
            for j in i :
                if j == ' ' :
                    return False
        return True
    def delMove (self, c) :
        for i in range (self.height) :
            if self.data[i][c] != ' ':
                self.data[i][c] = ' '
                return
    def inarow_Neast (self, ch, r_start, c_start, A, N):
        h = len(A)
        w = len(A[0])
        if r_start < 0 or r_start >= h or c_start < 0 or c_start+N-1 >= w:
            return False
        for i in range(N):
            if A[r_start][c_start+i] != ch:
                return False
        return True
    def inarow_Nsouth (self, ch, r_start, c_start, A, N):
        h = len(A)
        w = len(A[0])
        if r_start < 0 or r_start+N-1 >= h or c_start < 0 or c_start >= w:
            return False
        for i in range(N):
            if A[r_start+i][c_start] != ch:
                return False
        return True
    def inarow_Nse (self, ch, r_start, c_start, A, N):
        h = len(A)
        w = len(A[0])
        if r_start < 0 or r_start+N-1 >= h or c_start < 0 or c_start+N-1 >= w:
            return False
        for i in range(N):
            if A[r_start+i][c_start+i] != ch:
                return False
        return True
    def inarow_Nne (self, ch, r_start, c_start, A, N):
        h = len(A)
        w = len(A[0])
        if r_start-N+1 < 0 or r_start >= h or c_start < 0 or c_start+N-1 >= w:
            return False
        for i in range(N):
            if A[r_start-i][c_start+i] != ch:
                return False
        return True
    def winsFor (self, ox) :
        for i in range(self.height) :
            for j in range(self.width) :
                if self.inarow_Nne(ox, i, j, self.data, 4) \
                    or self.inarow_Nse(ox, i, j, self.data, 4) \
                    or self.inarow_Neast(ox, i, j, self.data, 4) \
                    or self.inarow_Nsouth(ox, i, j, self.data, 4) :
                    return True;
        return False
    
    def hostGame (self) :
        print "Welcome to Connect Four"
        print self
        while True :
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = input("X: Choose a column: ")
            self.addMove(users_col, "X")
            print self
            if self.winsFor("X") :
                print "X wins"
                return
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = input("O: Choose a column: ")
            self.addMove(users_col, "O")
            print self
            if self.winsFor("O") :
                print "O wins"
                return
            elif self.isFull() :
                print "Tie"
                return
            
    def playGame (self, px, po) :
        print "Welcome to Connect Four"
        print self
        while True :
            if px != "human" :
                self.addMove(px.nextMove(self), "X")
            else :
                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = input("X: Choose a column: ")
                self.addMove(users_col, "X")
                
            print self
            if self.winsFor("X") :
                print "X wins"
                return
            
            if po != "human" :
                self.addMove(po.nextMove(self), "O")
            else :
                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = input("O: Choose a column: ")
                self.addMove(users_col, "O")
                
            print self
            if self.winsFor("O") :
                print "O wins"
                return
            elif self.isFull() :
                print "Tie"
                return
    
class Player :
    def __init__ (self, ox, tbt, ply) :
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
    
    def __repr__ (self) :
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh (self) :
        return "O" if self.ox == "X" else "X"
    
    def scoreBoard (self, b) :
        userWon = b.winsFor(self.ox)
        oppWon = b.winsFor(self.oppCh())
        if userWon :
            return 100.0
        elif oppWon :
            return 0.0
        else :
            return 50.0
    def tiebreakMove (self, scores) :
        maxV = -10
        for score in scores :
            if score > maxV :
                maxV = score
        ls = []
        for i in range(len(scores)) :
            if scores[i] == maxV :
                ls.append(i)
        if self.tbt == 'LEFT' :
            return ls[0]
        elif self.tbt == 'RIGHT' :
            return ls[-1]
        else :
            return random.choice(ls)
    
    def scoresFor (self, b) :
        ls = [self.scoreBoard(b)] * b.width
        for i in range(b.width) :
            if not b.allowsMove(i) :
                ls[i] = -1
            elif self.ply != 0 :
                b.addMove(i, self.ox)
                score = self.scoreBoard(b)
                if score == 100.0 :
                    ls[i] = 100.0
                else :
                    opp = Player(self.oppCh(), self.tbt, self.ply-1)
                    bestOpp = max(opp.scoresFor(b))
                    ls[i] = 100.0 - bestOpp
                b.delMove(i)
        return ls
    
    def nextMove (self, b) :
        return self.tiebreakMove(self.scoresFor(b))
board = Board(7, 6)
board.playGame(Player("X", "RANDOM", 5), Player("O", "RANDOM", 5))

   
