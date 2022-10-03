# Shalini Bhakta ID: 74028480
# Project 2 - ICS 32 W22

# overlapping.py
# Contains all functions whose functionality overlap between the two programs:
# the shell-only user interface and the networked ver. user interface

import connectfour

def print_welcome_message() -> None:
    '''Print welcome banner message to user.'''
    print('+--------------------------+')
    print('| Let\'s Play Connect Four! |')
    print('+--------------------------+')
    

def build_game_board() -> None:
    '''Asks user for number or rows and columns.'''
    print('+--------------------------+')
    print('|  Build Your Gameboard!   |')
    print('+--------------------------+')
    while True:
        ncols = int(input('Numnber of Columns (4-20): ').strip())
        nrows = int(input('Number of Rows (4-20): ').strip())
        if (4 <= ncols <= 20) and (4 <= nrows <= 20):
            return ncols, nrows
        else:
            print('Please enter valid number of columns and rows.')


def ask_username() -> str:
    '''Ask user for a username until a valid username is given.
    A valid username has no spaces.'''
    while True:
        user = input('Username: ').strip()
        if (' ' in user) or (user == ''):
            print('Not a valid username; Please enter a username with no spaces or tabs.')
        else:
            return user


def start_banner() -> None:
    '''Print start message to user.'''
    print('+---------------+')
    print('|  GAME START   |')
    print('+---------------+')


def _check_col(game_state: connectfour.GameState, user_col: str) -> int:
    '''
    Checks if the given column number is valid. Returns column number
    as integer if number is valid.
    '''
    try:
        user_col = int(user_col)
        if 1 <= user_col <= connectfour.columns(game_state):
            return user_col
    except:
        raise ValueError
            

def drop_turn(game_state: connectfour.GameState, column: int) -> connectfour.GameState:
    '''Initiates drop sequence into given column.'''
    game_state = connectfour.drop(game_state, column-1)
    return game_state

        
def pop_turn(game_state: connectfour.GameState, column: int) -> connectfour.GameState:
    '''Initiates pop sequence into given column.'''
    game_state = connectfour.pop(game_state, column-1)
    return game_state
    

def get_command(game_state: connectfour.GameState) -> connectfour.GameState:
    '''Asks if user wants to drop or pop. Calls to drop or pop. Prompts again
    if move is invalid or cannot be done.'''
    
    while True:
        move = input(
            'Enter command DROP or POP, a single space, then column number: ').strip()
        move = move.split()
        
        if len(move) != 2:
            print('Invalid move; Try again.')
        else:
            
            try:
                column = _check_col(game_state, move[1])
                command = move[0].upper()
                
                if command == 'DROP':
                    return f'DROP {column}', drop_turn(game_state, column)
                elif command == 'POP':
                    return f'POP {column}', pop_turn(game_state, column)
                else:
                    print('Invalid command; Try again.')
            except:
                print('Invalid move; Try again.')


def check_winner(game_state: connectfour.GameState) -> bool:
    '''Checks game state and returns True if there is a winner.'''
    
    w = connectfour.winner(game_state)
    if w != 0:
        return True
    else:
        return False


def print_board(game_state: connectfour.GameState) -> None:
    '''Displays board to user.'''
    
    var = 1
    rows = connectfour.rows(game_state)
    cols = connectfour.columns(game_state)
        
    for row in range(rows):
        if row == 0:
            for col in range(cols):
                if var >= 9:
                    print(var, end=' ')
                else:
                    print(var, end='  ')
                var += 1
            print('\r')
        for col in range(cols):
            if game_state.board[col][row] == 0:
                print('.', end='  ')
            elif game_state.board[col][row] == 1:
                print('R', end='  ')
            else:
                print('Y', end='  ')
        
        print('\n')
