import pygame
from board import board
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
images = {
  'wP': 'Sprites/whitePawn.png',
  'bP':'Sprites/blackPawn.png',
  'wR':'Sprites/whiteRook.png',
  'bR':'Sprites/blackRook.png',
  'wN':'Sprites/whiteKnight.png',
  'bN':'Sprites/blackKnight.png',
  'wB':'Sprites/whiteBishop.png',
  'bB':'Sprites/blackBishop.png',
  'wK':'Sprites/whiteKing.png',
  'bK':'Sprites/blackKing.png',
  'wQ':'Sprites/whiteQueen.png',
  'bQ':'Sprites/blackQueen.png'
}

class Piece():
  def __init__(self, name, positionX, positionY):
    self.name = name
    self.image = pygame.image.load(images[self.name])
    self.position = [positionX, positionY]
    pass
  def render_piece(self, screen):
    screen.blit(self.image, (self.position[0]-25, self.position[1]-25))
    pass
  def move(self, board):
    self.position = board.return_board_position(pygame.mouse.get_pos())
    pass
  def check_capture(self):
    pass


class Pawn():
  def __init__(self):
    pass

class King():
  def __init__(self):
      pass