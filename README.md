# pong
#projekt z programowania

import pygame, sys

pygame.init()

#rozmiary ekranu
display = pygame.display.set_mode(800,400)

def core: 

  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break 
  
