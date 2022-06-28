import pygame
import os


class Game:
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()
        
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                image = self.images()
                self.screen.blit(image, topLeft)
    
    def loadImages(self):
        self.images={}
        for fileName in os.listdir("images"):
            if(not fileName.endswith(".png")):
                continue
            image = pygame.Image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image




