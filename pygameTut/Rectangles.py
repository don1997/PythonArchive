import pygame
from sys import exit



pygame.init()

#sets screen size
screen = pygame.display.set_mode((800, 400))

#screen title
pygame.display.set_caption("Runner")

#fps clock
clock = pygame.time.Clock()
#game now has font

#init font
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

#init grass, surface, and text
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render('My Game', False, 'Black')
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))


#Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Draws stuff to the screen
    screen.blit(sky_surface,(0,0))

    screen.blit(ground_surface,(0,300))
    
    screen.blit(text_surface,(300,50))
    #updates x pos of snail by + 1

    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,250))
    player_rect.left += 1
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    #fps of game
    clock.tick(60)