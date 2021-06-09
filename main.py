import pygame

# intialize the pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Hj250puzzle")
icon = pygame.image.load('motocross.png')
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # RGB - Red, Green, Blue
            screen.fill((0, 0, 0))
            pygame.display.update()







