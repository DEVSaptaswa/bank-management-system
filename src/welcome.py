from pyfiglet import Figlet
def welcome():
    f = Figlet(font='slant',justify='center')
    print(f.renderText('WELCOME'))
    print("1. New User")
    print("2. Existing User")
    n=int(input("Your choice: "))
    return n