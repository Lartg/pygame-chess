import pygame

def run_clocks(w_time, background_color, screen):
  font = pygame.font.Font(None, 64)
# white background/label -----------------------------
  background = pygame.draw.rect(screen, background_color, pygame.Rect((0, 0, 200, 200)))
  white = font.render('White', True, (10, 10, 10))
  white_textpos = white.get_rect(centerx=125, y=10)
  screen.blit(white, white_textpos)
# white's time ------------------------------
  
  w_display_time = f'{round(w_time/60)-1}:{round(w_time%60)}'
  text = font.render(w_display_time, True, (10, 10, 10))
  textpos = text.get_rect(centerx=125, y=50)
  screen.blit(screen, background)
  screen.blit(text, textpos)



def run_b_clock(b_time, background_color, screen):
  font = pygame.font.Font(None, 64)
  # black background/label -----------------------------
  b_background = pygame.draw.rect(screen, background_color, pygame.Rect((700, 0, 200, 200)))
  text = font.render('Black', True, (10, 10, 10))
  textpos = text.get_rect(centerx=775, y=10)
  screen.blit(text, textpos)
# black's time ------------------------------
  
  b_display_time = f'{round(b_time/60)-1}:{round(b_time%60)}'
  b_text = font.render(b_display_time, True, (10, 10, 10))
  b_textpos = text.get_rect(centerx=775, y=50)
  screen.blit(screen, b_background)
  screen.blit(b_text, b_textpos)


