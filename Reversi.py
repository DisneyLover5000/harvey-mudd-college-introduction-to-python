# Name: Jeffrey

import random

#===============================================================================
# CONSTANTS
#===============================================================================
            
POPULATION_SIZE = 10
FITNESS_COUNT = 50
GENERATION_COUNT = 50
dist = [[6,5,4,3,3,4,5,6],
        [5,4,3,2,2,3,4,5],
        [4,3,2,1,1,2,3,4],
        [3,2,1,0,0,1,2,3],
        [3,2,1,0,0,1,2,3],
        [4,3,2,1,1,2,3,4],
        [5,4,3,2,2,3,4,5],
        [6,5,4,3,3,4,5,6]]
f = open('Results.txt', 'w', 0)

#===============================================================================
# Board object that represents the reversi board
#===============================================================================
class Board :
    def __init__ (self, width = 8, height = 8) :
        #=======================================================================
        # Initializes the board object
        # Precondition: Width and height must both be even numbers
        #=======================================================================
        self.width = width
        self.height = height
        self.board = [[0]*width for row in range(height)]
    def __repr__ (self) :
        #=======================================================================
        # Returns a string representing the object
        #=======================================================================
        res = "   "
        for i in range(self.width) :
            res += str(i%10) + " "
        res += "\n"
        res += "   "
        res += "__" * (self.width)
        res += "\n"
        for i in range(self.height) :
            res += str(i%10)+" |"
            for j in range(self.width) :
                if self.board[i][j] == 0 :
                    res += "  "
                elif self.board[i][j] == 1 :
                    res += "O "
                else :
                    res += "X "
            res += "\n"
        return res
    def setInit (self) :
        #=======================================================================
        # Initializes the starting position
        # 1 represents a black piece and 2 represents a white piece
        #=======================================================================
        for i in range(self.height) :
            for j in range(self.width) :
                self.board[i][j] = 0
        self.board[self.height/2][self.width/2] = 1
        self.board[self.height/2-1][self.width/2] = 2
        self.board[self.height/2][self.width/2-1] = 2
        self.board[self.height/2-1][self.width/2-1] = 1
    def getCopy (self) :
        #=======================================================================
        # Returns a copy of the current board
        #=======================================================================
        res = Board()
        for i in range(self.height) :
            for j in range(self.width) :
                res.board[i][j] = self.board[i][j]
        return res
    def isValidMove (self, r, c, color) :
        #=======================================================================
        # Returns True or False depending on if the current move is valid or not
        #=======================================================================
        if r < 0 or r >= self.height or c < 0 or c >= self.width or self.board[r][c] != 0:
            return False
        opp = color % 2 + 1
        valid = False
        for mr in range(-1, 2) :
            for mc in range(-1, 2) :
                cr = r + mr
                cc = c + mc
                hasOpp = False
                while 0 <= cc < self.width and 0 <= cr < self.height :
                    if self.board[cr][cc] == opp :
                        hasOpp = True
                    elif self.board[cr][cc] == color:
                        valid |= hasOpp
                        break
                    elif self.board[cr][cc] == 0 :
                        break
                    cr += mr
                    cc += mc
        return valid
    def movePiece (self, r, c, color) :
        #=======================================================================
        # Place a color piece in (r, c) assuming that the move is legal
        #=======================================================================
        opp = color % 2 + 1
        for mr in range(-1, 2) :
            for mc in range(-1, 2) :
                cr = r + mr
                cc = c + mc
                hasOpp = False
                valid = False
                while 0 <= cc < self.width and 0 <= cr < self.height :
                    if self.board[cr][cc] == opp :
                        hasOpp = True
                    elif self.board[cr][cc] == color:
                        valid = hasOpp
                        break
                    elif self.board[cr][cc] == 0 :
                        break
                    cr += mr
                    cc += mc
                if valid : 
                    cr = r + mr
                    cc = c + mc
                    while 0 <= cc < self.width and 0 <= cr < self.height :
                        if self.board[cr][cc] == color:
                            break
                        self.board[cr][cc] = color
                        cr += mr
                        cc += mc
        self.board[r][c] = color
    def isGameOver (self, color) :
        #=======================================================================
        # Returns true if the game has finished for color
        #=======================================================================
        for i in range(self.height) :
            for j in range(self.width) :
                if self.isValidMove(i, j, color) :
                    return False
        return True
    def countPieces (self) :
        #=======================================================================
        # Return a integer representing the number of 1's minus the number of 0's
        #=======================================================================
        res = 0
        for i in range(self.height) :
            for j in range(self.width) :
                if self.board[i][j] == 1 :
                    res += 1
                elif self.board[i][j] == 2 :
                    res -= 1
        return res
    def getValidMoves (self, color) :
        #=======================================================================
        # Returns a list of valid moves
        #=======================================================================
        res = []
        for i in range(self.height) :
            for j in range(self.width) :
                if self.isValidMove(i, j, color) :
                    res += [[i, j]]
        return res
    def hostGame (self, p1, p2) :
        #=======================================================================
        # Plays a game between p1 and p2
        # Returns > 0 if p1 won, < 0 if p2 won and 0 if it is a tie
        #=======================================================================
        self.setInit()
        humanPlaying = p1 == "Human" or p2 == "Human"
        currMove = 1
        while True :
            if self.isGameOver(currMove) :
                if humanPlaying :
                    print self
                return self.countPieces()
            if p1 == "Human" :
                r = -1
                c = -1
                while not self.isValidMove(r, c, currMove) :
                    if humanPlaying :
                        print self
                    print "(1) Enter a valid square to move: "
                    r = int(raw_input("Enter Row:"))
                    c = int(raw_input("Enter Col:"))
                self.movePiece(r, c, currMove)
            else :
                if humanPlaying :
                    print self
                move = p1.getMove(self)
                self.movePiece(move[0], move[1], currMove)
            
            currMove = currMove % 2 + 1
            if self.isGameOver(currMove) :
                if humanPlaying :
                    print self
                return self.countPieces()
            if p2 == "Human" :
                r = -1
                c = -1
                while not self.isValidMove(r, c, currMove) :
                    if humanPlaying :
                        print self
                    print "(2) Enter a valid square to move: "
                    r = int(raw_input("Enter Row:"))
                    c = int(raw_input("Enter Col:"))
                self.movePiece(r, c, currMove)
            else :
                if humanPlaying :
                    print self
                move = p2.getMove(self)
                self.movePiece(move[0], move[1], currMove)
            currMove = currMove % 2 + 1
#===============================================================================
# Greedy Player that "looks" for future moves to ascertain the current best move
# This player will be the control variable for our genetic algorithm
#===============================================================================
class GreedyPlayer:
    def __init__ (self, color, look) :
        #=======================================================================
        # Initializer for the GreedyPlayer object
        # Color = the color the player is using (1, 2)
        # Look = how many moves into the future should the player "look"
        #=======================================================================
        self.color = color
        self.look = look
    def __repr__ (self) :
        #=======================================================================
        # Returns the string associated with the GreedyPlayer object
        #=======================================================================
        res = "Greedy Player playing "+str(self.color)+" with "+str(self.look)+" moves in the future"
        return res
    def getScores (self, b) :
        #=======================================================================
        # Returns a list of moves and scores associated with the board after self.look moves
        #=======================================================================
        if self.look == 0 :
            return [-1, [(b.countPieces() if self.color == 1 else -b.countPieces())]]
        poss = b.getValidMoves(self.color)
        if len(poss) == 0 :
            return [-1, [(b.countPieces() if self.color == 1 else -b.countPieces())]]
        weight = []
        for x in poss :
            nb = b.getCopy()    
            nb.movePiece(x[0], x[1], self.color)
            np = GreedyPlayer(self.color%2+1, self.look-1)
            weight += [max(np.getScores(nb)[1])]
        return [poss, weight]
    def getMove (self, b) :
        #=======================================================================
        # Picks the best move out of the list returned by getScores()
        # If there are ties, randomly pick
        #=======================================================================
        res = self.getScores(b)
        maxV = max(res[1])
        choose = []
        for i in range(len(res[0])) :
            if res[1][i] == maxV :
                choose += [res[0][i]]
        return random.choice(choose)
#===============================================================================
# Genetic Player will use the symmetry of the grid to its advantage. A square in
# the grid can be identified by the distance away from the center 4 squares.
# 
# 6 5 4 3 3 4 5 6
# 5 4 3 2 2 3 4 5
# 4 3 2 1 1 2 3 4
# 3 2 1 0 0 1 2 3
# 3 2 1 0 0 1 2 3
# 4 3 2 1 1 2 3 4
# 5 4 3 2 2 3 4 5
# 6 5 4 3 3 4 5 6
# Dist is a global 2D array that represents the distances of each grid space
# assuming that the Reversi game is played on a 8x8 grid
#===============================================================================

class GeneticPlayer :
    def __init__ (self, color, values) :
        #=======================================================================
        # Initializer for the GeneticPlayer object
        # Color = the color the player is using (1, 2)
        # Values = list associated with the values to calculate the value of a board
        #=======================================================================
        self.color = color
        self.values = values
    def __repr__ (self) :
        #=======================================================================
        # Returns the string associated with the GeneticPlayer object
        #=======================================================================
        res = "Genetic Player playing "+str(self.color)+" with values of "
        for i in self.values :
            res += str(i) + " "
        res += "\n"
        return res
    def getScores (self, b) :
        #=======================================================================
        # Returns a list of moves and scores associated with the board
        #=======================================================================
        poss = b.getValidMoves(self.color)
        weight = []
        prevSameMoves = len(poss)
        prevDiffMoves = len(b.getValidMoves(self.color % 2 + 1))
        for move in poss :
            nb = b.getCopy()
            nb.movePiece(move[0], move[1], self.color)
            res = 0.0
            currSameMoves = len(nb.getValidMoves(self.color));
            currDiffMoves = len(nb.getValidMoves(self.color % 2 + 1));
            for i in range(b.height) :
                for j in range(b.width) :
                    if self.color == b.board[i][j] :
                        res += self.values[dist[i][j]]
                    elif self.color % 2 + 1 == b.board[i][j] :
                        res -= self.values[dist[i][j]]
            weight += [res + self.values[7] * (prevDiffMoves - currDiffMoves) + self.values[8] * (currSameMoves - prevSameMoves) + self.values[9] * (nb.countPieces() - b.countPieces())]
        return [poss, weight]
    def getMove (self, b) :
        #=======================================================================
        # Picks the best move out of the list returned by getScores()
        # If there are ties, randomly pick
        #=======================================================================
        res = self.getScores(b)
        maxV = max(res[1])
        choose = []
        for i in range(len(res[0])) :
            if res[1][i] == maxV :
                choose += [res[0][i]]
        return random.choice(choose)
    def getFitness (self, player):
        #=======================================================================
        # Get the fitness of the current Genetic Player with FITNESS_COUNT iterations
        #=======================================================================
        b = Board(8, 8)
        res = 0.0
        player.color = self.color % 2 + 1
        for i in range(FITNESS_COUNT) :
            b.setInit()
            if self.color == 1 :
                gameRes = b.hostGame(self, player)
                if gameRes > 0 :
                    res += 1
                elif gameRes == 0 :
                    res += 0.5
            else :
                gameRes = b.hostGame(player, self)
                if gameRes < 0 :
                    res += 1
                elif gameRes == 0 :
                    res += 0.5
            print i
        return res / FITNESS_COUNT
#===============================================================================
# Random Player will randomly pick from the available moves
#===============================================================================
class RandomPlayer :
    def __init__ (self, color) :
        #=======================================================================
        # Initializer for the RandomPlayer object
        # Color = the color the player is using (1, 2)
        # Values = list associated with the values to calculate the value of a board
        #=======================================================================
        self.color = color
    def __repr__ (self) :
        #=======================================================================
        # Returns the string associated with the GeneticPlayer object
        #=======================================================================
        res = "Random Player playing "+str(self.color)+"\n"
        return res
    def getMove (self, b) :
        #=======================================================================
        # Picks a random move
        #=======================================================================
        return random.choice(b.getValidMoves(self.color))
class Tester :
    def __init__ (self, player) :
        #=======================================================================
        # Initializes the Tester object with a starting population of size POPULATION_SIZE
        # The fitness of the starting population is also evaluated with FITNESS_COUNT iterations
        #=======================================================================
        self.player = player
        players = []
        for i in range(POPULATION_SIZE) :
            curr = []
            for j in range(10) :
                curr += [random.random()]
            players += [curr]
        self.list = []
        for i in range(POPULATION_SIZE) :
            self.list += [[(players[i]), GeneticPlayer(1, players[i]).getFitness(player)]]
        #print self.list
        self.list = sorted(self.list, key=lambda player : player[1], reverse = True)
        f.write("GENERATION 0\n")
        for i in self.list :
            f.write(str(i[0]) + " " + str(i[1])+"\n")
    def getNextGeneration (self, gen) :
        newList = [self.list[0], self.list[1]]
        newList[0][1] = GeneticPlayer(1, newList[0][0]).getFitness(self.player)
        newList[1][1] = GeneticPlayer(1, newList[1][0]).getFitness(self.player)
        for x in range(POPULATION_SIZE-2) :
            i = random.choice(range(POPULATION_SIZE))
            j = random.choice(range(POPULATION_SIZE))
            curr = []
            for y in range(10) :
                minV = min(self.list[i][0][y], self.list[j][0][y])
                maxV = max(self.list[i][0][y], self.list[j][0][y])
                curr = random.random() * (maxV - minV) + minV
                ran = random.random()
                if ran < 0.1 :
                    curr[y] = random.random()
            newList += [[curr, GeneticPlayer(1, curr).getFitness(self.player)]]
        self.list = newList;
        self.list = sorted(self.list, key=lambda player : player[1], reverse = True)
        f.write("GENERATION "+str(gen)+"\n")
        for i in self.list :
            f.write(str(i[0]) + " " + str(i[1])+"\n")
        f.flush()
'''
b = Board()
p2 = RandomPlayer(2)
sum = 0
for i in range(1) :
    b.setInit()
    res = b.hostGame(p1, p2)
    if res > 0 :
        sum += 1
    elif res == 0 :
        sum += 0.5
    else :
        sum -= 1
    print res
print sum
'''
f.write("POPULATION SIZE  " + str(POPULATION_SIZE) + "\n")
f.write("FITNESS COUNT: " + str(FITNESS_COUNT) + "\n")
f.write("GENERATION COUNT: " + str(GENERATION_COUNT) + "\n")
t = Tester(GreedyPlayer(2, 1))
for i in range(1, GENERATION_COUNT+1) :
    print "ON GENERATION " + str(i)
    t.getNextGeneration(i)

