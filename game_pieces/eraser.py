class Eraser:
    # construct instance attributes
    def __init__(self,size,history=[],index=-1):
        self.history = history
        self.index = index
        self.size = size
    
    def add_to_history(self,position):
        self.history.append(position)

    def get_position(self):
        return self.history[self.index]

    def index_back_one(self):
        self.index = self.index - self.size
    
