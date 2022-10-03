# Shalini Bhakta ID: 74028480
# Project 2 - ICS 32 W22

# handling.py
# This program concerns functions for implementing I32CFSP and all
# socket handling for the ConnectFour (networkedver_ui.py) game.

import socket
from collections import namedtuple


_SHOW_DEBUG_TRACE = False

class C4ProtocolError(Exception):
    '''Raised when protocol does not run as expected.'''
    pass


C4Connection = namedtuple(
    'C4Connection',
    ['socket', 'input', 'output'])


def connect(host: str, port: int) -> C4Connection:
    '''Connects client to a server given a host and port.'''
    c4_socket = socket.socket()
    c4_socket.connect((host, port))

    c4_input = c4_socket.makefile('r')
    c4_output = c4_socket.makefile('w')

    return C4Connection(
        socket = c4_socket,
        input = c4_input,
        output = c4_output)


def close(connection: C4Connection) -> None:
    '''Closes client-server network connection.'''
    connection.input.close()
    connection.output.close()
    connection.socket.close()


def welcome(connection: C4Connection, username: str) -> bool:
    '''
    Takes first client input to make sure correct network is
    connected and username is valid. Raises C4ProtocolError if not.
    '''
    
    _write_line(connection, f'I32CFSP_HELLO {username}')

    ans = _read_line(connection)
    if ans.startswith('WELCOME '):
        return True
    else:
        raise C4ProtocolError


def start_game(connection: C4Connection, col, row) -> None:
    '''Writes board dimensions to server to start game.'''
    _write_line(connection, f'AI_GAME {col} {row}')

    res = _read_line(connection)

    if res != 'READY':
        raise C4ProtocolError


def ai_turn(connection: C4Connection) -> str:
    '''Reads AI's move from the server.'''
    line1 = _read_line(connection)
    line2 = _read_line(connection)
    
    return line1
    

def user_turn(connection: C4Connection, command: str) -> None:
    '''Writes user's move to the server.'''

    _write_line(connection, f'{command}')
    res = _read_line(connection)


def _write_line(connection: C4Connection, line: str) -> None:
    connection.output.write(line + '\r\n')
    connection.output.flush()

    if _SHOW_DEBUG_TRACE:
        print('SENT:  ' + line)
        
    
def _read_line(connection: C4Connection) -> str:
    line = connection.input.readline()[:-1]
        
    if _SHOW_DEBUG_TRACE:
        print('RCVD:  ' + line)
        
    return line

