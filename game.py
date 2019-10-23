from enum import Enum


class Color(Enum):
    WHITE = 'white'
    BLACK = 'black'


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class Tile:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    def __repr__(self):
        if (self.x + self.y) % 2 == 0:
            return 'O'
        else:
            return 'X'


class Piece:
    def __init__(self, color, tile, king=False):
        self.color = color
        self.tile = tile
        self.king = king

    def __repr__(self):
        if self.color == Color.WHITE:
            if not self.king:
                return '⛀'
            else:
                return '⛁'
        else:
            if not self.king:
                return '⛂'
            else:
                return '⛃'


class Board:
    def __init__(self):
        self.state = [[Tile(x, y) for x in range(8)] for y in range(8)]
        # here, we create an empty list of pointers to piece objects to be easily iterable
        self.whites = []
        self.blacks = []

    def new_board(self):
        self.state = [[Tile(x, y) for x in range(8)] for y in range(8)]
        self.whites = []
        self.blacks = []

        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                tile = self.state[y][x]
                if (x + y) % 2 != 0:
                    if y <= 2:
                        piece = Piece(Color.WHITE, tile)  # create a pointer to our object
                        tile.piece = piece
                        self.whites.append(piece)  # store out pointer
                    elif y > 4:
                        piece = Piece(Color.BLACK, tile)
                        tile.piece = piece
                        self.blacks.append(piece)

    def print_board(self):
        for row in self.state:
            for tile in row:
                if tile.piece is not None:
                    print(tile.piece, end=', ')
                else:
                    print(tile, end=', ')
            print('\n', end='')


def start():
    board = Board()
    board.new_board()
    board.print_board()


start()
