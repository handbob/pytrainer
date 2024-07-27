from scripts.classes.house import House
from scripts.classes.car import Car
from scripts.classes.person import Person

from sys import argv

print('Hello from Python!\n')

house = House("1234 Elm St", 4, 250000.0, "Single Family", 1995)
house.display_info()

person = Person("John Doe", 30, "Male", "456 Elm Street", "555-1234")
person.display_info()

car = Car("Toyota", "Camry", 2020, 20000.0, "Blue", 15000)
car.display_info()

VERSION = '1.0.0'


def print_help():
    help_message = '''usage: pytrainer [options] <command> 

example: pytrainer -t -m tictactoe

options:
    -v, --version         show version
    -h, --help            show help
    -t, --training        training the AI models with the provided datasets
    -T, --tests         test the AI models with the provided datasets
    -d, --datasets        provided datasets format: [.csv, .json, .png]

commands:
    -m, --model           specify the AI model to use: [hangman, chess, cards, tictactoe]'''
    print(help_message)


if '--help' in argv or '-h' in argv:
    print_help()
else:
    print('Try `pytrainer -h or --help` for more information.')
