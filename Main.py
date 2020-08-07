import pygame
from game_pieces.apple import Apple
from game_pieces.snake import Snake

#==== immutable values ====
game_size = 2000
game_piece_size = 50
color_red = (255,0,0)
color_green = (0,255,0)
#==========================

# initialize pygame
pygame.init()

# set up canvas and label
gameDisplay = pygame.display.set_mode((game_size,game_size))
pygame.display.set_caption('Python Snake!')


''' Initialize Apple ================================================================='''
# declare apple as type class:Apple
apple = Apple(game_size, game_piece_size) #include immutable values in class declaration
apple.rand_pos() #randomize the position of the apple
# draws the apple
pygame.draw.rect(gameDisplay,color_red,[apple.x,apple.y,game_piece_size,game_piece_size])
''' =================================================================================='''

''' Initialize Snake ================================================================='''
# declare snake as type class:Snake
snake = Snake()
# draws the snake with length 0
pygame.draw.rect(gameDisplay,color_green,[snake.head_pos_x,snake.head_pos_y,game_piece_size,game_piece_size])
''' =================================================================================='''

crashed = False
# creates a while loop that contains the game instance
while not crashed:
    for event in pygame.event.get():
        # runs if x (to close window) has been pressed
        if event.type == pygame.QUIT:
            crashed = True
        
        # detects arrow keys and changes variable 'direction'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT:
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snake.direction = 'right'



    pygame.draw.rect(gameDisplay,color_green,[snake.head_pos_x,snake.head_pos_y,game_piece_size,game_piece_size])
    pygame.display.update()