from logicDB import rules
from logicDB import conversions
import re

# If in test mode, file is already selected vs user entering file name
# (e.g. terminal interface)
# DEBUG
test_mode = True


# Description: If test mode is False, this will ask user for file name and loop
#              until valid file is given
# Input: none, user input
# Output: the opened file - infile
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


# Description: Creates a new 2D list with each element split
# Input: content_list - a 1D list with *correct* spacing
# Output: split list
def split_list(content_list):
    # Split elements in list
    new_list = []
    for i in range(len(content_list)):
        matches = re.findall(r'([^\s]+)', content_list[i])
        # handle empty assumption set
        if matches[0][0] == '(':
            matches.insert(0,'')
        # handle assumption line
        if matches[3] == 'A':
            matches.insert(3,'')
        new_list.append((matches))

    return new_list


# Description: Prints LaTex formatting to the console
# Input: content_list
# Output: none, output to screen
# TODO : this could be simplified a lot
def latex_print(content_list):
    assumption_set = []
    line_number = []
    sentence = []
    annotation_set = []
    annotation = []

    for i in range(len(content_list)):
        assumption_set.append(content_list[i][0])
        line_number.append(content_list[i][1])
        sentence.append(content_list[i][2])

        # Some rows have 5 columns due to annotation sets
        # TODO : this seems like a poor way to handle this
        if len(content_list[i]) == 5:
            annotation_set.append(content_list[i][3])
            annotation.append(content_list[i][4])
        else:
            annotation_set.append('')
            annotation.append(content_list[i][3])

        # TODO : Prints to console, could return or save to file in future
        print('{} & {} ${}$ & {} & {}\\\\' .format(assumption_set[i],
                                                   line_number[i],
                                                   sentence[i],
                                                   annotation_set[i],
                                                   annotation[i]))


# Description: Swaps symbols for sentence column from logic to LaTex
# Input: conversions list, content list
# Output: updated list
def sentence_swap(conversions, content_list):
    for i in range(len(content_list)):
        for j in range(len(conversions)):
                content_list[i][2] = content_list[i][2].replace(conversions[j][2], conversions[j][1])

    return content_list


# Description: Swaps annotation symbols for words
# Input: rules list, content list
# Output: updated list
def assumption_swap(rules, content_list):
    for i in range(len(content_list)):
        for j in range(len(rules)):
            content_list[i][4] = content_list[i][4].replace(rules[j][0], rules[j][2])

    return content_list


# Description: Performs swaps for first line
# Input: conversions list, line to be converted
# Output: converted line
def swap(conversions, logic):
    logic = logic.replace(' ', '')
    logic = logic.strip()
    for i in range(len(conversions)):
        logic = logic.replace(conversions[i][2], conversions[i][1])
    return logic


# Description: Prints converted line
# Input: converted line
# Output: none, screen output
def latex_print_line(logic):
    print('${}$\\\\' .format(logic))


def main():

    # DEBUG
    if test_mode is True:
        infile = open('logic.txt', 'r')
    else:
        infile = get_file()

    # Create list and close file
    content_list = infile.readlines()
    infile.close()
    first_line = content_list[0]
    del content_list[0]

    # Split elements in list
    content_list = split_list(content_list)

    # DEBUG - 1
    if test_mode is True:
        print('-' * 20)
        print('(1) [Assumption set, Line Number, Sentence, Annotation]')
        print('-' * 20)
        # [Assumption set, Line Number, Sentence, Annotation]
        for i in content_list:
            print(i)

    # DEBUG - 2
    if test_mode is True:
        print('-' * 20)
        print('(2) Initial LaTex print before any swaps')
        print('-' * 20)
        latex_print(content_list)

    content_list = assumption_swap(rules, content_list)

    # DEBUG - 3
    if test_mode is True:
        print('-' * 20)
        print('(3) LaTex print after Annotations are swapped')
        print('-' * 20)
        latex_print(content_list)

    content_list = sentence_swap(conversions, content_list)

    logic = swap(conversions, first_line)

    # DEBUG - 4
    if test_mode is True:
        print('-' * 20)
        print('(4) LaTex print after sentences are swapped (final result)')
        print('-' * 20)
        latex_print_line(logic)
        print('')
        print('\\begin{tabular}{llll}')
        # print final answer
        latex_print(content_list)
        print('\\end{tabular}')
    else:
        latex_print_line(logic)
        print('')
        print('\\begin{tabular}{llll}')
        # print final answer
        latex_print(content_list)
        print('\\end{tabular}')


if __name__ == "__main__":
    main()
