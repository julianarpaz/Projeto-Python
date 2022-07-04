from game import Game
from board import Board

size = (9,9)
board = Board(size)
screenSize = (600, 600)

game = Game(board, screenSize)
game.run()

