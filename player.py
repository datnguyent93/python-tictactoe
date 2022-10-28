import math
import random

class Player:
    # Constructor
    def __init__(self, letter):
        # x or o
        self.letter = letter
    
    # next move
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        # super is function to call inherited function
        super().__init__(letter)
        
    def get_move(self, game):
        pass
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        pass
