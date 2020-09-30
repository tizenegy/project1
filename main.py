# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and se
import random

state = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
player = 1
moves = 0


def print_board():
    print("| " + state[0] + " | " + state[1] + " | " + state[2] + " |")
    print("| " + state[3] + " | " + state[4] + " | " + state[5] + " |")
    print("| " + state[6] + " | " + state[7] + " | " + state[8] + " |")
    print("")


def make_move(plyr):
    num = 0
    if plyr == 2:
        num = ki_player()
        mark = "O"
        plyr = 1
    else:
        while not 0 < num < 10:
            try:
                num = int(input("Choose box (1-9):"))
            except ValueError:
                num = 0
            except IndexError:
                num = 0
        mark = "X"
        plyr = 2

    state[num - 1] = mark
    print_board()
    return plyr


def check_if_won():
    won = False
    if state[0] == state[3] == state[6]:
        won = True
    elif state[1] == state[4] == state[7]:
        won = True
    elif state[2] == state[5] == state[8]:
        won = True
    elif state[0] == state[1] == state[2]:
        won = True
    elif state[3] == state[4] == state[5]:
        won = True
    elif state[6] == state[7] == state[8]:
        won = True
    elif state[0] == state[4] == state[8]:
        won = True
    elif state[2] == state[4] == state[6]:
        won = True
    return won


def ki_player():
    num = 0
    available = []
    for box in state:
        if box != "X" and box != "O":
            available.append(box)
    if "5" in available:
        num = 5
    else:
        num = int(random.choice(available))
    print("computer chooses #"+str(num))

    #    hypo = []
    # for n in available:
    #     hypo = state
    #     if plyr == 1:
    #         move = "X"
    #     else:
    #         move = "O"
    #     hypo[num - 1] = move
    #     threat = check_hypo(hypo)
    return num


# def check_hypo(hy):
#     threat = False
#     if hy[0] == hy[3] == hy[6]:
#         won = True
#     elif hy[1] == hy[4] == hy[7]:
#         won = True
#     elif hy[2] == hy[5] == hy[8]:
    #     won = True
    # elif hy[0] == hy[1] == hy[2]:
    #     won = True
    # elif hy[3] == hy[4] == hy[5]:
    #     won = True
    # elif hy[6] == hy[7] == hy[8]:
    #     won = True
    # elif hy[0] == hy[4] == hy[8]:
    #     won = True
    # elif hy[2] == hy[4] == hy[6]:
    #     threat = True


if __name__ == '__main__':
    print_board()
    while not check_if_won() and moves < 9:
        player = make_move(player)
        moves = moves + 1
    if moves == 9:
        print("draw")
    else:
        print("congrats")
