from game import Game
from board import Board

size = (9,9)
probability = 0.5
board = Board(size, probability)
screenSize = (600, 600)

game = Game(board, screenSize)
game.run()

