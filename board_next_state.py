from board_states import *

def next_board_state(board_state):
    next_state = []
    # Loop through each row to check the cells.
    for yCoord in range(len(board_state)):
        next_state.append([])
        # Loop through each individual cell in a row.
        for xCoord in range(len(board_state[yCoord])):
            aliveNeighbours = 0
            # Check each of the adjacent cells in the row above current cell.
            if yCoord != 0 and xCoord != 0:
                aliveNeighbours += board_state[yCoord - 1][xCoord - 1]
            if yCoord != 0:
                aliveNeighbours += board_state[yCoord - 1][xCoord]
            if yCoord != 0 and xCoord != (len(board_state[yCoord]) - 1):
                aliveNeighbours += board_state[yCoord - 1][xCoord + 1]
            # Check each of the adjacent cells in the same row as current cell.
            if xCoord != 0:
                aliveNeighbours += board_state[yCoord][xCoord - 1]
            if  xCoord != (len(board_state[yCoord]) - 1):
                aliveNeighbours += board_state[yCoord][xCoord + 1]
            # Check each of the adjacent cells in the row below current cell.
            if yCoord != (len(board_state) - 1) and xCoord != 0:
                aliveNeighbours += board_state[yCoord + 1][xCoord - 1]
            if yCoord != (len(board_state) - 1):
                aliveNeighbours += board_state[yCoord + 1][xCoord]
            if yCoord != (len(board_state) - 1) and xCoord != (len(board_state[yCoord]) - 1):
                aliveNeighbours += board_state[yCoord + 1][xCoord + 1]
        # Follows the rules based on cell state and number of alive neighbours to either append a 0 or 1.
            if aliveNeighbours < 2 or aliveNeighbours > 3:
                next_state[yCoord].append(0)
            elif aliveNeighbours == 2:
                next_state[yCoord].append(board_state[yCoord][xCoord])
            elif aliveNeighbours == 3:
                next_state[yCoord].append(1)
    return next_state
