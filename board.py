from piece import Piece
from random import random

class Board:
    def __init__(self, size, probability):
        self.size = size
        self.probability = probability
        self.gameOver = False
        self.win = False
        self.numberOfBombsClicked = 0
        self.numberOfNonBombs = 0 
        self.setBoard() 
            
    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):                
                hasBomb = False
                bomb = random()
                if bomb < self.probability:
                    hasBomb = True               
                if (not hasBomb):
                    self.numberOfNonBombs +=1
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()
        
    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)
                
    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0]-1, index[0]+2):
            for col in range(index[1]-1, index[1]+2):
                outOfBoundaries = row < 0 or row >= self.size[0] or col < 0 or col >=self.size[1]
                itself = row == index[0] and col == index[1]
                if(itself or outOfBoundaries):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return  neighbors       
        
    def getSize(self):
        return self.size
    
    def getPiece(self, index):
        return self.board[index[0]][index[1]]
    
    def handleClick(self, piece, flag):
        if piece.getClicked() or not flag and piece.getFlagged():
           return 
        if (flag):
            piece.toggleFlag()
            return
        piece.click()
        if(piece.getHasBomb()):
            self.gameOver = True
            return
        self.numberOfBombsClicked += 1
        if (piece.getNumberOfBombsAround() != 0):
            return
        for neighbor in piece.getNeighbors():
            if(not neighbor.getHasBomb() and not neighbor.getClicked()):
               self.handleClick(neighbor, False)
            
    def getGameOver(self):
        return self.gameOver    
    
    def getWinner(self):
        return self.numberOfNonBombs == self.numberOfBombsClicked    
           
    def getUpdatedBoard(self):        
        print()
        for row in range(self.getSize()[0]):
            print(end="")
            for col in range(self.getSize()[1]):         
                piece = self.board[row][col]
                result = None
                if (piece.getClicked()):
                    if(piece.getHasBomb()):
                        result = "B"
                    else:
                        result = str(piece.getNumberOfBombsAround()) 
                else:
                    if piece.getFlagged():
                        result = "F"            
                    else:
                        result = "U"
                print(str(result), end=" ")
            print()
        print()
        
        
                     