import re

# If in test mode, file is already selected vs user entering file name
test_mode = True


def get_file():
    flag = True
    while flag is True:
        try:
            file = input('Enter the name of the txt file: ')
            infile = open(file, 'r')
            flag = False
        except Exception:
            flag = True
    return infile


def main():
    if test_mode is True:
        infile = open('latex.txt', 'r')
    else:
        infile = get_file()

    print(infile)


main()
