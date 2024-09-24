win = False
b = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
sample = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
p1 = "X"
p2 = "O"


def arrprint(b):
    result = ''
    for i in range(len(b)):
        result += '['
        for n in range(len(b[i])):
            result += str(b[i][n])
            if n != 2:
                result += ' | '
        result += ']'
        if i != 2:
            result += '\n'
    print(result + '\n')

#the start() function has no parameters and will run at the
#beginning of the game to initialize which symbol a player has
def run():
    global win
    win = False
    global b
    b = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("Player 1 is X and Player 2 is O")
    print("This is a key for the different squares of the board:")
    arrprint(sample)
    while win == False:
        move(p1)
        if win == True:
            print(f'{p1} wins!')
            return
        if tie():
            print("It's a tie!")
            return
        move(p2)
        if win == True:
            print(f'{p2} wins!')
            return
        if tie():
            print("It's a tie!")
            return
   
def move(p):
    if p == p1:
        pos = input ("Player 1: Which square would you like to move? Please use lowercase letters \n")
    else:
        pos = input ("Player 2: Which square would you like to move? Please use lowercase letters \n")
    positions = {'a': (0, 0), 'b': (0, 1), 'c': (0, 2), 'd': (1, 0), 'e': (1, 1), 'f': (1, 2), 'g': (2, 0), 'h': (2, 1), 'i': (2, 2)}
   
    if pos in positions:
        row, col = positions[pos]
        if b[row][col] == ' ':
            b[row][col] = p
            print('This is your current board: ')
            arrprint(b)
            c_win(p)
        else:
            print("This square is taken up. Choose a different one.")
            move(p)
    else:
        print("Please choose a valid square")
        move(p)
       
def c_win(p):
    global win
    if b[0][0] == p and b[0][1] == p and b[0][2] == p:
        win = True
        print(f"Yay {p} won!")
    if b[1][0] == p and b[1][1] == p and b[1][2] == p:
        win = True
        print(f"Yay {p} won!")
    if b[2][0] == p and b[2][1] == p and b[2][2] == p:
        win = True
        print(f"Yay {p} won!")
    if b[0][0] == p and b[1][0] == p and b[2][0] == p:
        win = True
        print(f"Yay {p} won!")
    if b[0][1] == p and b[1][1] == p and b[2][1] == p:
        win = True
        print(f"Yay {p} won!")
    if b[0][2] == p and b[1][2] == p and b[2][2] == p:
        win = True
        print(f"Yay {p} won!")
    if b[0][0] == p and b[1][1] == p and b[2][2] == p:
        win = True
        print(f"Yay {p} won!")
    if b[2][0] == p and b[1][1] == p and b[0][2] == p:
        win = True
        print(f"Yay {p} won!")
       
def tie():
    for i in b:
        if ' ' in i:
            return False
    return True
           
run()