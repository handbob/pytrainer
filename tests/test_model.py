import torch
import numpy as np
from models.tictactoe_model import TicTacToeModel

def test_model():
    print('Starting model testing...')
    model = TicTacToeModel()
    model.load_state_dict(torch.load('models/tictactoe.pt'))
    model.eval()

    def print_board(board):
        for row in board:
            print(' '.join(['X' if x == 1 else 'O' if x == -1 else '_' for x in row]))
        print()

    test_boards = [
        np.array([[ 1, -1,  1],
                  [-1,  1, -1],
                  [ 0,  1, -1]]),

        np.array([[ 1,  1, -1],
                  [-1, -1,  1],
                  [ 0,  1,  0]]),

        np.array([[ 0,  0,  0],
                  [ 0,  0,  0],
                  [ 0,  0,  0]]),

        np.array([[ 1,  1,  0],
                  [ 0, -1, -1],
                  [ 0,  0,  1]])
    ]

    test_states = [torch.FloatTensor(board.flatten()).unsqueeze(0) for board in test_boards]

    for i, state in enumerate(test_states):
        with torch.no_grad():
            output = model(state)
        predicted_move = torch.argmax(output, dim=1).item()
        move_position = np.unravel_index(predicted_move, (3, 3))
        
        print(f'Test Board {i + 1}:')
        print_board(test_boards[i])
        print(f'Predicted Move: {move_position}\n')

    print('Model testing completed.')

if __name__ == '__main__':
    test_model()
