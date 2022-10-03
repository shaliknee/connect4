# Shalini Bhakta ID: 74028480
# Project 2 - ICS 32 W22


# shell_ui.py
# FIRST PROGRAM, allows the play of one game of Connect Four using only Python
# shell interaction between two human players.

import connectfour
import overlapping


def _show_winner(game_state: connectfour.GameState, p1, p2) -> None:
    '''Displays winner banner.'''
    if game_state.turn == 2:
        asci = len(p1) + 8
        print('+' + ('-' * asci) + '+')
        print(f'| {p1} WINS! |')
        print('+' + ('-' * asci) + '+')
    else:
        asci = len(p2) + 8
        print('+' + ('-' * asci) + '+')
        print(f'| {p2} WINS! |')
        print('+' + ('-' * asci) + '+')
    quit()
        

def _login() -> str:
    '''Get player name for each player.'''
    print('Player One (R), enter your username.')
    p1 = overlapping.ask_username()
    print('Player Two (Y), enter your username.')
    p2 = overlapping.ask_username()

    return p1.upper(), p2.upper()
    

def run_shell_ui() -> None:
    '''Run FIRST PROGRAM of ConnectFour game between two players.'''
    overlapping.print_welcome_message()
    player1, player2 = _login()
    col, row = overlapping.build_game_board()
    game_state = connectfour.new_game(col, row)
    overlapping.start_banner()
    overlapping.print_board(game_state)
    
    while not overlapping.check_winner(game_state):
        if game_state.turn == 1:
            print(f'R: {player1}\'s TURN')
        else:
            print(f'Y: {player2}\'s TURN')
        _, game_state = overlapping.get_command(game_state)
        overlapping.print_board(game_state)
        
    _show_winner(game_state, player1, player2)
    

if __name__ == '__main__':
    run_shell_ui()
