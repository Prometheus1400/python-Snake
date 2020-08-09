import random as r
import pygame

class Apple:
    # class attributes N/A
    color = (255,0,0)
    # instance attributes
    def __init__(self, game_size, apple_size, x=0, y=0,freespace=False):
        self.game_size = game_size
        self.apple_size = apple_size
        self.x = x
        self.y = y
        self.gameDisplay = pygame.display.set_mode((game_size,game_size))
        self.freespace = freespace

        
    # public class methods
    # changes apples positions to a random location on the board
    def rand_pos(self,snake_history):
        # value of game_size divided by width of game piece (50)
        max_rand_int = self.game_size / self.apple_size
        
        # initialize freespace as false to trigger the while loop
        self.freespace = False
        while self.freespace == False:
            # assign x and y a random value between 1 and (length of game / 50)
            old_x = r.randint(0,max_rand_int)
            old_y = r.randint(0,max_rand_int)
            # get x and y positions in terms of the grid factor 50 (intervals of 50)
            new_x = old_x * self.apple_size
            new_y = old_y * self.apple_size

            # check and see if the apple is trying to place in a currently occupied square
            for i in snake_history:
                if (i[0] == new_x) and (i[1] == new_y):
                    self.freespace == False
                    break
                else:
                    self.freespace = True

        self.x = new_x
        self.y = new_y
        

    
    def draw(self):
        pygame.draw.rect(self.gameDisplay,self.color,[self.x,self.y,self.apple_size,self.apple_size])
