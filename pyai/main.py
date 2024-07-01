from sys import argv

VERSION = '1.0.0'


def print_help():
    help_message = '''usage: pyai [options] <command> 

example: pyai -t -m tictactoe

options:
    -v, --version         show version
    -h, --help            show help
    -t, --training        train the AI models with the provided datasets
    -T, --testing         test the AI models with the provided datasets
    -d, --datasets        provided datasets format: [.csv, .json, .png]

commands:
    -m, --model           specify the AI model to use: [hangman, chess, cards, tictactoe]'''
    print(help_message)


def main():
    if len(argv) > 1:
        print_help()
    else:
        print('Try `pyai --help` for more information.')


if __name__ == '__main__':
    main()
