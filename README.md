# pong
#projekt z programowania

import pygame, sys

pygame.init()
zegar = pygame.time.Clock()
#rozmiary ekranu
width=800
height=400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("pong")
def core():
    zegar=pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.display.flip()
    zegar.tick(25)
