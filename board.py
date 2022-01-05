import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

class board():
  def __init__(self):
    self.board = [
      [1,2,3,4,5,6,7,8],
      [9,10,11,12,13,14,15,16],
      [17,18,19,20,21,22,23,24],
      [25,26,27,28,29,30,31,32],
      [33,34,35,36,37,38,39,40],
      [41,42,43,44,45,46,47,48],
      [49,50,51,52,53,54,55,56],
      [57,58,59,60,61,62,63,64]
    ]
    self.square_size = 50
  
  def draw_board_squares(self, screen):
    for row in self.board:
      for column in row:
        if (row.index(column) + self.board.index(row))%2 == 0:
          square_color = pygame.Color(238,238,210)
          pygame.draw.rect(screen, square_color, pygame.Rect((row.index(column)+1)*self.square_size+200, (self.board.index(row))*self.square_size, self.square_size, self.square_size))
          
        else:
          square_color = pygame.Color(118,150,86)
          pygame.draw.rect(screen, square_color, pygame.Rect((row.index(column)+1)*self.square_size+200, (self.board.index(row))*self.square_size, self.square_size, self.square_size))
    pass

  def return_board_position(self, position):
    files = [
    range(250,301),
    range(300,351),
    range(350,401),
    range(400,451),
    range(450,501),
    range(500,551),
    range(550,601),
    range(600,651)]

    file_names = [
      'A',
      'B',
      'C',
      'D',
      'E',
      'F',
      'G',
      'H'
    ]

    ranks = [
    range(350,401),
    range(300,351),
    range(250,301),
    range(200,251),
    range(150,201),
    range(100,151),
    range(50,101),
    range(0,51)]

    for file in files:
      if position[0] in file:
        file_name = file_names[files.index(file)]
        file = file
        for rank in ranks:
          if position[1] in rank:
            rank_name = str(ranks.index(rank) + 1)
            rank = rank
            return [int(sum(file)/(len(file))), int(sum(rank)/(len(rank)))]

