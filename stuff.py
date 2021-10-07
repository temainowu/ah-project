import random

class Users:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
    #end def

    def show(self):
        print(f'{self.name} has won {self.score} games')
    #end def
#end class

loclist = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def sort(array):
    for i in range(1, len(array)):
        temp = array[i] #swap
        pos = i
        
        while pos > 0 and array[pos-1].score < temp.score:
            array[pos] = array[pos-1] #swap
            pos -= 1
        #end while

        array[pos] = temp #swap
    #end for
    return array
#end def

def readScore():
    scores = []
    file = open('Scores.txt','r')
    data = file.readlines()
    file.close()

    for line in data:
        user = line.split(",")
        scores.append(Users(user[0], int(user[1])))
    #end for

    scores = sort(scores)
    for i in scores:
        i.show()
    #end for
#end def

def playMove(): #currently random (probably fine)
    move = random.randint(0, 8)
    while loclist[0][move] or loclist[1][move]:
        move = random.randint(0, 8)
    #end while
    return move
#end def

def search(array, target):
    found = False
    pos = 0
    for i in range(1, len(array)):
        if array[i].name == target:
            found = True
            pos = i
        #end if
    #end for
    
    if found:
        return pos
    else:
        return None
    #end if
#end def

def addScore(name):
    scores = []
    file = open('Scores.txt','r')
    data = file.readlines()
    file.close()

    for line in data:
        user = line.split(",")
        scores.append(Users(user[0], int(user[1])))
    #end for

    location = search(scores, name)

    if location is None:
        scores.append(Users(name, 1))
    else:
        scores[location].score += 1
    #end if

    file = open('Scores.txt', 'w')
    file.truncate()
    for i in scores:
        file.write(f'{i.name},{i.score},\n')
    #end for
    file.close()
#end def

def gameOver(moveCount, name):
    winCombos = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1],
                 [1, 0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 1, 0, 1, 0, 1, 0, 0]]
    for j in range(len(winCombos)):
        if [x & y for x, y in zip(winCombos[j], loclist[0])] in winCombos:
            print('You won in', (moveCount+1)//2, 'moves')
            addScore(name)
            return True
        elif [x & y for x, y in zip(winCombos[j], loclist[1])] in winCombos:
            print('AI won in', (moveCount)//2, 'moves')
            return True
        #end if
    #end for
    
    if moveCount > 8:
        print('Draw')
        return True
    else:
        return False
    #end if
#end def

def show_board(board):
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])
#end def

def play():
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    symbol = ['X', 'O']
    print('Noughts and Crosses')
    show_board(board)

    name = input('Name: ')

    moveCount = 0
    while not gameOver(moveCount, name):
        move = moveCount&1 #%2
        if move:
            loc = playMove()
        else:
            loc = int(input('Enter move: '))-1
            while loclist[0][loc] or loclist[1][loc]:
                print('invalid move')
                loc = int(input('Enter move: '))-1
            #end while
        #end if
        board[loc] = symbol[move]
        loclist[move][loc] = 1
        show_board(board)
        moveCount += 1
    #end while
#end def

def main():
    if input('Play Game? (Y/N): ') == 'Y':
        play()
    elif input('View scores? (Y/N): ') == 'Y':
        readScore()
    #end if
#end main

main()
