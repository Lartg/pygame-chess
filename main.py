import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from board import board
from pieces import Piece, Pawn, King, Rook, Bishop
from standard_setup import standard_setup
from loggers import run_clocks

pygame.init()

def main():
  screen = pygame.display.set_mode([900, 600])
  background_color = pygame.Color(255,255,255)
  screen.fill(background_color)
  chess = board()
  chess.draw_board_squares(screen)
  pieces = standard_setup
  selected_piece = ''
  pygame.display.flip()
  running = True
  step1 = False
  turn = 1
  clock = pygame.time.Clock()
  w_time = 300
  b_time = 300
  dt = 0
  for piece in pieces:
      piece.render_piece(screen)
  while running:
    
    for event in pygame.event.get():
      if event.type == MOUSEBUTTONDOWN:
        for piece in pieces:
          if piece.position == chess.return_board_position(pygame.mouse.get_pos()):
            selected_piece = piece
            if turn % 2 == 0 and 'b' in selected_piece.name:
              step1 = True              
            elif turn % 2 != 0 and 'w' in selected_piece.name:
              step1 = True            
      if event.type == MOUSEBUTTONUP:
        if step1 == True:
          old_position = selected_piece.position
          selected_piece.move(pieces, chess, screen)
          for piece in pieces:
            if piece != selected_piece and piece.position == selected_piece.position:
              if 'w' in selected_piece.name and 'w' in piece.name:
                selected_piece.position = old_position
              elif 'b' in selected_piece.name and 'b' in piece.name:
                selected_piece.position = old_position
              elif 'w' in piece.name and 'b' in selected_piece.name:                 
                  pieces.remove(piece)
              elif 'b' in piece.name and 'w' in selected_piece.name:
                  pieces.remove(piece)
          step1 = False
          if selected_piece.position != old_position:
            turn += 1
          selected_piece = ''
          for piece in pieces:
            piece.render_piece(screen)
            
      if event.type == pygame.QUIT:
        running = False
      pygame.display.update(200,0,500,500)
      
    if turn % 2 == 0:
      b_time -= dt  
    else:
      w_time -= dt
    
    dt = clock.tick(30)/1000
    run_clocks(w_time, b_time, background_color, screen)
    
      
    pygame.display.update(200,0,500,500)
    
    

if __name__ == '__main__':
  main()