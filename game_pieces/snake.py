import pygame

class Snake:
    # class attributes
    color = (0,255,0)
    # construct instance attributes
    def __init__(self,game_size,snake_size,move_speed,x=1000,y=1000,direction='none',history=[],counter=0,start_eraser=False,delay=False):
        self.game_size = game_size
        self.snake_size = snake_size
        self.gameDisplay = pygame.display.set_mode((game_size,game_size))
        self.x = x
        self.y = y
        self.direction = direction
        self.history = [[x,y]]
        self.counter = counter
        self.start_eraser = start_eraser
        self.move_speed = move_speed
        self.delay = delay

    # public methods
    def ate_apple(self):
        self.delay = True

    # adds current position into memory
    def update_history(self):
        if self.direction != 'none':
            self.history.append([self.x, self.y])
    
    # pops the first element from memory, delay attribute utilized when snake eats apple
    def erase_history(self):
        if self.delay == False:
            self.history.pop(0)
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= (self.snake_size / self.move_speed):
                self.delay = False

    # not utilied yet
    def kill(self):
        pass

    # draws the snake
    def draw(self):
        pygame.draw.rect(self.gameDisplay,self.color,[self.x,self.y,self.snake_size,self.snake_size])

    # changes direction of the snake
    def change_direction(self,key):
        if (key == pygame.K_UP) and (self.x % self.snake_size == 0):
            self.direction = 'up'
        elif (key== pygame.K_DOWN) and (self.x % self.snake_size == 0):
            self.direction = 'down'
        elif (key == pygame.K_LEFT) and (self.y % self.snake_size == 0):
            self.direction = 'left'
        elif (key == pygame.K_RIGHT) and (self.y % self.snake_size == 0):
            self.direction = 'right'

    #moves the snake in the current direction, does not do anything until a key is initially pressed
    def slither(self):
        if self.direction == 'none':
            pass
        else:
            if self.direction == 'up':
                self.y = self.y - self.move_speed
            elif self.direction == 'down':
                self.y = self.y + self.move_speed
            elif self.direction == 'left':
                self.x = self.x - self.move_speed
            elif self.direction == 'right':
                self.x = self.x + self.move_speed
            self.check_for_eraser_start()


    def check_for_eraser_start(self):
        if self.start_eraser == True:
            pass
        else:
            if (self.direction != 'none') and (self.x % 50 == 0) and (self.y % 50 == 0): # if the snake is moving and has moved an entire space
                self.start_eraser = True

    # checks the snake for collision
    def check_collision(self):
        if self.start_eraser == True:
            # checks snake for collision with itself
            for i in self.history:
                if self.x == i[0] and self.y == i[1]:
                    self.kill()
                    return True
            # checks to see if snake has moved out of bounds
            if ((self.x < 0) or (self.x > self.game_size - self.snake_size)) or ((self.y < 0) or (self.y > self.game_size - self.snake_size)):
                self.kill()
                return True
        


    