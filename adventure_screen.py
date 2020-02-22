import pygame

#initiazile the pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((1200, 1000))

#title and icon
pygame.display.set_caption("Adventure")
icon = pygame.image.load("trees.png")
pygame.display.set_icon(icon)

#Player
playerimg = pygame.image.load("character_standingbig.png")
playerx =
playery = 0

def player():
    screen.blit(playerimg, [playerx, playery])

#Game loop
running = True
while running:

    # rgb colour
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #call player function
    player()
    pygame.display.update()