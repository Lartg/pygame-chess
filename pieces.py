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
          for piece in pieces:
            if piece != self and piece.position == new_position:
              return 
          self.position = board.return_board_position(pygame.mouse.get_pos())
         
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return
      elif translation[0] == 0 and translation[1] == board.square_size:
        for piece in pieces:
            if piece != self and piece.position == new_position:
              return
        
        self.position = board.return_board_position(pygame.mouse.get_pos())
      
        self.render_piece(screen)
        board.draw_board_squares(screen)
        return
      elif translation == [board.square_size,board.square_size] or translation == [-board.square_size, board.square_size]:
        for piece in pieces:
          if piece != self and piece.position == new_position:
            self.position = board.return_board_position(pygame.mouse.get_pos())
           
            self.render_piece(screen)
            board.draw_board_squares(screen)
        return
    if 'b' in self.name:
      if self.position[1] < 2*board.square_size:
        if translation[0] == 0 and translation[1] == -board.square_size or translation[0] == 0 and translation[1] == -2*board.square_size:
          for piece in pieces:
            if piece != self and piece.position == new_position:
              return 
          self.position = board.return_board_position(pygame.mouse.get_pos())
          
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return
      elif translation[0] == 0 and translation[1] == -board.square_size:
        for piece in pieces:
            if piece != self and piece.position == new_position:
              return 
        self.position = board.return_board_position(pygame.mouse.get_pos())
        
        self.render_piece(screen)
        board.draw_board_squares(screen)
        return
      elif translation == [board.square_size,-board.square_size] or translation == [-board.square_size, -board.square_size]:
        for piece in pieces:
          if piece != self and piece.position == new_position:
            self.position = board.return_board_position(pygame.mouse.get_pos())
            
            self.render_piece(screen)
            board.draw_board_squares(screen)
        return
  def promote(self, selected_piece, pieces):
    
    pass
      
  
  pass

class Bishop(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [-self.position[0] + new_position[0], -self.position[1] + new_position[1]]
    x_increment = 1
    if translation[0] < 0:
      x_increment = -1
    y_increment = 1
    if translation[1] < 0:
      y_increment = -1
    paths = []
    for x in range(0, abs(int(translation[0]/board.square_size))):
        path = [self.position[0] + x*board.square_size*x_increment, self.position[1] + x*board.square_size*y_increment]
        paths.append(path)
    for piece in pieces:
      if piece != self:
        for path in paths:
          if ('w' in self.name and 'w' in piece.name) or ('b' in self.name and 'b' in piece.name):
              if piece.position == path:
                paths = []
                return
          elif ('b' in self.name and 'w' in piece.name) or ('w' in self.name and 'b' in piece.name):
            if piece.position == path and new_position != piece.position:
                paths = []
                return
            
                
    if translation[0] != 0 and translation[1] != 0:
      if translation[0] % board.square_size == 0 and translation[1] % board.square_size == 0:
        if translation[0] / translation[1] == 1 or translation[0] / translation[1] == -1:
          self.position = board.return_board_position(pygame.mouse.get_pos())
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return 


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
    translation = [-self.position[0] + new_position[0], -self.position[1] + new_position[1]]
    if translation[0] != 0:
      translation = translation[0]
      translation_axis = 'x'
      translation_increment =1
      if translation < 0:
        translation_increment =-1
    else:
      translation = translation[1]
      translation_axis = 'y'
      translation_increment =1
      if translation < 0:
        translation_increment =-1
    paths = []

    for x in range(0, abs(int(translation/board.square_size))):
      if translation_axis == 'x':
        path = [self.position[0] + x*board.square_size*translation_increment, self.position[1]]
      elif translation_axis == 'y':
        path = [self.position[0], self.position[1] + x*board.square_size*translation_increment]
      paths.append(path)
    for piece in pieces:
      if piece != self:
        for path in paths:
          if ('w' in self.name and 'w' in piece.name) or ('b' in self.name and 'b' in piece.name):
              if piece.position == path:
                paths = []
                return
          elif ('b' in self.name and 'w' in piece.name) or ('w' in self.name and 'b' in piece.name):
            if piece.position == path and new_position != piece.position:
                paths = []
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
    pass
  pass
class Queen(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [-self.position[0] + new_position[0], -self.position[1] + new_position[1]]
    if translation[0] != 0 and translation[1] != 0:
      x_increment = 1
      if translation[0] < 0:
        x_increment = -1
      y_increment = 1
      if translation[1] < 0:
        y_increment = -1
      paths = []
      for x in range(0, abs(int(translation[0]/board.square_size))):
          path = [self.position[0] + x*board.square_size*x_increment, self.position[1] + x*board.square_size*y_increment]
          paths.append(path)
      for piece in pieces:
        if piece != self:
          for path in paths:
            if ('w' in self.name and 'w' in piece.name) or ('b' in self.name and 'b' in piece.name):
                if piece.position == path:
                  paths = []
                  return
            elif ('b' in self.name and 'w' in piece.name) or ('w' in self.name and 'b' in piece.name):
              if piece.position == path and new_position != piece.position:
                paths = []
                return   
      if translation[0] % board.square_size == 0 and translation[1] % board.square_size == 0:
        if translation[0] / translation[1] == 1 or translation[0] / translation[1] == -1:
          self.position = board.return_board_position(pygame.mouse.get_pos())
          self.render_piece(screen)
          board.draw_board_squares(screen)
          return 
    else:
      if translation[0] != 0:
        translation = translation[0]
        translation_axis = 'x'
        translation_increment =1
        if translation < 0:
          translation_increment =-1
      else:
        translation = translation[1]
        translation_axis = 'y'
        translation_increment =1
        if translation < 0:
          translation_increment =-1
      paths = []

      for x in range(0, abs(int(translation/board.square_size))):
        if translation_axis == 'x':
          path = [self.position[0] + x*board.square_size*translation_increment, self.position[1]]
        elif translation_axis == 'y':
          path = [self.position[0], self.position[1] + x*board.square_size*translation_increment]
        paths.append(path)
      for piece in pieces:
        if piece != self:
          for path in paths:
            if ('w' in self.name and 'w' in piece.name) or ('b' in self.name and 'b' in piece.name):
                if piece.position == path:
                  paths = []
                  return
            elif ('b' in self.name and 'w' in piece.name) or ('w' in self.name and 'b' in piece.name):
              if piece.position == path and new_position != piece.position:
                paths = []
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
      pass
    pass



class King(Piece):
  def move(self, pieces, board, screen):
    new_position = board.return_board_position(pygame.mouse.get_pos())
    translation = [self.position[0] - new_position[0], self.position[1] - new_position[1]]
    if self.position == [475, 375] and 'w' in self.name:
        if new_position[0] == 575 and new_position[1] == 375:
          for piece in pieces:
              if piece.name == 'wR' and piece.position == [625,375]:
                piece.position = [525,375]
                self.position = board.return_board_position(pygame.mouse.get_pos())
                self.render_piece(screen)
                board.draw_board_squares(screen)
                return
        elif new_position[0] == 375 and new_position[1] == 375:
          for piece in pieces:
              if piece.name == 'wR' and piece.position == [275,375]:
                piece.position = [425,375]
                self.position = board.return_board_position(pygame.mouse.get_pos())
                self.render_piece(screen)
                board.draw_board_squares(screen)
                return
    if self.position == [475, 25] and 'b' in self.name:
        if new_position[0] == 575 and new_position[1] == 25:
          for piece in pieces:
              if piece.name == 'bR' and piece.position == [625, 25]:
                piece.position = [525, 25]
                self.position = board.return_board_position(pygame.mouse.get_pos())
                self.render_piece(screen)
                board.draw_board_squares(screen)
                return
        elif new_position[0] == 375 and new_position[1] == 25:
          for piece in pieces:
              if piece.name == 'bR' and piece.position == [275,25]:
                piece.position = [425,25]
                self.position = board.return_board_position(pygame.mouse.get_pos())
                self.render_piece(screen)
                board.draw_board_squares(screen)
                return
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

