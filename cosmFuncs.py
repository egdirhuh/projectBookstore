from os import system, name
import shutil #to get command window's size


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def get_terminal_columns(): #to get command window's size
    return shutil.get_terminal_size().columns

def prnHeader(title):
    clear()
    width = get_terminal_columns()
    print("*" * width)
    print("*" + " "*int((width-len(title))/2 - 1) + title + " "*int((width-len(title))/2 - 1) + "*")
    print("*" * width)

def prnCenter(phrase):
    width = get_terminal_columns()
    print(" "*int((width-len(phrase))/2) + phrase + " "*int((width-len(phrase))/2))


def prnOptions(options):
    i = 1
    for option in options:
        print("    ", end="")
        print("{}. {}".format(i, option))
        i += 1
    while True:
        choice = input("\n Enter your choice: ")
        try:
            if 0 < int(choice) < i:
                break
            print("Invalid Choice!")
        except :
            print("Please input a valid choice!")
    print('\n')
    return choice