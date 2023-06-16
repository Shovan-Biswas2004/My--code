#importhing the modules :
import pygame 
import os
from sys import exit
pygame.font.init()
pygame.init()

# display :
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('STAR WARS-PvP-')
CLOCK = pygame.time.Clock()

# SURFACE commands :
border= pygame.Rect(449, 0, 1, 600)
surface = pygame.Surface((900,600))
surface.fill('white')

# Fonts :
font = pygame.font.Font(None,40)
health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('Bauhaus 93', 40)

#Bullets :
first_bullet =[]
sec_bullet =[]
max_bullet = 3
bullet= 0
first_hit = pygame.USEREVENT +1
sec_hit = pygame.USEREVENT +2
first_health = 10
sec_health = 10
no = 0
def draw_winner(name):
    winner_text = winner_font.render(name, 1, 'white')
    screen.blit(winner_text,(900//2- winner_text.get_width()/2,600//2-winner_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def handle_bullets(first_bullet,sec_bullet,first_ship,sec_ship):
    for bullet in first_bullet:
        bullet.x+= 7
        #collide = pygame.Rect.colliderect(bullet)
        if sec_ship.colliderect(bullet):
            pygame.event.post(pygame.event.Event(sec_hit))
            first_bullet.remove(bullet)
            
        elif bullet.x > 900:
            first_bullet.remove(bullet)

    for bullet in sec_bullet:
        bullet.x-= 7
        if first_ship.colliderect(bullet):
            pygame.event.post(pygame.event.Event(first_hit))
            sec_bullet.remove(bullet)
       
        elif bullet.x <0 :
            sec_bullet.remove(bullet)
            
def draw_window(first_bullet,sec_bullet, first_health, sec_health ):
    for bullet in sec_bullet:
        pygame.draw.rect(screen,'red',bullet)
    for bullet in first_bullet:
        pygame.draw.rect(screen,'blue',bullet)

#texts :
text = font.render('Please press space to start',True,'white')
textm= text.get_rect(midbottom = (440,460))

# Rectangles :
background= pygame.image.load(os.path.join('python codes', 'files', 'background.webp'))
background_new = pygame.transform.scale(background,(900,600))
ship= pygame.image.load(os.path.join('python codes', 'files', 'ship.png'))
tie= pygame.image.load(os.path.join('python codes', 'files', 'tie.png'))
heart =  pygame.image.load(os.path.join('python codes', 'files', 'heart.png'))
heart_new = pygame.transform.scale(heart,(70,60))
heart_n = pygame.transform.scale(heart,(70,60))
ship_new= pygame.transform.scale(ship,(80,70))
first_ship = ship_new.get_rect(midbottom = (200,200))
tie_new= pygame.transform.rotate(pygame.transform.scale(tie,(150,90)), 270)
sec_ship = tie_new.get_rect(midbottom = (700,500))

count= 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(first_bullet)< max_bullet :
                bullet = pygame.Rect(first_ship.x + first_ship.width , first_ship.y + first_ship.height//2-2,10,5)
                first_bullet.append(bullet)

                
            if event.key == pygame.K_RCTRL and len(sec_bullet)< max_bullet:
                bullet = pygame.Rect(sec_ship.x , sec_ship.y + sec_ship.height//2-2,10,5)
               
                sec_bullet.append(bullet)
                
        if event.type == sec_hit:
             sec_health-=1
            

        if event.type == first_hit:
            first_health-=1
            
    winner = ""
    if first_health<=0:
        winner = "The SITH won"

    if sec_health<=0:
        winner = "The FORCE won"
    if winner!="":
        draw_winner(winner)
        break


    handle_bullets(first_bullet,sec_bullet,first_ship,sec_ship)
    screen.blit(surface,(0,0))
    pygame.draw.rect(screen,'black',border)
    screen.blit(background_new,(0,0))
    screen.blit(text,textm)
   
    screen.blit(ship_new,first_ship)
    screen.blit(tie_new,sec_ship)
    enter = pygame.key.get_pressed()
    if enter[pygame.K_SPACE]:
        no=1
        
        
    if no==1:
        
        score1 = health_font.render("     : "+ str(first_health), False , 'white')
        score2 = health_font.render("     : "+ str(sec_health), False , 'white')
        screen.blit(heart_new ,(10,20))
        screen.blit(heart_n,(900-score2.get_width()-20,20))
        screen.blit(score1,(20,20))
        screen.blit(score2,(900-score2.get_width()-10,20))
        textm.y+=5      
        draw_window(first_bullet,sec_bullet, first_health,sec_health)
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
     
    CLOCK.tick(60)
    pygame.display.update()
              
            

    
