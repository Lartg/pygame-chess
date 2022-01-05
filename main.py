import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from board import board
from pieces import Piece, Pawn, King
from standard_setup import standard_setup

pygame.init()

def main():
  screen = pygame.display.set_mode([900, 600])
  screen.fill(pygame.Color(255,255,255))
  chess = board()
  chess.draw_board_squares(screen)
  pieces = standard_setup
  
  pygame.display.flip()
  running = True
  step1 = False
  
  while running:
    for piece in pieces:
      piece.render_piece(screen)
    for event in pygame.event.get():
      for piece in pieces:
        if event.type == MOUSEBUTTONDOWN:
            if piece.position == chess.return_board_position(pygame.mouse.get_pos()):
              step1 = True
            pass
        if event.type == MOUSEBUTTONUP:
          if step1 == True:
            print('step2')
            piece.position = chess.return_board_position(pygame.mouse.get_pos())
            piece.render_piece(screen)
            chess.draw_board_squares(screen)
            step1 = False
          pass
      if event.type == pygame.QUIT:
        running = False
    pygame.display.update(200,0,500,500)
    
    

if __name__ == '__main__':
  main()