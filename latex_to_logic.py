import re
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


def split_list(list):
    # Split elements in list
    new_list = []
    for i in range(len(list)):
        temp = (re.findall(r'(?<=\s{2})(\S.*?)(?=\s{2})'))
        temp = temp.strip()
    print(temp)

    return new_list

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

print(content_list)

# Split elements in list
content_list = split_list(content_list)