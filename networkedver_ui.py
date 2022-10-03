# Shalini Bhakta ID: 74028480
# Project 2 - ICS 32 W22

# networkedver_ui.py
# This program is the user interface of the SECOND PROGRAM,
# and allows a networked version of the game to be played against an AI.

import handling
import connectfour
import overlapping


class NetworkError(Exception):
    pass
        

def _login(connection: handling.C4Connection) -> None:
    '''Logs into game by passing a valid username to welcome sequence.'''
    
    username = overlapping.ask_username()
    handling.welcome(connection, username)
    return username
    

def _winner_banner(game_state: connectfour.GameState, username) -> None:
    '''Shows the winner and ends program.'''

    chars = len(username)
    if game_state.turn == 2:
        asci = 28 + chars
        print('+' + ('-' * asci) + '+')
        print(f'| CONGRATULATIONS {username.upper()}! YOU WIN! |')
        print('+' + ('-' * asci) + '+')
    else:
        asci = 21 + chars
        print('+' + ('-' * asci) + '+')
        print(f'| SORRY {username.upper()}! YOU LOSE :( |')
        print('+' + ('-' * asci) + '+')
    quit()
    

def _begin_game(connection: handling.C4Connection) -> connectfour.GameState:
    '''Builds game board and begins game.'''
    col, row = overlapping.build_game_board()
    handling.start_game(connection, col, row)
    game_state = connectfour.new_game(col, row)
    overlapping.start_banner()
    overlapping.print_board(game_state)
    
    return game_state


def _take_turns(connection: handling.C4Connection, game_state: connectfour.GameState) -> '???':

    while not overlapping.check_winner(game_state):
        if game_state.turn == 1:
            print('R: YOUR TURN')
            game_state = _user_turn(connection, game_state)
            
        elif game_state.turn == 2:
            print('Y: AI TURN...')
            game_state = _ai_turn(connection, game_state)

        overlapping.print_board(game_state)
    return game_state


def _user_turn(connection: handling.C4Connection, game_state: connectfour.GameState) -> '??':
    command, game_state = overlapping.get_command(game_state)
    handling.user_turn(connection, command)
    return game_state


def _ai_turn(connection: handling.C4Connection, game_state: connectfour.GameState) -> '??':
    move = handling.ai_turn(connection)

    move = move.split()
    col = int(move[1])
    command = move[0].upper()
    if command == 'DROP':
        return overlapping.drop_turn(game_state, col)
    elif command == 'POP':
        return overlapping.pop_turn(game_state, col)  
    return game_state
        
    
def run_networkedver_ui() -> None:
    
    host = input('Host: ').strip()
    port = int(input('Port: ').strip())

    try:
        connection = handling.connect(host, port)
    except:
        quit()
        raise NetworkError

    try:
        overlapping.print_welcome_message()
        username = _login(connection)
        game_state = _begin_game(connection)
        game_state = _take_turns(connection, game_state)
        _winner_banner(game_state, username)
    finally:
        handling.close(connection)


if __name__ == '__main__':
    run_networkedver_ui()
