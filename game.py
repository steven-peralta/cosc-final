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
    enemy = (2, 4) if piece == 1 else (1, 3)  # tuple of piece states that are an enemy to our selected piece

    if piece == 1 or piece == 2:  # if a piece is a pawn (not a king)
        y_vec = 1 if piece == 1 else -1  # black pieces must move downwards (+1 on the y variable), otherwise move
        # upwards (-1 on the y variable)
        # for ex, if our piece is a black piece then our enemies are (2, 4) piece states
        # if pos is plusone:
        #    for x_dir in range(-1, 2, 2):
        #        for y_dir in range(-1, 2, 2):
        #            try:
        #                sel = state[y + y_dir][x + x_dir]
        #                if
        # else:
        for x_dir in range(-1, 2, 2):
            try:
                # since python indices can be negative, we want to prevent negative indices being pushed
                # to our available moveset
                if x + x_dir < 0:
                    raise IndexError

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
    elif piece == 3 or piece == 4:
        for x_dir in range(-1, 2, 2):
            for y_dir in range(-1, 2, 2):
                if x + x_dir < 0 or y + y_dir < 0:
                    raise IndexError

                try:
                    sel = state[y + y_dir][x + x_dir]
                    if sel == 0:
                        moves.append((x + x_dir, y + y_dir))
                    elif sel in enemy:
                        try:
                            if state[y + (y_dir * 2)][x + (x_dir * 2)] == 0:
                                moves.append((x + x_dir, y + y_dir))
                        except IndexError:
                            pass
                except IndexError:
                    pass

    return tuple(moves)


# returns the new state if the move was successful, returns False if it was not
def make_move(state, computer, pos, new_pos):
    if state[pos[1]][pos[0]] not in (1, 2, 3, 4):
        print("That's not a piece you can move")
        return False

    state = list(state)
    enemies = (1, 3) if computer else (2, 4)
    friendlies = (2, 4) if computer else (1, 3)
    piece = state[pos[1]][pos[0]]
    target = state[new_pos[1]][new_pos[0]]

    if piece not in friendlies:
        print("That's not a piece you can move")
        return False

    if new_pos in available_moves(state, pos):
        if target in enemies:
            state[new_pos[1]][new_pos[0]] = 0
            # oh fuck we fucked something up here
            state[new_pos[1]][new_pos[0]]

# checks the board for winning conditions after every move
# returns 0 if no one has won yet
# returns 1 if black player has won
# returns 2 if white player has won
#
def check_board(state):
    return True


def print_board(state):
    str_builder = []
    for y in range(len(state)):
        string = '   ==================================================\n'
        string += ' ' + str(y) + ' '
        for x in range(len(state[y])):
            piece = ' '
            if state[y][x] == 1:
                piece = '⛂'
            elif state[y][x] == 2:
                piece = '⛀'
            elif state[y][x] == 3:
                piece = '⛃'
            elif state[y][x] == 4:
                piece = '⛁'
            string += '|  ' + piece + '  '
            if x == len(state[y]) - 1:
                string += '|\n'
        str_builder.append(string)
    str_builder[-1] += """   ==================================================
       0     1     2     3     4     5     6     7
    """
    # '   +------+------+------+------+------+------+------+\n' \
    # ''
    for row in str_builder:
        print(row, end='')


def prompt(player, debug=False, history=None):
    if debug:
        cmd = input("Command: ").split(' ')
        if cmd[0] == 'print':
            print_board(history[-1])
        elif cmd[0] == 'moveto':
            current_state = list(history[-1])
            sel = current_state[int(cmd[2])][int(cmd[1])]
            current_state[int(cmd[4])][int(cmd[3])] = sel
            current_state[int(cmd[2])][int(cmd[1])] = 0

            print_board(current_state)
        elif cmd[0] == 'histlen':
            print("{} previous board states have been saved".format(len(history)))
        elif cmd[0] == 'view':
            print_board(history[cmd[1]])
        elif cmd[0] == 'avail':
            moves = {}  # piece pos -> tuple of available moves
            state = history[-1]
            for y in range(len(state)):
                for x in range(len(state[y])):
                    moves[(x, y)] = available_moves(state, (x, y))
            for key in moves:
                if len(moves[key]) == 0:
                    continue
                print("{} -> {}".format(key, moves[key]))
    else:
        print('not impl')


def start():
    debug = True
    running = True
    # the current state is the right most element in the array
    computer = False  # false is player moves (black), true is computer moves (white)
    history = [new_state()]
    print_board(history[-1])
    while running:
        if debug:
            prompt(computer, debug, history)
        else:
            prompt(computer)
    # print(available_moves(history[-1], prompt(computer)))
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
