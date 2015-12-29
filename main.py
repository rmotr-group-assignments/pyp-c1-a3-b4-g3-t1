from board import Board
from collections import namedtuple
from player import Player

def intro():
    print "Welcome to tic tac toe"
    print "Each player will have a turn to place their mark in one"
    print "of the empty spaces on the board"
    print "\nLet the game begin!\n"

def game():
    player_1 = Player(name=raw_input("Player 1 enter your name: "), mark="X")
    player_2 = Player(name=raw_input("Player 2 enter your name: "), mark="O")
    board = Board()
    while not board.tie_exists():
        # business logic. have each player take their turn switching back and forth
    else:
        print "{} and {} tied!".format(player_1.name, player_2.name)
    print "Thanks for playing!"

if __name__ == '__main__':
    intro()
    game()
