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
            
    def getSize(self):
        return self.size
    
    def getPiece(self, index):
        return self.board[index[0]][index[1]]
