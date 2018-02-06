from logic_suplemental import convertions
from logic_suplemental import rules
import re

# If in test mode, file is already selected vs user entering file name
# DEBUG
test_mode = True


def menu():
    # DEBUG
    if test_mode is True:
        choice = 1
    else:
        print('(1) Logic to LaTex')
        print('(2) LaTex to Logic\n')
        choice = input('Option: ')


# If test mode is False, this will ask user for file name and loop until valid file is given
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


def split_list(list):
    # Split elements in list
    new_list = []
    for i in range(len(list)):
        new_list.append(re.findall(r'([^\s]+)', list[i]))

    return new_list


# Prints LaTex formating to the console
def latex_print(list):
    assumption_set = []
    line_number = []
    sentence = []
    assumption_req = []
    assumption = []

    for i in range(len(list)):
        assumption_set.append(list[i][0])
        line_number.append(list[i][1])
        sentence.append(list[i][2])

        # Some rows have 5 columns due to assumption assumption requirements
        if len(list[i]) == 5:
            assumption_req.append(list[i][3])
            assumption.append(list[i][4])
        else:
            assumption_req.append('')
            assumption.append(list[i][3])

        # TODO(add): Prints to console for right now, could return or could save to file in future
        print('{} & {} ${}$ & {} & {}\\\\' .format(assumption_set[i], line_number[i], sentence[i], assumption_req[i], assumption[i]))


# Swaps symbols mainly for the sentence column, but I'm having trouble just changing that column
def sentence_swap(convertions, list):
    # TODO(fix) : only want this to apply to list[i][2]
    for i in range(len(list)):
        for j in range(len(convertions)):
            list[i] = [x.replace(convertions[j][2], convertions[j][1]) for x in list[i]]

    return list


# Swaps assumption symbols for English words, they still suck. Will need to convert again to our definitions
def assumption_swap(rules, list):
    for i in range(len(list)):
        for j in range(len(rules)):
            list[i] = [x.replace(rules[j][0], rules[j][2]) for x in list[i]]

    return list


def main():

    menu()

    # DEBUG
    if test_mode is True:
        infile = open('latex.txt', 'r')
    else:
        infile = get_file()

    # Create list and close file
    content_list = infile.readlines()
    infile.close()

    # Split elements in list
    content_list = split_list(content_list)

    # DEBUG
    if test_mode is True:
        print('-' * 20)
        print('[Assumption set, Line Number, Sentence, Annotation]')
        print('-' * 20)
        # [Assumption set, Line Number, Sentence, Annotation]
        for i in content_list:
            print(i)

    # DEBUG
    if test_mode is True:
        print('-' * 20)
        print('Initial LaTex print before any swaps')
        print('-' * 20)
        latex_print(content_list)

    content_list = assumption_swap(rules, content_list)

    # DEBUG
    if test_mode is True:
        print('-' * 20)
        print('LaTex print after Annotations are swapped')
        print('-' * 20)
        latex_print(content_list)

    content_list = sentence_swap(convertions, content_list)

    if test_mode is True:
        print('-' * 20)
        print('LaTex print after sentences are swapped (final result)')
        print('-' * 20)
        latex_print(content_list)
    else:
        latex_print(content_list)


if __name__ == "__main__":
    main()
