import os
import platform

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')


## show board

def board(row1, row2, row3):
    print('   |   |   ')
    print(row1)
    print('___|___|___')
    print('   |   |   ')
    print(row2)
    print('___|___|___')
    print('   |   |   ')
    print(row3)
    print('   |   |   ')

board()

def check_board():
    pass
    #board_pos = [1, 5, 9]

## first user input
def player_move():
    print('Player 1 turn!')
    select_row = 'Wrong move'
    select_pos = 'Wrong move'
    within_range = False

    while select_row.isdigit() == False or within_range == False:
        print('Select a row to play!')
        select_row = input('[0] Top \n[1] Middle \n[2] Bottom: \nAnswer: ')
        if select_row.isdigit() :
            if int(select_row) in range(0,3):
                within_range = True
            else:
                within_range = False

        if not select_row.isdigit():
            print("Sorry, but you did not enter an integer. Please try again.")
            clear()

    return select_row, select_pos
    

#player_move()

## check if game ended
def endgame():
    pass

## run everything
def tic_tac_toe():
    pass