import random as ran

class Apple:
    # class attributes N/A

    # instance attributes
    def __innit__(self, x=0, y=0):
        self.x = x
        self.y = y
    '''def __str__(self):
        return f"{self.x} {self.y}"
    '''
    # public class methods
    # changes apples positions to a random location on the board
    def rand_app_pos(game_size,piece_width):
        # value of game_size divided by width of game piece (50)
        max_rand_int = game_size / piece_width

        # assign x and y a random value between 1 and (length of game / 50)
        x = ran.randint(1,max_rand_int+1)
        y = ran.randint(1,max_rand_int+1)

        # get x and y positions in terms of the grid factor 50 (intervals of 50)
        self.x = (game_size % x) * piece_width
        self.y = (game_size % y) * piece_width

        return x,y