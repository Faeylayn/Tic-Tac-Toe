import copy
import random

def board_size():
    "Get the grid size from the Player."
    length = ""
    while not (length == "3" or length == "4"): 
        print "Would you like to play a grid of 3 or 4"
        print "Please enter 3 or 4 (a 3x3 Grid will play against 1 Opponent, a 4x4 will play against 2 opponents."
        length = raw_input()
    return int(length)

def assign_letters():
    user_letter = ""
    while not (user_letter == "X" or user_letter == "O"): 
        print "Would you like to be X's or O's"
        user_letter = raw_input()
       
    if user_letter == "X":
        ai_letter = "O"
    if user_letter == "O":
        ai_letter = "X"
        
    return [user_letter, ai_letter]
        
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
    z = 0
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
    row = (move) / len(board)
    space = (move) % len(board[row])
    return board[row][space] == " "
        
def make_move(board, move, letter):
    "Take a location on the board and save the move to the board state."
    row = (move) / len(board)
    space = (move) % len(board[row])
    board[row][space] = letter
    return board

def user_turn(board, letter, grid):
    move = '40'
    while (int(move) >= (len(board) * len(board[1]))) or (check_space(board, int(move)) == False):
        print "Where would you like to move?"
        move = raw_input()

    return make_move(board, int(move), letter)

def checker(test, letter):
    "Check a list for a sequence of three elements in a row. Assumes the list is at least of length 3."
    for i in range(len(test) - 2):
        if (test[i] == letter) and (test[i + 1] == letter) and (test[i + 2] == letter):
            return True
             
def col_flip(board):
    "Create a list of the board to put the columns of the board into their own lists. Assumes the length of all rows are equal." 
    test = []
    for y in range(len(board[1])):
        test.append(list())
        for x in range(len(board)):
            test[y].append(board[x][len(board) - y - 1])
    return test

def diag(board):
    "Create a list of lists for all diagnol positions on board with three or more elements."
    test = []
    for x in range(len(board)-2):
        
        test.append(list())
        for y in range(len(board[1]) - x):
            test[x].append(board[x + y][y])
            
    for c in range(len(board[1])-2):
        test.append(list())
        for d in range(len(board[1])-c):
            test[len(board)+c-2].append(board[d][d+c])             
    return test
        
def win_check(board, letter):
    "Check for tic-tac-toe win condition in the board state. Assumes board is a list of lists."
        
    for i in range(len(board)):
        if checker(board[i], letter):
            return True
    
    col_test = col_flip(board)

    for c in range(len(col_test)):
        if checker(col_test[c], letter):
            return True

    diag_test = diag(board)

    for d in range(len(diag_test)):
        if checker(diag_test[d], letter):
            return True
    
    diag_col = diag(col_test)

    for e in range(len(diag_col)):
        if checker(diag_col[e], letter):
            return True
    
def ai_check(board, letter):
    total = len(board) * len(board[1])

    for i in range(total):
        test = copy.deepcopy(board)
        if check_space(test, i) == True:
            row = (i) / len(board)
            space = (i) % len(board[row])
            test[row][space] = letter
            if win_check(test, letter) == True:
                return i    
    return False

def ai_behavior(board, letter, turn, ai_num):
    counter = turn    
    #import pdb; pdb.set_trace()
    if check_space(board, (len(board) + (len(board) / 2))):
        return make_move(board, (len(board) + (len(board) / 2)), letter[turn])
    
    if ai_num == 2:
        ai_2 = ai_check(board, letter[counter])
        if ai_2 != False:
            return make_move(board, ai_2, letter[turn])
        counter = 0

    ai_1 = ai_check(board, letter[counter])
    if ai_1 != False:
        return make_move(board, ai_1, letter[turn])
    if counter == 0:
        counter = 1
    else:
        counter = 0

    ai_p =  ai_check(board, letter[counter])
    if ai_p != False:
        return make_move(board, ai_p, letter[turn])
    
    
    while True:
        r = (random.random() * 2) - 1
        rand = ((len(board) ^ 2) / 2) + ((len(board) * r))
        if check_space(board, int(rand)):
            return make_move(board, int(rand), letter[turn])
    
def board_full(board):
    "Check if the board has any playable spaces"
    total = len(board) * len(board[1])
    for f in range(total):
        if check_space(board, f) == True:
            return False
        
    return True
        
def first(ai_num):
    return random.randint(0, ai_num)
        
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
        ai_num = 1
        letter = assign_letters()
        if length == 4:
            letter.append('Z')
            ai_num = 2
        print "Player is " + str(letter[0])
        
        board = make_board(length)
        grid = make_grid(length)
               
        print_board(grid)
        turn = first(ai_num)
        
        if turn == 0:
            print 'The Player is first'
        else:
            print 'The Computer is first'
        
        game_on = True
        
        while game_on:
            if turn == 0:
                print_board(board)
                board = user_turn(board, letter[0], grid)
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
                #import pdb; pdb.set_trace()
                board = ai_behavior(board, letter, turn, ai_num)

                if win_check(board, letter[1]) == True:
                    print_board(board)
                    print 'You Lose! Sorry!'
                    game_on = False
                else:

                    if board_full(board) == True:
                        print_board(board)
                        print 'The Game is a tie!'
                        game_on = False
                    elif ai_num == 2:
                        turn += 1
                    else:
                        turn = 0

            if turn == 2:
                ai_behavior(board, letter, turn, ai_num)
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
