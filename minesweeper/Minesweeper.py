# lets create a board object to represent minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here" or "render this game for this object"
class Board:
    def __int__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
    # lets create the board

    # initialise a set to keep track of which locations we've uncovered
    # we'll save (row, col) tuples into this set
    self.dug = set() # if we dig at 1,1 then self.dug = {(1,1)}

# play the game
def play(dim_size=10, num_bombs=10):
    # step 1: create the board and plant the bombs
    # step 2: show the user the board and ask them where they want to dig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if the location is next to a bomb, dig recursively
    #   until each square is atleast next to a bomb
    # step 4: reap step 2 and 3a/b until there are no more places to dig --> VICTORY
    pass

