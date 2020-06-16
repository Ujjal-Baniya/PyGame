#Basics Movements Boundaries and Jump

import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

isJump =True
jump = 10

x = 50
y = 40
height = 40
width = 60
vel = 50

screenwidth = 500
screenheight = 500
run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x>10:
        x -= vel
    if keys[pygame.K_RIGHT] and x<screenwidth-width-vel:
        x +=vel
        
    if not(isJump):
        if keys[pygame.K_UP] and y>vel:
            y -=vel
        if keys[pygame.K_DOWN] and y<screenheight-height-vel:
            y +=vel   

        if keys[pygame.K_SPACE]:
            isJump= True
    else:
        if jump>= -10:
            neg = 1
            if jump<0:
                neg=-1
            y -= (jump**2) * 0.5 * neg
            jump -=1
        else:
            isJump = False
            jump= 10
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()