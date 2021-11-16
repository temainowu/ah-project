USER_FILE = "UserData.txt"

class User:
    def __init__(self, name: str, score: int, question: str, answer_hash: str, password_hash: str) -> None:
        self.name = name
        self.score = score
        self.question = question
        self.answer_hash = answer_hash
        self.password_hash = password_hash
    # end def

    def show(self) -> None:
        print(f'{self.name} has won {self.score} games')
    # end def

    @classmethod
    def from_string(cls, string: str) -> 'User':
        name, score, question, answer_hash, password_hash = string.split(',')
        return cls(name, int(score), question, answer_hash, password_hash)
    # end def

    def to_string(self) -> str:
        return f'{self.name},{self.score},{self.question},{self.answer_hash},{self.password_hash}'
    # end def
# end class

def sort(array): #insertion sort list of User by score
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

def open_file():
    users = []
    file = open(USER_FILE, 'r')
    data = file.readlines()
    file.close()

    for line in data:
        users.append(User.from_string(line))
    # end for
    return users
    

def add_user(name, score, question, answer_hash, password_hash) -> None:
    users = open_file()

    if search(users, name):
        print()
    
    users.append(User(name, score, question, answer_hash, password_hash))
    sort(users)

    file = open(USER_FILE, 'w')
    for i in users:
        file.write(i.to_string())
    # end for
    file.close()
# end def

def read_score() -> None:
    users = open_file()
    for i in users:
        i.show()
    # end for
# end def

def search(array, target): #linear search list of User for target name
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

def increase_score(name):
    users = open_file()
    
    users[search(users, name)].score += 1
    sort(users)
    
    file = open(USER_FILE, 'w')
    for i in users:
        file.write(i.to_string())
    # end for
    file.close()
#end def
    
