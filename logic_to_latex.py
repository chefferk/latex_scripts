from logic_suplemental import convertions
from logic_suplemental import rules
import re

# If test mode is False, this will ask user for file name and loop until valid file is given
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
        print('{} & {} ${}$ & {} & {}\\\\' .format(assumption_set[i], line_number[i], sentence[i].lower(), assumption_req[i], assumption[i]))


# Swaps symbols mainly for the sentence column, but I'm having trouble just changing that column
def sentence_swap(convertions, list):
    # TODO(fix) : only want this to apply to list[i][2]
    # TODO(fix) : could use regex to parse two spaces as boundry for sentences
    for i in range(len(list)):
        for j in range(len(convertions)):
            list[i] = [x.replace(convertions[j][2], convertions[j][1], 1) for x in list[i]]

    return list


# Swaps assumption symbols for English words
def assumption_swap(rules, list):
    for i in range(len(list)):
        for j in range(len(rules)):
            list[i] = [x.replace(rules[j][0], rules[j][2]) for x in list[i]]

    return list


def swap(convertions, logic):
    logic = logic.replace(' ', '')
    logic = logic.strip()
    for i in range(len(convertions)):
        logic = logic.replace(convertions[i][2], convertions[i][1])
        logic = logic.lower()
    return logic


def latex_print_line(logic):
    print('${}$\\\\' .format(logic))


def main():

    # DEBUG
    if test_mode is True:
        infile = open('latex2.txt', 'r')
    else:
        infile = get_file()

    # Create list and close file
    content_list = infile.readlines()
    infile.close()
    first_line = content_list[0]
    del content_list[0]

    # Split elements in list
    content_list = split_list(content_list)

    # swap out sentences
    content_list = sentence_swap(convertions, content_list)

    # swap out assumptions
    content_list = assumption_swap(rules, content_list)

    logic = swap(convertions, first_line)
    latex_print_line(logic)

    print('')

    print('\\begin{tabular}{llll}')
    # print final answer
    latex_print(content_list)
    print('\\end{tabular}')


if __name__ == "__main__":
    main()
