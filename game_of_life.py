from board_states import *
from board_next_state import *
from board_render import *

start_state_x = int(input("How many columns? > "))
start_state_y = int(input("How many rows? > "))
board_state = random_state(start_state_x, start_state_y)

# Infinitely loops through the game, pausing with every 
while True:
    render(board_state)
    board_state = next_board_state(board_state)
    input("Enter to continue: ")