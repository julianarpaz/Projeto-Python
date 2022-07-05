class Piece():
    
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        
    def getHasBomb(self):
        return self.hasBomb
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumberOfBombsAround()
        
    def setNumberOfBombsAround(self):
        self.numberOfBombsAround = 0
        for piece in self.neighbors:
            if (piece.getHasBomb()):
                self.numberOfBombsAround += 1                
    
    def getNumberOfBombsAround(self):
        return self.numberOfBombsAround