from sys import argv

VERSION = '1.0.0'


def print_help():
    help_message = '''
Usage: py_ai <command> [options]

Commands:
    generate              Generate datasets for the AI models.
    test                  Test the AI models with the provided datasets.
    train                 Train the AI models with the provided datasets.
    continue              Continue training the AI models with additional datasets.

Options:
    -v, --version         show version
    -h, --help            show help message
    -m, --models          Specify the AI models to use. Choose from {hangman, chess, cards, tictactoe}.
    '''
    print(help_message)


def main():
    args = argv[1:]

    if not args or '-h' in args or '--help' in args:
        print_help()
        return

    if '-v' in args or '--version' in args:
        print(f'pyai version {VERSION}')
        return

    model = None
    if '-m' in args or '--models' in args:
        model_index = args.index('-m') if '-m' in args else args.index('--models')
        try:
            model = args[model_index + 1]
        except IndexError:
            print('Missing argument for --models option.')
            return

        if model not in ['hangman', 'chess', 'cards', 'tictactoe']:
            print('Invalid models. Choose from {hangman, chess, cards, tictactoe}.')
            return

    if len(args) < 2:
        print_help()
        return

    command = args[0]
    command_args = args[1:]

    if command == 'generate':
        if '--output' in command_args:
            try:
                output_index = command_args.index('--output')
                output_path = command_args[output_index + 1]
                print(f'Generating datasets to {output_path}')
            except IndexError:
                print('Missing value for --output option.')
                print_help()
        else:
            print('Missing required argument: --output')
            print_help()

    elif command == 'test':
        if '--input' in command_args:
            try:
                input_index = command_args.index('--input')
                input_path = command_args[input_index + 1]
                print(f'Testing datasets from {input_path}')
            except IndexError:
                print('Missing value for --input option.')
                print_help()
        else:
            print('Missing required argument: --input')
            print_help()

    elif command == 'train':
        if '--input' in command_args:
            try:
                input_index = command_args.index('--input')
                input_path = command_args[input_index + 1]
                print(f'Training datasets from {input_path}')
            except IndexError:
                print('Missing value for --input option.')
                print_help()
        else:
            print('Missing required argument: --input')
            print_help()

    elif command == 'continue':
        if '--input' in command_args:
            try:
                input_index = command_args.index('--input')
                input_path = command_args[input_index + 1]
                print(f'Continuing training with datasets from {input_path}')
            except IndexError:
                print('Missing value for --input option.')
                print_help()
        else:
            print('Missing required argument: --input')
            print_help()

    else:
        print_help()


if __name__ == '__main__':
    main()
