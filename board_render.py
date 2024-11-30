from board_states import *

def render(board_state):
    rendered_board = "-" * (len(board_state[0]) + 2)
    # Loops through each row of board, checking value and adding 0 or 1 to the render
    for row in range(len(board_state)): 
        rendered_board += "\n|"
        for column in board_state[row]:
            if column == 1:
                rendered_board += "*"
            else: rendered_board += " "
        rendered_board += "|"
    rendered_board += "\n" + "-" * (len(board_state[0]) + 2)
    print(rendered_board)
