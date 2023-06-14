import pygame
import os
from sys import exit
pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('1st Game YaY')
CLOCK = pygame.time.Clock()

surface = pygame.Surface((900,600))
surface.fill('white')

background= pygame.image.load(os.path.join('python codes', 'files', 'background.webp'))
background_new = pygame.transform.scale(background,(900,600))
ship= pygame.image.load(os.path.join('python codes', 'files', 'ship.png'))
tie= pygame.image.load(os.path.join('python codes', 'files', 'tie.png'))
ship_new= pygame.transform.scale(ship,(80,70))
first_ship = ship_new.get_rect(midbottom = (200,200))
tie_new= pygame.transform.rotate(pygame.transform.scale(tie,(150,90)), 270)
sec_ship = tie_new.get_rect(midbottom = (700,500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(surface,(0,0))
    screen.blit(background_new,(0,0))
    
    screen.blit(ship_new,first_ship)
    screen.blit(tie_new,sec_ship)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sec_ship.y-=1
    elif keys[pygame.K_DOWN]:
        sec_ship.y+=1
    elif keys[pygame.K_LEFT]:
        sec_ship.x-=1
    elif keys[pygame.K_RIGHT]:
        sec_ship.x+=1
    key = pygame.key.get_pressed()   
    if key[pygame.K_w]:
        first_ship.y-=1
    elif key[pygame.K_s]:
        first_ship.y+=1
    elif key[pygame.K_a]:
        first_ship.x-=1
    elif key[pygame.K_d]:
        first_ship.x+=1
          
    CLOCK.tick(60)
    pygame.display.update()
              
            

    
