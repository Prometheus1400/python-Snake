import random as r

class Apple:
    # class attributes N/A

    # instance attributes
    def __innit__(self, x_pos=0, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
    def __str__(self):
        return f"{self.x} {self.y}"
        
    # public class methods
    # changes apples positions to a random location on the board
    def rand_app_pos(game_size,piece_width):
        # value of game_size divided by width of game piece (50)
        max_rand_int = game_size / piece_width

        # assign x and y a random value between 1 and (length of game / 50)
        x = r.randint(1,max_rand_int+1)
        y = r.randint(1,max_rand_int+1)

        # get x and y positions in terms of the grid factor 50 (intervals of 50)
        self.x = (game_size % x) * piece_width
        self.y = (game_size % y) * piece_width

        return x,y

    def read(self):
        print(   f"{self.x_pos}")