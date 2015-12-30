from board import Board
from player import Player


def intro():
    """Display the intro message"""
    print "Welcome to tic tac toe"
    print "Each player will have a turn to place their mark in one"
    print "of the empty spaces on the board"
    print "\nLet the game begin!\n"


def game():
    """Play a new game"""
    player_1 = Player(name=raw_input("Player 1 enter your name: "), mark="X")
    player_2 = Player(name=raw_input("Player 2 enter your name: "), mark="O")
    players = (player_1, player_2)
    p = 0
    board = Board()
    # game loop
    while not board.tie_exists():
        # Have each player take their turn switching back and forth
        try:
            curr_player = players[p % 2]
            print "It is your turn {player}!".format(player=curr_player.name)
            board.show()
            raw_next_mark = raw_input("Where would you like to place your " +
                                      "next piece? ").upper()
            row, col = int(raw_next_mark[1]), raw_next_mark[0]
            piece = curr_player.mark
            board.mark(row, col, piece)
            if board.has_win(row, col, piece):
                print "{player} won!!".format(player=curr_player.name)
                break
            p += 1
        except ValueError:
            print "{} your piece <{}> was invalid".format(curr_player.name,
                                                          raw_next_mark)
    else:
        print "{} and {} tied!".format(player_1.name, player_2.name)
    board.show()
    print "Thanks for playing!"

if __name__ == '__main__':
    intro()
    game()
