import pygame
from game_pieces.apple import Apple
from game_pieces.snake import Snake

#==== immutable values ====
game_size = 2000
game_piece_size = 50
#==========================

# initialize pygame
pygame.init()

# set up canvas and label
gameDisplay = pygame.display.set_mode((game_size,game_size))
pygame.display.set_caption('Python Snake!')

# get starting random position for Apple
apple = Apple()
apple.read()



#clock = pygame.time.Clock()

#pygame.draw.rect(gameDisplay,(255,255,255),[975,975,50,50])

crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)

    pygame.display.update()
    #clock.tick(60)