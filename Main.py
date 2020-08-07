import pygame
from game_pieces.apple import Apple
from game_pieces.snake import Snake

#==== immutable values ====
game_size = 2000
game_piece_size = 50
move_speed = 2
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
pygame.draw.rect(gameDisplay,color_green,[snake.x,snake.y,game_piece_size,game_piece_size])
''' =================================================================================='''
crashed = False
last_key_pressed = None
# creates a while loop that contains the game instance
while not crashed:
    for event in pygame.event.get():
        # runs if x (to close window) has been pressed
        if event.type == pygame.QUIT:
            crashed = True
        
        # detects arrow keys and logs it in last_key_pressed
        if event.type == pygame.KEYDOWN:
            last_key_pressed = event.key
        
        if (last_key_pressed == pygame.K_UP) and (snake.y % 50 == 0):
            snake.direction = 'up'
        elif (last_key_pressed == pygame.K_DOWN) and (snake.y % 50 == 0):
            snake.direction = 'down'
        elif (last_key_pressed == pygame.K_LEFT) and (snake.x % 50 == 0):
            snake.direction = 'left'
        elif (last_key_pressed == pygame.K_RIGHT) and (snake.x % 50 == 0):
            snake.direction = 'right'

    if snake.direction == 'none':
        pass
    else:
        if snake.direction == 'up':
            snake.y = snake.y - move_speed
        elif snake.direction == 'down':
            snake.y = snake.y + move_speed
        elif snake.direction == 'left':
            snake.x = snake.x - move_speed
        elif snake.direction == 'right':
            snake.x = snake.x + move_speed
    # update snake position
    pygame.draw.rect(gameDisplay,color_green,[snake.x,snake.y,game_piece_size,game_piece_size])
    # update whole screen
    pygame.display.update()
    print(snake.x, snake.y)
    