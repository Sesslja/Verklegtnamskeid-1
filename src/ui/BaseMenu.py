import sys, os
try:
    import readline
except ImportError:
    pass
from ui.textCompleter import TextCompleter
from ui.Colors import color

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
            menuState = self.getUserInput()
            if menuState == 'main': # Check if the user wanted to go to the main menu
                if self.isMainMenu == False:
                    return menuState # If this menu is not the main menu then return 'main'
                else:
                    menuState = 'run' # If this is the main menu then turn menuState into 'run'
            elif menuState == 'quit':
                self.clear()
                print('Goodbye!')
                exit()

    def getUserInput(self):
        try:
            user_input = None
            while user_input is None:
                user_input = input("").upper() #User input P/M/C/E
            return self.computeUserOptions(user_input)
        except KeyboardInterrupt:
            print('')
            if input('Are you sure you want to quit? (y/N): ').lower() == 'y':
                return 'quit'
            else:
                self.getUserInput()

    def computeUserOptions(self, user_input)-> str:
        opt = self.menu_options

        if user_input in opt:
            if 'special' in opt[user_input]:
                if opt[user_input]['special'] == 'back':
                    return 'back'
                elif opt[user_input]['special'] == 'main':
                    return 'main'
                elif opt[user_input]['special'] == 'quit':
                    return 'quit'
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

    def createTable(self, header=list, objList=list):
        '''Creates and returns a formatted table. \n
        header input is a list of those keys you want to include in the table\n
        \t Ex. header = ['name', 'email', 'ssn', 'isManager'] \n
        objList is a list of model objects'''
        show_keys = {}
        for key in header:
            show_keys.update({key: {}})

        # Add length of each key to dictionary
        for key in show_keys:
            show_keys[key].update({'length': len(key)})
            try:
                show_keys[key]['special_color']
            except KeyError:
                show_keys[key].update({'special_color': None})

        # Finds max length for each key
        for record in objList:
            record = record.__dict__
            for key in show_keys:
                record_keyVal = len(str(record[key]))
                if record_keyVal > show_keys[key]['length']:
                    show_keys[key]['length'] = record_keyVal

        # Find total character length of longest line
        total_length = sum([(
            show_keys[key]['length'] + (2 if (len(show_keys) - 1) is i else 3)
            ) for i, key in enumerate(show_keys)])

        # Add top line to table printout
        printout = ''#.join([('-'*total_length),'\n'])

        # Add key header to table printout
        printout += (''.join([
                (color(''.join(
                    [   # Bit convoluted but, part before the if statement is the normal printout of the header,        the part after the if statement is if header list has a 'special_color' key which then colors that column
                        '| ',(''.join(['{:<',str(show_keys[key]['length']),'}']) ),  # Specify length of field
                        (" |" if (len(show_keys) - 1) is i else " " ) # Put a pipe if this is the end field
                    ]
                ), 'black',
                'white')) for i, key in enumerate(show_keys) # For each header value
            ])
            .format(*show_keys)) + '\n'# Input all header keys

        # printout += color(
        #     (''.join([
        #         (color(''.join(
        #             [   # Bit convoluted but, part before the if statement is the normal printout of the header,        the part after the if statement is if header list has a 'special_color' key which then colors that column
        #                 '| ',(''.join(['{:<',str(show_keys[key]['length']),'}']) if show_keys[key]['special_color'] is None else color(''.join(['{:<',str(show_keys[key]['length']),'}']), show_keys[key]['special_color']['color'], show_keys[key]['special_color']['background']) ),  # Specify length of field
        #                 (" |" if (len(show_keys) - 1) is i else " " ) # Put a pipe if this is the end field
        #             ]
        #         ), 'white' if show_keys[key]['special_color'] is None else show_keys[key]['special_color']['color'])) for i, key in enumerate(show_keys) # For each header value
        #     ])
        #     .format(*show_keys)) # Input all header keys
        # , 'black', 'white') + '\n'
        
        # Add lines under header keys
        # printout += '|'+('-'*total_length)+'|\n'

        # Adds values for each record to table printout
        for record in objList:
            record = record.__dict__
            printout += (
                ''.join([
                    (''.join(
                        ['| {:<',str(show_keys[key]['length']),'}', (" |" if (len(show_keys) - 1) is i else " " )]
                    )) for i, key in enumerate(show_keys)
                ])
                .format(*[record[key] for key in show_keys]))+'\n'

        # Adds bottom line
        printout += color((''.join(['| {:<',str(total_length-2), '} |\n'])).format('Nr. of records: '+str(len(objList))), 'black', 'blue', 'underline')
        printout += ' '+('‾'*total_length)+' '
            
        return printout

    def waitForKeyPress(self):
        ''' Wait for a key press on the console and return it. '''
        # Script gotten from https://stackoverflow.com/questions/983354/how-to-make-a-python-script-wait-for-a-pressed-key
        # Which was rewritten code from the Python Docs
        print('Press any key to continue ', end='')
        if os.name == 'nt': # If user is on windows then use msvcrt
            import msvcrt
            msvcrt.getch()
        else: # If user is on a unix based system then use termios
            import termios
            fd = sys.stdin.fileno()

            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)

            try:
                sys.stdin.read(1)
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)


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


