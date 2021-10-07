import random
from typing import Optional


class User:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
    # end def

    def show(self) -> None:
        print(f'{self.name} has won {self.score} games')
    # end def
# end class


loclist = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def sort(array: "list[User]") -> None:
    for i in range(1, len(array)):
        temp = array[i]  # swap
        pos = i

        while pos > 0 and array[pos-1].score < temp.score:
            array[pos] = array[pos-1]  # swap
            pos -= 1
        # end while

        array[pos] = temp  # swap
    # end for
# end def


def parse_line(line: "list[str]") -> "User":
    name, score = line
    return User(name, int(score))


def read_score() -> None:
    scores = []
    file = open('Scores.txt', 'r')
    data = file.readlines()
    file.close()

    for line in data:
        user = parse_line(line.split(","))
        scores.append(user)
    # end for

    sort(scores)
    for i in scores:
        i.show()
    # end for
# end def


def play_move() -> int:
    # currently random (probably fine)
    move = random.randint(0, 8)
    while loclist[0][move] or loclist[1][move]:
        move = random.randint(0, 8)
    # end while
    return move
# end def


def search(array: "list[User]", target: "str") -> "Optional[int]":
    found = False
    pos = 0
    for i in range(1, len(array)):
        if array[i].name == target:
            found = True
            pos = i
        # end if
    # end for

    if found:
        return pos
    else:
        return None
    # end if
# end def


def add_score(name: str) -> None:
    scores = []
    file = open('Scores.txt', 'r')
    data = file.readlines()
    file.close()

    for line in data:
        user = line.split(",")
        scores.append(User(user[0], int(user[1])))
    # end for

    location = search(scores, name)

    if location is None:
        scores.append(User(name, 1))
    else:
        scores[location].score += 1
    # end if

    file = open('Scores.txt', 'w')
    file.truncate()
    for i in scores:
        file.write(f'{i.name},{i.score},\n')
    # end for
    file.close()
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
    ]
    for j in range(len(win_combos)):
        if [x & y for x, y in zip(win_combos[j], loclist[0])] in win_combos:
            print(f'You won in {(move_count+1)//2} moves')
            add_score(name)
            return True
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


def play() -> None:
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    symbol = ['X', 'O']
    print('Noughts and Crosses')
    show_board(board)

    name = input('Name: ')

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
    if input('Play Game? (Y/N): ') == 'Y':
        play()
    elif input('View scores? (Y/N): ') == 'Y':
        read_score()
    # end if
# end main


if __name__ == '__main__':
    main()
# end if
