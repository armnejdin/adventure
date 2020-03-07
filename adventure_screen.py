import pygame

#initiazile the pygame
pygame.init()

#creating the screens
player_screen = pygame.display.set_mode((1200, 950))
#mountains
background_screen = pygame.display.set_mode((1200,950))
mountain = pygame.image.load("mountain.png")


#title and icon
pygame.display.set_caption("Adventure")
icon = pygame.image.load("trees.png")
pygame.display.set_icon(icon)

#Player
playerimg = pygame.image.load("character_standingbig.png")
playerx = 400
playery = 400
playerx_change = 0
playery_change = 0

#player function
def player(x,y):
    player_screen.blit(playerimg, [x, y])

#Game loop
running = True
while running:

    # rgb colour
    player_screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     #if key pressed check if left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change -= 5
            if event.key == pygame.K_RIGHT:
                playerx_change += 5
            if event.key == pygame.K_UP:
                playery_change -= 5
            if event.key == pygame.K_DOWN:
                playery_change += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP :
                playerx_change = 0
                playery_change = 0



    #player movement
    playerx += playerx_change
    playery += playery_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 1000:
        playerx = 1000
    if playery <= 0:
        playery = 0
    elif playery >= 750:
        playery = 750

    # background
    player_screen.blit(mountain, [300, 400])

    #call player function
    player(playerx, playery)
    pygame.display.update()

