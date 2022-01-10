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


class Pawn(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [self.position[0] - new_position[0], self.position[1] - new_position[1]]
    if 'w' in self.name:
      if self.position[1] > 6*board.square_size:
        if translation[0] == 0 and translation[1] == board.square_size or translation[0] == 0 and translation[1] == 2*board.square_size:
          self.position = board.return_board_position(pygame.mouse.get_pos())
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return
      elif translation[0] == 0 and translation[1] == board.square_size:
        self.position = board.return_board_position(pygame.mouse.get_pos())
        self.render_piece(screen)
        board.draw_board_squares(screen)
        return
      elif translation == [50,50] or translation == [-50, 50]:
        for piece in pieces:
          if piece != self and piece.position == new_position:
            self.position = board.return_board_position(pygame.mouse.get_pos())
            self.render_piece(screen)
            board.draw_board_squares(screen)
        return
    if 'b' in self.name:
      if self.position[1] < 2*board.square_size:
        if translation[0] == 0 and translation[1] == -board.square_size or translation[0] == 0 and translation[1] == -2*board.square_size:
          self.position = board.return_board_position(pygame.mouse.get_pos())
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return
      elif translation[0] == 0 and translation[1] == -board.square_size:
        self.position = board.return_board_position(pygame.mouse.get_pos())
        self.render_piece(screen)
        board.draw_board_squares(screen)
        return
      elif translation == [50,-50] or translation == [-50, -50]:
        for piece in pieces:
          if piece != self and piece.position == new_position:
            self.position = board.return_board_position(pygame.mouse.get_pos())
            self.render_piece(screen)
            board.draw_board_squares(screen)
        return
      
  def promote_pawn():
    pass
  pass

class Bishop(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [self.position[0] - new_position[0], self.position[1] - new_position[1]]
    if translation[0] != 0 and translation[1] != 0:
      if translation[0] % board.square_size == 0 and translation[1] % board.square_size == 0:
        if translation[0] / translation[1] == 1 or translation[0] / translation[1] == -1:
          self.position = board.return_board_position(pygame.mouse.get_pos())
          self.render_piece(screen)
          board.draw_board_squares(screen)
          pass  
    pass
  pass


class Knight(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [self.position[0] - new_position[0], self.position[1] - new_position[1]]
    if translation[1] == 2*board.square_size or translation[1] == -2*board.square_size:
      if translation[0] == board.square_size or translation[0] == -board.square_size:
        self.position = board.return_board_position(pygame.mouse.get_pos())
        self.render_piece(screen)
        board.draw_board_squares(screen)
    elif translation[0] == 2*board.square_size or translation[0] == -2*board.square_size:
      if translation[1] == board.square_size or translation[1] == -board.square_size:
        self.position = board.return_board_position(pygame.mouse.get_pos())
        self.render_piece(screen)
        board.draw_board_squares(screen)
    
  pass

class Rook(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    if self.position == new_position:
      return
    elif self.position[0] ==  new_position[0]:
      pass
    elif self.position[1] == new_position[1]:
      pass
    else:
      return
    self.position = board.return_board_position(pygame.mouse.get_pos())
    self.render_piece(screen)
    board.draw_board_squares(screen)
    pass
  pass
class Queen(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [self.position[0] - new_position[0], self.position[1] - new_position[1]]
    if translation[0] != 0 and translation[1] != 0:
      if translation[0] % board.square_size == 0 and translation[1] % board.square_size == 0:
        if translation[0] / translation[1] == 1 or translation[0] / translation[1] == -1:
          self.position = board.return_board_position(pygame.mouse.get_pos())
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return
    if self.position == new_position:
      return
    elif self.position[0] ==  new_position[0]:
      pass
    elif self.position[1] == new_position[1]:
      pass
    else:
      return
    self.position = board.return_board_position(pygame.mouse.get_pos())
    self.render_piece(screen)
    board.draw_board_squares(screen)
    return

class King(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [self.position[0] - new_position[0], self.position[1] - new_position[1]]
    if translation[0] <= 50 and translation[0] >= -50:
      if translation[1] <= 50 and translation[1] >= -50:
        if translation[0] != 0 or translation[1]!= 0:
          self.position = board.return_board_position(pygame.mouse.get_pos())
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return
    pass
  def check():
    pass
  pass