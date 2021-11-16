import random
from typing import Optional
from User import User, read_score, increase_score
from server import do

loclist = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def play_move() -> int:
    move = random.randint(0, 8)
    while loclist[0][move] or loclist[1][move]:
        move = random.randint(0, 8)
    # end while
    return move
# end def

def game_over(move_count: int, name: str) -> bool:
    win_combos = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0]
    ] #list of winnig board states
    
    for j in range(len(win_combos)):
        #if the Xs on the board match a win condition in win_combos
        if [x & y for x, y in zip(win_combos[j], loclist[0])] in win_combos:
            print(f'You won in {(move_count+1)//2} moves')
            increase_score(name)
            return True
        #if the Os on the board match a win condition in win_combos
        elif [x & y for x, y in zip(win_combos[j], loclist[1])] in win_combos:
            print(f'AI won in {(move_count)//2} moves')
            return True
        # end if
    # end for

    if move_count > 8:
        print('Draw')
        return True
    else:
        return False
    # end if
# end def

def show_board(board: "list[str]") -> None:
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])
# end def

def play():
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    symbol = ['X', 'O']
    print('Noughts and Crosses')
    show_board(board)

    move_count = 0
    while not game_over(move_count, name):
        move = move_count & 1  # (same as doing move_count % 2)
        if move:
            loc = play_move()
        else:
            loc = int(input('Enter move: '))-1
            while loclist[0][loc] or loclist[1][loc]:
                print('invalid move')
                loc = int(input('Enter move: '))-1
            # end while
        # end if
        board[loc] = symbol[move]
        loclist[move][loc] = 1
        show_board(board)
        move_count += 1
    # end while
# end def

def main():
    if input('Play Game? (y/n): ') == 'y':
        play()
    elif input('View scores? (y/n): ') == 'y':
        read_score()
    # end if
# end main

if __name__ == '__main__':
    main()
# end if
