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

class GeniusComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9: # if all spaces available choose a random one
            square = random.choice(game.available_moves())
        else:
            # get square based off minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'o' if player == 'x' else 'x'

        if state.current_winner == other_player: # someone won
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.num_empty_squares(): # no empty squares
            return {'position': None, 'score': 0}

        if player == max_player :
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_moves in state.available_moves():
            # step 1: make a move and try a spot
            state.make_move(possible_moves, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # now we alternate players
            #step 3: undo the move
            state.board[possible_moves] = ' '
            state.current_winner = None
            sim_score['position'] = possible_moves
            # step 4: update the move if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score #replace best
            else: # but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best
        return best