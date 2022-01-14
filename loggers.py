import pygame
from pygame import display

def run_clocks(w_time, b_time, background_color, screen):
  font = pygame.font.Font(None, 64)
# white background/label -----------------------------
  w_background = pygame.draw.rect(screen, background_color, pygame.Rect((0, 0, 200, 100)))
  w_text = font.render('White', True, (10, 10, 10))
  w_textpos = w_text.get_rect(centerx=125, y=10)
  screen.blit(w_text, w_textpos)
# white's time ------------------------------
  
  w_display_time = f'{round(w_time/60)-1}:{round(w_time%60)}'
  w_text = font.render(w_display_time, True, (10, 10, 10))
  w_textpos = w_text.get_rect(centerx=125, y=50)
  
  screen.blit(w_text, w_textpos)

# black background/label -----------------------------
  b_background = pygame.draw.rect(screen, background_color, pygame.Rect((651, 0, 249, 100)))
  b_text = font.render('Black', True, (10, 10, 10))
  b_textpos = b_text.get_rect(centerx=775, y=10)
  screen.blit(b_text, b_textpos)
# white's time ------------------------------
  
  b_display_time = f'{round(b_time/60)-1}:{round(b_time%60)}'
  if b_time == 300:
    b_display_time = '5:00'
  b_text = font.render(b_display_time, True, (10, 10, 10))
  b_textpos = b_text.get_rect(centerx=775, y=50)
  screen.blit(b_text, b_textpos)

def count_material(w_captures, b_captures, screen):
  for piece in w_captures:
    row = w_captures.index(piece)
    if row < 4:
      row = 0
    elif row < 8:
      row = 1
    elif row < 12:
      row = 2
    elif row < 16:
      row = 3
    piece.position = [50 + 50*(w_captures.index(piece)%4), 150 + row*50]
    piece.render_piece(screen)
  for piece in b_captures:
    row = b_captures.index(piece)
    if row < 4:
      row = 0
    elif row < 8:
      row = 1
    elif row < 12:
      row = 2
    elif row < 16:
      row = 3
    piece.position = [700 + 50*(b_captures.index(piece)%4), 150 + row*50]
    piece.render_piece(screen)
  pass

def log_moves(screen, background_color, selected_piece, turn, moves):
  
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
    if selected_piece.position[0] in file:
      file_name = file_names[files.index(file)]
      for rank in ranks:
        if selected_piece.position[1] in rank:
          rank_name = str(ranks.index(rank) + 1)
  
        
        
  move_log_background = pygame.draw.rect(screen, background_color, pygame.Rect((0,400,900,400)))
  font = pygame.font.Font(None, 24)
  
  moves.append(f'{turn}. {selected_piece.name[-1]}{file_name}{rank_name}')
  
  for move in moves:
    column = moves.index(move)
    row = 0
    for x in range(1,15):
      if moves.index(move) > 10*x:
        column -= 11
        row += 1
    
    
    move_text = font.render(move, True, (10, 10, 10))
    move_textpos = move_text.get_rect(centerx=50+75*column, y=420+20*row)
    screen.blit(move_text, move_textpos) 
      
  pass





