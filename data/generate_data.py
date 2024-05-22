import numpy as np
import pandas as pd
import os

EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1

def check_winner(board):
    for player in [PLAYER_X, PLAYER_O]:
        win = player * 3
        if any(np.sum(board, axis=0) == win) or any(np.sum(board, axis=1) == win) or np.trace(board) == win or np.trace(np.fliplr(board)) == win:
            return player
    return None

def get_empty_positions(board):
    return np.argwhere(board == EMPTY)

def make_move(board, position, player):
    new_board = board.copy()
    new_board[position[0], position[1]] = player
    return new_board

def generate_data():
    print('Starting data generation...')
    data = []
    for _ in range(50000):
        board = np.zeros((3, 3), dtype=int)
        current_player = PLAYER_X
        states = []
        moves = []
        while True:
            empty_positions = get_empty_positions(board)
            if empty_positions.size == 0 or check_winner(board) is not None:
                break
            move = empty_positions[np.random.choice(len(empty_positions))]
            states.append(board.flatten().tolist())
            moves.append(np.ravel_multi_index(move, (3, 3)))
            board = make_move(board, move, current_player)
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
        for i in range(len(states)):
            data.append((states[i], moves[i]))
    df = pd.DataFrame(data, columns=['state', 'move'])
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/tictactoe_data.csv', index=False)
    print('Data generation completed. Data saved to data/tictactoe_data.csv')

if __name__ == '__main__':
    generate_data()
