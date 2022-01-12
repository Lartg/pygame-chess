import pygame

def run_clocks(w_time, b_time, background_color, screen):
  font = pygame.font.Font(None, 64)
# white background/label -----------------------------
  w_background = pygame.draw.rect(screen, background_color, pygame.Rect((0, 0, 200, 200)))
  w_text = font.render('White', True, (10, 10, 10))
  w_textpos = w_text.get_rect(centerx=125, y=10)
  screen.blit(w_text, w_textpos)
# white's time ------------------------------
  
  w_display_time = f'{round(w_time/60)-1}:{round(w_time%60)}'
  w_text = font.render(w_display_time, True, (10, 10, 10))
  w_textpos = w_text.get_rect(centerx=125, y=50)
  
  screen.blit(w_text, w_textpos)

# black background/label -----------------------------
  b_background = pygame.draw.rect(screen, background_color, pygame.Rect((651, 0, 249, 200)))
  b_text = font.render('Black', True, (10, 10, 10))
  b_textpos = b_text.get_rect(centerx=775, y=10)
  screen.blit(b_text, b_textpos)
# white's time ------------------------------
  
  b_display_time = f'{round(b_time/60)-1}:{round(b_time%60)}'
  b_text = font.render(b_display_time, True, (10, 10, 10))
  b_textpos = b_text.get_rect(centerx=775, y=50)
  # screen.blit(screen, b_background)
  screen.blit(b_text, b_textpos)







