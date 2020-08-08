import pygame
from game_pieces.apple  import Apple
from game_pieces.snake  import Snake
from game_pieces.eraser import Eraser

'''==== immutable values ===='''
game_size = 2000
game_piece_size = 50
move_speed = 5
color_red = (255,0,0)
color_green = (0,255,0)
color_black = (0,0,0)
'''=========================='''

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

''' Initialize Eraser ================================================================='''
# declare eraser as type class:Eraser
eraser = Eraser(game_piece_size)
eraser.add_to_history([snake.x,snake.y])
''' =================================================================================='''

crashed = False
last_key_pressed = None
# creates a while loop that contains the game instance
while not crashed:
    events = pygame.event.get()
    for event in events:
        # runs if x (to close window) has been pressed
        if event.type == pygame.QUIT:
            crashed = True
        # detects arrow keys and logs it in last_key_pressed
        if event.type == pygame.KEYDOWN:
            last_key_pressed = event.key
    # assigns direction change only if x or y pos is in multiples of game_piece_size  
    if (last_key_pressed == pygame.K_UP) and (snake.x % game_piece_size == 0):
        snake.direction = 'up'
    elif (last_key_pressed == pygame.K_DOWN) and (snake.x % game_piece_size == 0):
        snake.direction = 'down'
    elif (last_key_pressed == pygame.K_LEFT) and (snake.y % game_piece_size == 0):
        snake.direction = 'left'
    elif (last_key_pressed == pygame.K_RIGHT) and (snake.y % game_piece_size == 0):
        snake.direction = 'right'

    # moves snake in the current direction incrementally every iteration
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
    
    # detecting one movement and adding the position into erasers history
    if (snake.direction == 'none') or (snake.x == apple.x and snake.y == apple.y):
        pass
    else:
        if (snake.x % 50 == 0) or (snake.y % 50 == 0):
            pygame.draw.rect(gameDisplay,color_black,[eraser.get_position()[0],eraser.get_position()[1],game_piece_size,game_piece_size])
            eraser.add_to_history([snake.x,snake.y])

    # detect snake eating apple
    if (snake.x == apple.x) and (snake.y == apple.y):
        apple.rand_pos()
        eraser.index_back_one()
    
    #gameDisplay = pygame.display.set_mode((game_size,game_size))
    # update snake and apple position
    pygame.draw.rect(gameDisplay,color_red,[apple.x,apple.y,game_piece_size,game_piece_size])
    pygame.draw.rect(gameDisplay,color_green,[snake.x,snake.y,game_piece_size,game_piece_size])
    # update whole screen
    pygame.display.update()
    