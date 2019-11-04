# the state is an array with the length of 32, each value being between 0-4
# 0 - empty space
# 1 - black man
# 2 - white man
# 3 - black king
# 4 - white king

# so effectively, black pieces are always odd, white pieces are always even
state = [0 for _ in range(32)]


def new_state():
    for i in range(32):
        if i < 12:
            state[i] = 1
        elif i >= 20:
            state[i] = 2
        else:
            state[i] = 0


# returns true or false depending on if the move was successful or not
def make_move(pos, new_pos):
    pos -= 1
    new_pos -= 1

    if state[pos] == 0:
        print("the piece you want to move isn't in that spot")
        return False

    if state[new_pos] is not 0:
        print("the spot you want to move to has an occupying piece")
        return False

    if state[pos] is not 0 and state[new_pos] == 0:
        if state[pos] % 1 == 0: # black piece
            if (new_pos )




def print_board():
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


def start():
    new_state()
    print_board()


start()
