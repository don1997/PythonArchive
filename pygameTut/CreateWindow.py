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
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black')

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


    pygame.display.update()
    clock.tick(60)