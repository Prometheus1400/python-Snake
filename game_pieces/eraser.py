import pygame

class Eraser:
    #class attributes
    color = (0,0,0)
    # construct instance attributes
    def __init__(self,game_size,eraser_size):
        self.eraser_size = eraser_size
        self.gameDisplay = pygame.display.set_mode((game_size,game_size))

    def draw(self,snake_history):
        pygame.draw.rect(self.gameDisplay,self.color,[snake_history[0][0],snake_history[0][1],self.eraser_size,self.eraser_size])

    
