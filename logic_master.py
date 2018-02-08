from logic_suplemental import *
from latex_to_logic import *
from logic_to_latex import *


def menu():
    # DEBUG
    if test_mode is True:
        choice = 1
    else:
        print('(1) Logic to LaTex')
        print('(2) LaTex to Logic\n')
        choice = input('Option: ')

    return choice


def main():

    choice = menu()


if __name__ == "__main__":
    main()
