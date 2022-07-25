import math
import random

class Player:

    def __init__(self, letter):
        self.letter = letter
        # the letter is x or o

    # we want all players to get their next move
    def get_move(self, game):
        pass # base player class

# here we are going to use inheritance to create a \
# random computer player and a human computer player that

class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            # checking if value if valid by casting it into an integer
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # valid value obtained
            except ValueError:
                print("Invalid value, try again.")
        return val