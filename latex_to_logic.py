import re
from logic_suplemental import convertions, rules
import pprint

pprint.pprint(convertions)
pprint.pprint(rules)
print('asdf')
# If in test mode, file is already selected vs user entering file name
# DEBUG
test_mode = True


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


def menu():
    print('(1) Logic to LaTex')
    print('(2) LaTex to Logic\n')

    # DEBUG
    if test_mode is True:
        choice = 1
    else:
        choice = input('Option: ')


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

        # Prints to console for right now, could return or could save to file in future
        print('{} & {} ${}$ & {} & {}\\\\' .format(assumption_set[i], line_number[i], sentence[i], assumption_req[i], assumption[i]))


# Swaps symbols mainly for the sentence column, but I'm having trouble just changing that column
def sentence_swap(convertions, list):
    if test_mode is True:
        print('-' * 20)
        print('Sentences after convertion')
        print('-' * 20)

    # TODO(fix) : only want this to apply to list[i][2]
    for i in range(len(list)):
        for j in range(len(convertions)):
            list[i] = [x.replace(convertions[j][2], convertions[j][1]) for x in list[i]]

        # DEBUG
        if test_mode is True:
            print(list[i][2])

    return list


# Swaps assumption symbols for English words, they still suck. Will need to convert again to our definitions
def assumption_swap(rules, list):
    if test_mode is True:
        print('-' * 20)
        print('Assumption after convertion')
        print('-' * 20)

    for i in range(len(list)):
        for j in range(len(rules)):
            list[i] = [x.replace(rules[j][0], rules[j][2]) for x in list[i]]

        # DEBUG
        if test_mode is True:
            print(list[i][2])

    return list


def main():
    convertions = [['not', ' \\neg ', '~'],
                   ['and', ' \\wedge ', '&'],
                   ['or', ' \\vee ', 'v'],
                   ['implies', ' \\to ', '->'],
                   ['iff', ' \\leftrightarrow ', '<->'],
                   ['all', ' \\forall ', '@'],
                   ['some', ' \\exists ', '$']]

    menu()

    # DEBUG
    if test_mode is True:
        infile = open('latex.txt', 'r')
    else:
        infile = get_file()

    content_list = infile.readlines()
    infile.close()

    # Get rules file
    # This gets really confusing, clean this up
    rules_infile = open('rules2.txt', 'r')
    rules = rules_infile.readlines()
    rules_infile.close()

    # DEBUG
    this = True
    if test_mode is True and this == False:
        pprint.pprint(rules)

    # strips & splits lines -> makes 2d array
    rules_list = list()
    for i in rules:
        content = i.strip()
        rules_list.append(content.split(', '))

    # DEBUG
    if test_mode is True:
        pprint.pprint(rules_list)

    split_list = list()

    for i in range(len(content_list)):
        split_list.append(re.findall(r'([^\s]+)', content_list[i]))

    # DEBUG
    if test_mode is True:
        # [Assumption set, Line Number, Sentence, Annotation]
        for i in split_list:
            print(i)

        print('-' * 20)

    # DEBUG
    if test_mode is True:
        latex_print(split_list)
        print('-' * 20)

    swap_list = assumption_swap(rules_list, split_list)

    # DEBUG
    if test_mode is True:
        latex_print(swap_list)

    swap_list = sentence_swap(convertions, split_list)
    latex_print(swap_list)


if __name__ == "__main__":
    main()
