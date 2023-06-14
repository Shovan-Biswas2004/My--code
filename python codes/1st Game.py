import pygame
import os
from sys import exit
pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('STAR WARS-PvP-')
CLOCK = pygame.time.Clock()
no = 0
border= pygame.Rect(449, 0, 1, 600)
surface = pygame.Surface((900,600))
surface.fill('white')
font = pygame.font.Font(None,40)

text = font.render('Please press space to start',True,'white')

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
    screen.blit(text,(250,450))
    pygame.draw.rect(screen,'black',border)
    screen.blit(ship_new,first_ship)
    screen.blit(tie_new,sec_ship)
    enter = pygame.key.get_pressed()
    if enter[pygame.K_SPACE]:
        no=1
    if no==1:
              
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and sec_ship.y>-40:
            sec_ship.y-=3
        if keys[pygame.K_DOWN] and sec_ship.y<480 :
            sec_ship.y+=3
        if keys[pygame.K_LEFT] and sec_ship.x>border.x:
            sec_ship.x-=3
        if keys[pygame.K_RIGHT] and sec_ship.x<810:
            sec_ship.x+=3
        key = pygame.key.get_pressed()   
        if key[pygame.K_w] and first_ship.y>-8:
            first_ship.y-=3
        if key[pygame.K_s] and first_ship.y<530:
            first_ship.y+=3
        if key[pygame.K_a] and first_ship.x>0:
            first_ship.x-=3
        if key[pygame.K_d] and first_ship.x<365:
            first_ship.x+=3
    print(border)      
    CLOCK.tick(60)
    pygame.display.update()
              
            

    
