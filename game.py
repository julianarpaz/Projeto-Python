
import pygame
import os

class Game:
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:            
            for event in pygame.event.get():
                self.board.getUpdatedBoard()
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]                    
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            #if(self.board.getWinner() or self.board.getGameOver()):
                #running = False            tirei pra a tela não fechar quando perder
        pygame.quit()
        
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                #image = self.images["unopened-square"]
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0]+ self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1]+ self.pieceSize[1]
    
    def loadImages(self):
        self.images={}
        for fileName in os.listdir("assets"):
            if(not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"assets/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image
            
    def getImage(self, piece):
        string = None
        if (piece.getClicked()):
            if(piece.getHasBomb()):
                string = "clicked-block-with-bomb"
            else:
               string = str(piece.getNumberOfBombsAround()) 
        else:
            if piece.getFlagged():
                string = "flag"            
            else:
                string = "unopened-square" 
                
        #string = None
        #if (piece.getClicked()):
            #pass
        #else:
            #if piece.getFlagged():
                #string = "flag"            
            #else:
                #string = "unopened-square"
                                
        #if piece.getHasBomb():   se quiser testar que a probabilidade funciona mesmo pode descomentar dessa linha até a 76
            #string = "unclicked-block-with-bomb"   e comentar o que tem acima, dai só aparecerá as bombas e os números vizinhos
        #else:
            #string = str(piece.getNumberOfBombsAround())               
        
        return self.images[string]
    
    def handleClick(self, position, rightClick):
        if(self.board.getGameOver()):
            return
        index = position [1]//self.pieceSize[1], position[0]//self.pieceSize[0]
        #print(index)
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)



