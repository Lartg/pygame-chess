import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from board import board
from pieces import Piece, Pawn, King, Rook, Bishop
from standard_setup import standard_setup

pygame.init()

def main():
  screen = pygame.display.set_mode([900, 600])
  screen.fill(pygame.Color(255,255,255))
  chess = board()
  chess.draw_board_squares(screen)
  pieces = standard_setup
  selected_piece = ''
  pygame.display.flip()
  running = True
  step1 = False
  for piece in pieces:
      piece.render_piece(screen)
  while running:
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            print(chess.return_board_position(pygame.mouse.get_pos()))
            for piece in pieces:
              if piece.position == chess.return_board_position(pygame.mouse.get_pos()):
                step1 = True
                selected_piece = piece
        if event.type == MOUSEBUTTONUP:
          if step1 == True:
            selected_piece.move(chess, screen)
            step1 = False
            selected_piece = ''
            for piece in pieces:
              piece.render_piece(screen)
            pass
    if event.type == pygame.QUIT:
      running = False
    pygame.display.update(200,0,500,500)
    
    

if __name__ == '__main__':
  main()