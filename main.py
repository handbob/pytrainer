import argparse
import sys
from data.generate_data import generate_data
from training.train_model import train_model
from tests.test_model import test_model

def main():
    parser = argparse.ArgumentParser(description='Tic-Tac-Toe AI')
    parser.add_argument('--generate-data', action='store_true', help='Generate Tic-Tac-Toe data')
    parser.add_argument('--train', action='store_true', help='Train the Tic-Tac-Toe model from scratch')
    parser.add_argument('--continue-training', action='store_true', help='Continue training the Tic-Tac-Toe model')
    parser.add_argument('--test', action='store_true', help='Test the Tic-Tac-Toe model')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs for training (must be a positive integer)')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    try:
        args = parser.parse_args()

        if args.epochs <= 0:
            raise ValueError('--epochs must be a positive integer.')

        if args.generate_data:
            generate_data()
        elif args.train:
            train_model(epochs=args.epochs, continue_training=False)
        elif args.continue_training:
            train_model(epochs=args.epochs, continue_training=True)
        elif args.test:
            test_model()
        else:
            raise ValueError('Invalid argument provided.')

    except FileNotFoundError as e:
        if 'data/tictactoe_data.csv' in str(e):
            print('Error: Data file not found. Please generate the data first using --generate-data.')
        elif 'models/tictactoe-1.0.0.pt' in str(e):
            print('Error: Model file not found. Please train the model first using --train or provide a valid model path.')
        else:
            print(f'FileNotFoundError: {e}')
        sys.exit(1)
    except argparse.ArgumentError as e:
        print(f'Error: {e}')
        parser.print_help()
        sys.exit(1)
    except ValueError as e:
        print(f'Error: {e}')
        parser.print_help()
        sys.exit(1)
    except Exception as e:
        print(f'Unexpected error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
