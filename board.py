# BOARD CONSTANTS
WIDTH = 3
PADDING = WIDTH - 1
PADDED_WIDTH = WIDTH + 2 * PADDING

COL_MAP = {'A':0, 'B':1, 'C':2}

class Board:
    def __init__(self):
        # 3x3 grid w/ 2 cells of padding each side
        # padding prevents the has_win routine from having to check for out
        # of bounds pieces
        self.board = []
        for row in range(PADDED_WIDTH):
            self.board.append([" "] * PADDED_WIDTH)
        self.marks = set()

    def valid_input(self, row, col):
        """ Returns True if row and col are valid values"""
        return ((row, col) not in self.marks and
               row <= WIDTH and row > 0 and
               col in COL_MAP)

    def mark(self, row, col, piece):
        """
        Place a piece on the board at position ROW-COL

        raises a ValueError if row or column is invalid
        """
        if self.valid_input(row, col):
            self.marks.add((row, col))
            self.place_at(row - 1, COL_MAP[col], piece)
        else:
            raise ValueError("invalid row and column supplied: row={}, col={}"
                             .format(row, col))

    def piece_at(self, row, col):
        """Get the piece at the zero indexed row and column"""
        return self.board[row + PADDING][col + PADDING]

    def place_at(self, row, col, piece):
        """Place the piece at the zero indexed row and column"""
        self.board[row + PADDING][col + PADDING] = piece

    def has_win(self, r, c, piece):
        """
        Check if the last piece added at (r,c) creates a winning state
        """
        row = r - 1
        col = COL_MAP[c]
        cnt = 0

        # check vertical
        for dr in range(-1 * PADDING, PADDING):
            cnt = cnt + 1 if self.piece_at(row + dr, col) == piece else cnt
        if cnt == WIDTH:
            return True
        else:
            cnt = 0
        # check horizontal
        for dc in range(-1 * PADDING, PADDING):
            cnt = cnt + 1 if self.piece_at(row, col + dc) == piece else cnt
        if cnt == WIDTH:
            return True
        else:
            cnt = 0
        # check diagonal rightdown
        for drc in range(-1 * PADDING, PADDING):
            cnt = cnt + 1 if self.piece_at(row + drc, col + drc) == piece else cnt
        if cnt == WIDTH:
            return True
        else:
            cnt = 0
        # check diagonal rightup
        for drc in range(-1 * PADDING, PADDING):
            cnt = cnt + 1 if self.piece_at(row - drc, col + drc) == piece else cnt
        if cnt == WIDTH:
            return True

        return False

    def show(self):
        """Print the board"""
        print "  A B C"
        for row in xrange(0, WIDTH):
            print "{} {}|{}|{}".format(row + 1, self.piece_at(row, 0),
                                       self.piece_at(row, 1),
                                       self.piece_at(row, 2))

    def tie_exists(self):
        """Returns true if a tie exists on this board"""
        return len(self.marks) == 9
