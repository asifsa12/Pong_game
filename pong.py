import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window 
screen_width = 1280
screen_height = 860
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles, will be empty until drawn 
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 10,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
  

#Color
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#Ball speed set
ball_speed_x = 7
ball_speed_y = 7 


while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    ball.x += ball_speed_x
    ball.y += ball_speed_y  

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_x *= -1   

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1    

    # Updating the window 
    pygame.display.flip()
    clock.tick (80)     
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    #changes
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))          

    



                   