COL_MAP = {'A':0 'B':1, 'C':2}

class Board:
    def __init__(self):
        # holds the placed pieces
        self.board = [[" "] * 3] * 3
        # set of all the currently placed pieces
        self.marks = set()

    def mark(self, row, col, piece):
        # check if already place in board
        if (row, col) not in self.marks:
            self.marks.add((row, col))
            self.board[row - 1][ COL_MAP[col] ] = piece
        else:
            raise ValueError("place already marked")

    def show(self):
        print "  A B C"
        for r in xrange(3):
            row = self.board[r]
            print "{} {}|{}|{}".format(r, row[0], row[1], row[2])

    def tie_exists(self):
        return len(self.marks) == 9
