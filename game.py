# the state is an array with the length of 32, each value being between 0-4
# 0 - empty space
# 1 - black man
# 2 - white man
# 3 - black king
# 4 - white king

# so effectively, black pieces are always odd, white pieces are always even

# board states are immutable, this ensure that we can't commit new states without making sure
# the board is in a legal state

# range(3, 32, 8), pieces that exist within these spaces may only move leftward if player is black, or rightward if
# player is white.

# [4::8], pieces that exist within these spaces may only move rightward if player is black, or leftward if player is
# white.


def new_state():
    state = [0 for _ in range(32)]  # initialize empty array of zeroes with size of 32
    for i in range(32):
        if i < 12:
            state[i] = 1
        elif i >= 20:
            state[i] = 2
        else:
            state[i] = 0
    return tuple(state)


def available_moves(state, pos):
    piece = state[pos]
    positions = []

    # down left
    x = pos
    step = 4
    while x not in range(4, 32, 8) and x not in range(28, 31):
        x += step
        if step == 4:
            step = 3
        else:
            step = 4
        positions.append(x)

    return tuple(positions)


# returns the new state if the move was successful, returns False if it was not
def make_move(state, player, pos, new_pos):
    state = list(state)
    pos -= 1
    new_pos -= 1

    # if player is black
    if player == 0:
        if state[pos] % 1 is not 0:
            print("That piece isn't yours.")
            return False

        kinged = True if state[pos] == 3 else False

        # this checks if the piece is on the rightmost side of the board (row 1, 3, 5, 7)
        # if it is, then it can only move left.
        if pos in range(3, 32, 8):

            # since the selected piece is on the rightmost side of the board,
            # there is only one space that we can move to, which is the space +4 spaces ahead of our current position
            # this makes sure the player's new position is the correct position
            if new_pos is not (pos + 4):
                print("invalid move")
                return False

            if state[new_pos] == 1:
                print("one of your pieces is already there.")
                return False

            elif state[new_pos] == 2:

                return False

            elif state[new_pos] == 0:
                state[new_pos] = state[pos]
                state[pos] = 0
                return tuple(state)



        # this checks if the piece is on the leftmost side of the board (row 2, 4, 6, 8)
        # if it is, then it can only move right.
        elif pos in range(4, 32, 8):
            print("piece is on the left most side of the board")

        # if the piece isn't on the left most or right most side of the board, it must be in the middle
        # therefore, it can move either left or right.
        else:
            print("piece is in middle of board")


# checks the board for winning conditions after every move
# returns 0 if no one has won yet
# returns 1 if black player has won
# returns 2 if white player has won
# if
def check_board(state):
    return True


def print_board(state):
    str_builder = ''
    itr = 0
    for row in range(8):
        for column in range(8):
            if row % 2 == 0:
                if column % 2 == 0:
                    str_builder += '-'
                else:
                    str_builder += str(state[itr])
                    itr += 1
            else:
                if column % 2 == 0:
                    str_builder += str(state[itr])
                    itr += 1
                else:
                    str_builder += '-'
        str_builder += '\n'

    print(str_builder)


def prompt(player):
    print("Player %s:" % ('Black' if player is False else 'White'))
    return tuple(list(map(lambda i: int(i), input("Enter the move you would to like to make: ").split(' ')))[0:2])


def start():
    # the current state is the right most element in the array
    current_player = False  # false is black, true is white
    history = [new_state()]
    print_board(history[-1])
    while check_board(history[-1]):
        position_input = prompt(current_player)
        print(available_moves(history[-1], position_input[0]))
        """
        move = make_move(history[-1], int(current_player), position_input[0], position_input[1])
        if not move:
            continue
        else:
            history.append(move)
            print_board(history[-1])
            current_player = not current_player
            """


start()
