
import random
 
def main():
    
    def assign_letters():
        user_letter = ""
        while not (user_letter == "X" or user_letter == "O"): 
            print "Would you like to be X's or O's"
            user_letter = raw_input()
       
       
        if user_letter == "X":
            ai_letter = "O"
        if user_letter == "O":
            ai_letter = "X"
        
        return (user_letter, ai_letter)
        
    
    def print_board(board):
        print '\n'
        print "  " + board[0] + " I " + board[1] + " I " + board[2] + '\n'
        print "  " + board[3] + " I " + board[4] + " I " + board[5] + '\n'
        print "  " + board[6] + " I " + board[7] + " I " + board[8] + '\n'

    
    
        
    def check_space(board, move):
        return board[move] == " "
        
    def user_turn(board, letter):
        move = '9'
        while move not in grid or check_space(board, int(move)) == False:
            print "Where would you like to move?"
            move = raw_input()
        
        board[int(move)] = letter[0]
        return board
        
    def win_check(board, letter):
        return ((board[0] == letter and board[1] == letter and board[2] == letter) or
        (board[3] == letter and board[4] == letter and board[5] == letter) or
        (board[6] == letter and board[7] == letter and board[8] == letter) or
        (board[0] == letter and board[3] == letter and board[6] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[0] == letter and board[4] == letter and board[8] == letter) or
        (board[2] == letter and board[4] == letter and board[6] == letter))
    
    def ai_behavior(board, letter):
        
        for i in range(9):
            test = list(board)
            if check_space(test, i) == True:
                test[i] = letter[1]
                if win_check(test, letter[1]) == True:
                    board[i] = letter[1]
                    return board
                    
        for p in range(9):
            test = list(board)
            if check_space(test, p) == True:
                test[p] = letter[0]
                if win_check(test, letter[0]) == True:
                    board[p] = letter[1]
                    return board
        
        while True:
            r = random.randint(0,8)
            if check_space(board, r) == True:
                board[r] = letter[1]
                return board
    
    def board_full(board):
        for f in range(9):
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
        
    while True:
        #Set a blank board for new game.
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", "start"]
    
        grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        
        letter = assign_letters()
        print "Player is " + str(letter[0])
        
        #Lets player know what each grid space corresponds to.
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
                ai_behavior(board, letter)
                if win_check(board, letter[1]) == True:
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
