import pygame

background_color= (0,0,0)
screen_x=500
screem_y=500
screen = pygame.display.set_mode((500,500))

pygame.display.set_caption('space invaders')

pygame.display.flip()
running = True

x= 250
y= 490

ship_width=10
ship_height=10


velocity =0.2
bullets =[]
bullet_vel=10
bullet_rad=5
bullet_col=(255,255,255)
bullet_y=250

while running:
    #print(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()


    for bullet in bullets:
        print(('Bullet coordinate',bullet,bullet_y))

        if bullet_y <500 and bullet_y >0:
            print('bullet created')
            bullet_y += bullet_vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE]:
        #print('pressed bullet')
        if len(bullets) < 5:
            #print('circle drawn',round(x),round(y))
            bullets.append(pygame.draw.circle(screen,bullet_col,(round(x),round(y)),bullet_rad))

    if keys[pygame.K_LEFT] and x>0:
        x-= velocity
    if keys[pygame.K_RIGHT] and x<500-ship_width:
        x+= velocity
    if keys[pygame.K_UP] and y>0:
        y-=velocity
    if keys[pygame.K_DOWN] and y<500 -ship_height:
        y+=velocity

    
   
    screen.fill(background_color)
    pygame.draw.rect(screen,(255,0,0),(x,y,ship_width,ship_height))
    pygame.display.update()
pygame.quit()