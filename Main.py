import pygame
from game_pieces.apple  import Apple
from game_pieces.snake  import Snake
from game_pieces.eraser import Eraser

'''==== gamerule values ===='''
game_size = 2000
game_piece_size = 50
move_speed = 2
'''=========================='''


# initialize pygame
pygame.init()
# set up canvas and label
gameDisplay = pygame.display.set_mode((game_size,game_size))
pygame.display.set_caption('Python Snake!')

''' Initialize Snake ================================================================='''
# declare snake as type class:Snake
snake = Snake(game_size, game_piece_size,move_speed)
# draws the snake with length 0
snake.draw()
''' =================================================================================='''

''' Initialize Apple ================================================================='''
# declare apple as type class:Apple
apple = Apple(game_size, game_piece_size) #include immutable values in class declaration
apple.rand_pos(snake.history) #randomize the position of the apple
# draws the apple
apple.draw()
''' =================================================================================='''

''' Initialize Eraser ================================================================'''
# declare eraser as type class:Eraser
eraser = Eraser(game_size,game_piece_size)
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
    snake.change_direction(last_key_pressed)
    # moves snake in the current direction incrementally every iteration
    snake.slither()
    if snake.check_collision() == True:
        crashed = True
    #updates the history of the body of the snake
    snake.update_history()

    # detect snake eating apple
    if (snake.x == apple.x) and (snake.y == apple.y):
        apple.rand_pos(snake.history)
        snake.ate_apple()
    if snake.start_eraser == True:
        eraser.draw(snake.history)
        snake.erase_history()
    #gameDisplay = pygame.display.set_mode((game_size,game_size))
    # update snake and apple position
    apple.draw()
    snake.draw()
    # update whole screen
    pygame.display.update()
