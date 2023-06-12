import pygame
import os
from sys import exit
pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('1st Game YaY')
CLOCK = pygame.time.Clock()

screen.fill('cornflowerblue')
ship= pygame.image.load(os.path.join('python codes', 'files', 'ship.png'))
ship_new= pygame.transform.scale(ship,(80,70))
first_ship = ship_new.get_rect(midbottom = (200,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(ship_new,first_ship)      
    CLOCK.tick(60)
    pygame.display.update()
              
            

    
