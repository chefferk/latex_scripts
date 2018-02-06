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

    content_list = infile.readlines()
    infile.close()

    split_list = list()

    for i in range(len(content_list)):
        split_list.append(re.findall(r'([^\s]+)', content_list[i]))

    for i in split_list:
        print(i)


if __name__ == "__main__":
    main()
