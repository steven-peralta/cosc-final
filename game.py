# the state is an array with the length of 32, each value being between 0-4
# -1    - white space
# 0     - empty space
# 1     - black man
# 2     - white man
# 3     - black king
# 4     - white king
# so effectively, black pieces are always odd, white pieces are always even

# board states are immutable, this ensure that we can't commit new states without making sure
# the board is in a legal state


def new_state():
    state = [[-1 for _ in range(8)] for _ in range(8)]  # 2d array of 8x8
    for y in range(len(state)):
        for x in range((y + 1) % 2, len(state[y]), 2):
            if y <= 2:
                state[y][x] = 1
            elif y >= 5:
                state[y][x] = 2
            else:
                state[y][x] = 0

    return tuple(state)


def available_moves(state, pos):
    moves = []
    x = pos[0]
    y = pos[1]
    piece = state[y][x]

    if piece == 1 or piece == 2:
        y_vec = 1 if piece == 1 else -1
        enemy = (2, 4) if piece == 1 else (1, 3)

        for x_dir in range(-1, 2, 2):
            try:
                print("y: {} x: {}".format(y+y_vec, x+x_dir))
                sel = state[y + y_vec][x + x_dir]
                if sel == 0:
                    moves.append((x + x_dir, y + y_vec))
                elif sel in enemy:  # if there is a white piece
                    try:
                        if state[y + (y_vec * 2)][x + (x_dir * 2)] == 0:
                            moves.append((x + x_dir, y + y_vec))
                    except IndexError:
                        pass
            except IndexError:
                pass

    return tuple(moves)


# returns the new state if the move was successful, returns False if it was not
def make_move(state, player, pos, new_pos):
    state = list(state)


# checks the board for winning conditions after every move
# returns 0 if no one has won yet
# returns 1 if black player has won
# returns 2 if white player has won
#
def check_board(state):
    return True


def print_board(state):
    str_builder = ''

    for y in state:
        for x in y:
            if x == -1:
                str_builder += '-'
            else:
                str_builder += str(x)
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
    print(available_moves(history[-1], prompt(current_player)))
    # while check_board(history[-1]):
    #    position_input = prompt(current_player)
    #    print(available_moves(history[-1], position_input[0]))
    #    """
    #    move = make_move(history[-1], int(current_player), position_input[0], position_input[1])
    #    if not move:
    #        continue
    #    else:
    #        history.append(move)
    #        print_board(history[-1])
    #        current_player = not current_player
    #        """


start()
