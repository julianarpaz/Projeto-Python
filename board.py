from piece import Piece
from random import random

class Board:
    def __init__(self, size, probability):
        self.size = size
        self.probability = probability
        self.setBoard()        

    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.probability
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