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


def latex_print(list):
    assumption_set = []
    line_number = []
    sentence = []
    assumption = []

    for i in range(len(list)):
        assumption_set.append(list[i][0])
        line_number.append(list[i][1])
        sentence.append(list[i][2])
        assumption.append(list[i][3])

        print('{} & {} ${}$ & {}\\\\' .format(assumption_set[i], line_number[i], sentence[i], assumption[i]))


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

    if test_mode is True:
        # [Assumption set, Line Number, Sentence, Annotation]
        for i in split_list:
            print(i)

        print('-' * 20)

    latex_print(split_list)


if __name__ == "__main__":
    main()
