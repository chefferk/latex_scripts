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


def main():
    pass

if __name__ == "__main__":
    main()