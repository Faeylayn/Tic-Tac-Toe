
import random

def board_size():
    "Get the grid size from the Player."
    length = ""
    while not (length == "3" or length == "4"): 
        print "Would you like to play a grid of 3 or 4"
        print "Please enter 3 or 4 (a 3x3 Grid will play against 1 Opponent, a 4x4 will play against 2 opponents."
        length = raw_input()
    return length

def assign_letters(length):
    user_letter = ""
    while not (user_letter == "X" or user_letter == "O"): 
        print "Would you like to be X's or O's"
        user_letter = raw_input()
       
    if user_letter == "X":
        ai_letter = "O"
    if user_letter == "O":
        ai_letter = "X"
        
    return (user_letter, ai_letter)
        
def make_board(length):
    "Takes an integer and creates a list that length with a list of that length at each index."
    board = []
    for x in range(length):        
        board.append(list())
        for y in range(length):
            board[x].append(" ")
    return board
    
def make_grid(length):
    "Takes an integer and creates a list that length with a list of that length at each index, numbering each index space."
    grid = []
    z = 1
    for x in range(length):        
        grid.append(list())
        for y in range(length):
            grid[x].append(z)
            z += 1
    return grid

def print_board(board):
    "Print the board state. It is expected that board is a list of lists."
    length = len(board)
    for x in range(length):
        print '\n'
        print ' ',
        var = len(board[x])
        for y in range(var):
            print board[x][y],
            if y < (length - 1):
                print " I ",


def check_space(board, move):
    "Check if a space on the board is free."
    row = (move - 1) / len(board)
    space = (move - 1) % len(board[row])
    return board[row][space] == " "
        
def make_move(board, move, letter)
    row = (move) / len(board)
    space = (move) % len(board[row])
    board[row][space] = letter
    return board

def user_turn(board, letter):
    move = '40'
    while (move not in grid) or (check_space(board, int(move)) == False):
        print "Where would you like to move?"
        move = raw_input()
        
    return make_move(board, move, letter)
        
def win_check(board, letter):
    "This is not done yet."
    raise NotImplementedError
    return ((board[0] == letter and board[1] == letter and board[2] == letter) or
    (board[3] == letter and board[4] == letter and board[5] == letter) or
    (board[6] == letter and board[7] == letter and board[8] == letter) or
    (board[0] == letter and board[3] == letter and board[6] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[0] == letter and board[4] == letter and board[8] == letter) or
    (board[2] == letter and board[4] == letter and board[6] == letter))
    
def ai_check(board, letter)
    total = len(board) * len(board[1])

    for i in range(total):
        test = list(board)
        if check_space(test, i) == True:
            test[i] = letter
            if win_check(test, letter) == True:
                return i    
    return False

def ai_behavior(board, letter, turn):
    counter = turn    
    
    if check_space(board, ((len(board) ^ 2) / 2))
        return make_move(board, ((len(board) ^ 2) / 2), letter[turn])
    
    if len(board) == 4:
        ai_2 = ai_check(board, letter[counter])
        if ai_2 != False:
            return make_move(board, ai_2, letter[turn])
        counter == 0

    ai_1 = ai_check(board, letter[counter])
    if ai_1 != False:
        return make_move(board, ai_1, letter[turn])
    if counter == 0:
        counter == 1
    else 
        counter == 0:

    ai_p =  ai_check(board, letter[counter])
    if ai_p != False:
        return make_move(board, ai_p, letter[turn])
    
    
    while True:
        r = (random.random() * 2) - 1
        rand = ((len(board) ^ 2) / 2) + ((len(board) * r)
        if check_space(board, int(rand)) == True:
            return make_move(board, int(rand), letter[turn])
    
def board_full(board):
    "Check if the board has any playable spaces"
    total = len(board) * len(board[1])
    for f in range(total):
        if check_space(board, f) == True:
            return False
        
    return True
        
def first():
    return random.randint(0,1)
        
def another():
    answer = ''
    while not (answer == 'Y' or answer == 'N'):
        print 'Would you like to play another game? (Y/N)'
        answer = raw_input()
       
    if answer == 'Y':
        print 'OK! Game On!'
        return True
    else:
        print 'OK! Goodbye!'
        return False
 
def main():
        
    while True:

        length = board_size()
        
        letter = assign_letters()
        if length == 4
            letter.append('Z')
        print "Player is " + str(letter[0])
        
        board = make_board(length)
        grid = make_grid(length)
               
        print_board(grid)
        turn = first()
        
        if turn == 0:
            print 'The Player is first'
        else:
            print 'The Computer is first'
        
        game_on = True
        
        while game_on:
            if turn == 0:
                print_board(board)
                user_turn(board, letter)
                if win_check(board, letter[0]) == True:
                    print_board(board)
                    print 'You win! Congrats!'
                    game_on = False
                else:
                    if board_full(board) == True:
                        print_board(board)
                        print 'The Game is a tie!'
                        game_on = False
                    else:
                        turn = 1
            if turn == 1:
                ai_behavior(board, letter, turn)
                if win_check(board, letter[1]) == True:
                    print_board(board)
                    print 'You Lose! Sorry!'
                    game_on = False
                else:
                    if board_full(board) == True:
                        print_board(board)
                        print 'The Game is a tie!'
                        game_on = False
                    elif length == 4:
                        turn += 1
                    else:
                        turn = 0

            if turn == 2:
                ai_behavior(board, letter, turn)
                if win_check(board, letter[2]) == True:
                    print_board(board)
                    print 'You Lose! Sorry!'
                    game_on = False
                else:
                    if board_full(board) == True:
                        print_board(board)
                        print 'The Game is a tie!'
                        game_on = False
                    else:
                        turn = 0                
                        
        if another() == False:
            break
                    
        
        
               
    
if __name__ == "__main__":

    main()
