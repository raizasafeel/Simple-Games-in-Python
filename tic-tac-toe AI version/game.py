from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

"""
MINIMAX ALGORITHM:
- you are trying to maximise your win while your opponent is trying to 
minimize their loss.
- utility function: -1/0/1 * (number of empty spaces +1)
    - 1 for your win
    - -1 for opponent win
    - 0 for tie
"""

class TicTacToe:
    def __init__(self):
        self.board =  self.make_board()# we will use a single list t0 rep 3x3 board
        self.current_winner = None # keep track of current winner

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # the header goes like 0-3, 3-6, 6-9 and tells us which \
            # row we are at where 0, 1 , 2 first row; 3, 4, 5 second and so on
            print('|'+'|'.join(row)+'|')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc, tells us which number corresponds to which box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        '''
        # return [], a list of available moves
        moves = []
        for (i, x) in enumerate(self, board):
        # enumerate creates a list and assigns value 0, 1, .. to each
        # value from the list. eg. 'hi' -> [(0, h), (1, i)]
        # enumerate l1 = ['hello', 'world'] as enumerate(2, l1]
        # would go as [(2, 'hello'), (3, 'world')]
        # so here it would go as ['x','x','o'] -> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot = ' ': moves.append(i)
            return moves
        '''
        # or just do
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())
        # return self.board.count(' ')

    def make_move(self, square, letter):
        # if the move is valid then return true else false
        if self.board[square] == ' ':
            self.board[square] = letter
            # check for winner
            if self.winner(square, letter):
                self.current_winner =  letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3 # checking row [specifies which row we are on]
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # check column if above was false
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        # check diagonal
        # for this we have to place a move to a diagonal sq
        # i.e. [0,2,4,6,8] even number
        if square % 2 == 0:
        # first diagonal [0,4,8] or second [2,4,6]
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal1]):
                return True
            if all([spot == letter for spot in diagonal2]):
                return True
        return False




    def play(game, x_player, o_player, print_game = True):
        # return winner if there is one else return none which is tie
        if print_game:
            game.print_board_nums() # see which number correspond to which spot

        letter = 'x' # starting letter
        # iterate while the game has empty squares
        while game.empty_squares():
            if letter == 'o':
                square = o_player.get_move(game)
            if letter == 'x':
                square = x_player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(letter + f' makes a move to square {square}')
                    game.print_board()
                    print('') # just an empty line

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter


                 # next move/ switch letter
                '''if letter == 'x': letter = 'o'
                else letter = 'x'
                can be re written as '''
                letter = 'o' if letter == 'x' else 'x'

            # adding a pause
            if print_game:
                time.sleep(0.8)


        if print_game:
            print("It's a tie.")

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = HumanPlayer('x')
        o_player = GeniusComputerPlayer('o')
        t = TicTacToe()
        result = t.play( x_player, o_player)
        if result == 'x':
            x_wins += 1
        elif result == 'o':
            o_wins += 1
        else: ties += 1

    print(f"x wins: {x_wins} o wins: {o_wins} ties: {ties}")

