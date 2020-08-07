import random as r

class Apple:
    # class attributes N/A

    # instance attributes
    def __init__(self, game_size, piece_width, x=0, y=0):
        self.game_size = game_size
        self.piece_width = piece_width
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x} {self.y}"
        
    # public class methods
    # changes apples positions to a random location on the board
    def rand_pos(self):
        # value of game_size divided by width of game piece (50)
        max_rand_int = self.game_size / self.piece_width

        # assign x and y a random value between 1 and (length of game / 50)
        x = r.randint(1,max_rand_int+1)
        y = r.randint(1,max_rand_int+1)

        # get x and y positions in terms of the grid factor 50 (intervals of 50)
        self.x = x * self.piece_width
        self.y = y * self.piece_width