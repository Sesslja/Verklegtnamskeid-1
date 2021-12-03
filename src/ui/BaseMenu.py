import os
try:
    import readline
except ImportError:
    pass
from ui.textCompleter import TextCompleter

class BaseMenu :
    def __init__(self):
        self.menu_options = {}
        self.clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
        self.menu_title = str()
        self.isMainMenu = False

    def print_options(self):
        menuState = 'run'
        while menuState == 'run':
            self.clear()
            to_print = self.menu_title + '\n'
            to_print += ("-"*30) + '\n'
            for key in  self.menu_options :
                to_print += f"[{key}] {self.menu_options[key]['title']} \n"
            to_print += ("-"*30)
            print(to_print)
            menuState = self.get_user_input()
            if menuState == 'main': # Check if the user wanted to go to the main menu
                if self.isMainMenu == False:
                    return menuState # If this menu is not the main menu then return 'main'
                else:
                    menuState = 'run' # If this is the main menu then turn menuState into 'run'


    def autocomplete_input(self, possible: list=None): # Creates an input that takes possible inputs as a list and provides a autocomplete function
        if 'libedit' in readline.__doc__: # If running python provided with mac then readline is non standard
            readline.parse_and_bind("bind ^I rl_complete") # Different keybind rules if running a mac
        else:
            readline.parse_and_bind("tab: complete") # Normal keybind rules
        readline.set_completer(TextCompleter(possible).complete)
        line = ''
        while line != 'exit':
            line = input('Enter name of user(exit to leave): ')
            if line in possible:
                return line
    
    def funcNotFound(self):
        print('Function not found')
        input('Press any key to continue')

    def get_user_input(self)-> str:

        user_input = input("").upper() #User input P/M/C/E
        opt = self.menu_options

        if user_input in opt:
            if 'special' in opt[user_input]:
                if opt[user_input]['special'] == 'back':
                    return 'back'
                elif opt[user_input]['special'] == 'main':
                    return 'main'
            elif 'class' in opt[user_input]:
                opt_class = opt[user_input]['class']
                new_menu = opt_class()
                if new_menu.print_options() == 'main':
                    return 'main'
                return 'run'
            elif 'function' in opt[user_input]:
                opt_func = opt[user_input]['function']
                run_func = getattr(self, opt_func, self.funcNotFound)
                self.clear()
                run_func()
                return 'run'
            else:
                return 'run'
        else:
            print(f'Invalid input: {user_input}')
            return 'run'

