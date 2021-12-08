import sys, os

try:
    import readline
except ImportError:
    pass
from ui.textCompleter import TextCompleter
from ui.Colors import color

try:
    from rich import box, print
    from rich.console import Console
    from rich.table import Table
    from rich.align import Align
    from rich.style import Style
    from rich.prompt import Prompt
    RICH_AVAILABLE = True
except ModuleNotFoundError:
    RICH_AVAILABLE = False

class BaseMenu :
    def __init__(self, logged_in_user=None):
        self.menu_options = {}
        self.clear = lambda: os.system('cls' if os.name=='nt' else 'clear') if not RICH_AVAILABLE else Console().clear()
        self.menu_title = str()
        self.isMainMenu = False
        self.failed = False
        self.loggedIn = False
        self.loggedInUser = self.login() if logged_in_user is None else logged_in_user
    
    def login(self, failed_attempt: bool=False):
        from logic.AuthLogic import AuthAPI
        authApi = AuthAPI()
        self.clear()
        print('Incorrect login details, please try again') if failed_attempt else ''
        userSsn = ""
        while userSsn == "":
            userSsn = Prompt.ask('Please enter your ID')
            self.clear()
        login_res = authApi.userLogin(userSsn)

        if login_res:
            self.loggedIn = True
            return login_res
        else:
            return self.login(failed_attempt=True)


    def print_options(self):
        if self.failed:
            return 'run'
        menuState = 'run'
        while menuState == 'run':
            self.clear()
            if not RICH_AVAILABLE:
                to_print = self.menu_title + '\n'
                # Checks if Rich module is installed, install with 'pip install rich'
                to_print = color('Rich package is not installed, program may not render correctly\n', backgroundColor='red') + to_print
                to_print += ("-"*30) + '\n'
                for key in  self.menu_options :
                    to_print += f"[{key}] {self.menu_options[key]['title']} \n"
                to_print += ("-"*30)
                print(to_print)
            else:
                menuTable = Table(show_header=False, show_lines=True)
                menuTable.title = self.menu_title
                menuTable.add_column()
                menuTable.add_column()
                for key in self.menu_options:
                    try:
                        if self.menu_options[key]['access'] == 'manager' and self.loggedInUser.isManager:
                            menuTable.add_row(key, self.menu_options[key]['title'])
                        elif self.menu_options[key]['access'] != 'manager':
                            menuTable.add_row(key, self.menu_options[key]['title'])
                    except KeyError:
                        menuTable.add_row(key, self.menu_options[key]['title'])
                menuTable.box = box.MINIMAL
                menuTable.caption = f'You are logged in as {self.loggedInUser.name}'
                menuTable_centered = Align.center(menuTable)
                print(menuTable_centered)

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
        '''Gets the user input, then directs that input into computeUserOptions.\n
        Only used in menus'''
        try:
            user_input = self.waitForKeyPress(print_text=False).upper() #User input
            return self.computeUserOptions(user_input)
        except KeyboardInterrupt:
            print('')
            if input('Are you sure you want to quit? (y/N): ').lower() == 'y':
                return 'quit'
            else:
                self.getUserInput()

    def computeUserOptions(self, user_input)-> str:
        ''' Finds what option the user input corresponds to.\n
        If it's a function, it runs the function.\n
        if it's a class it initiates the class\n
        There are also "special" values such as back, menu or quit'''
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
                new_menu = opt_class(logged_in_user=self.loggedInUser)
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
            #print(f'Invalid input: {user_input}')
            return 'run'

    def createTable(self, 
    header, 
    obj, 
    hide_header: bool=False,
    table_title: str=None, 
    line_between_records: bool=False, 
    return_table: bool=False, 
    justify_table: str='left',
    table_style: str='bright_yellow',
    color_newest: bool=False):

        if not RICH_AVAILABLE:
            return self.createTableNoDependency(header, obj, line_between_records)

        table = Table(show_lines=line_between_records)

        if type(header) is list:
            old_header = header
            header = {}
            for key in old_header:
                table.add_column(key)
                header.update({key: {}})
        else:
            for i, key in enumerate(header):
                try:
                    table.add_column(header[key]['display_name'])
                except KeyError:
                    table.add_column(key)
                try:
                    table.columns[i].justify = header[key]['justify']
                except KeyError:
                    pass
                try:
                    table.columns[i].style = header[key]['style']
                except KeyError:
                    pass
                try:
                    table.columns[i].header_style = header[key]['header_style']
                except KeyError:
                    pass
                
        for record in obj:
            try:
                record = record.__dict__
            except AttributeError:
                pass
            row_list = []
            for key in header:
                if key in record:
                    if type(record[key]) is list:
                        record[key] = ''.join([f'{list_val}'+(', ' if i < (len(record[key]) -1) else '') for i, list_val in enumerate(record[key])])
                    elif type(record[key]) is bool:
                        record[key] = 'True' if record[key] else 'False'
                    elif type(record[key]) is int:
                        record[key] = str(record[key])
                    elif type(record[key]) is float:
                        record[key] = str(round(record[key]))

                    try:
                        record[key] += header[key]['suffix']
                    except KeyError:
                        pass

                    row_list.append(record[key])
            table.add_row(*row_list)

        if table_title:
            table.title = table_title

        if color_newest:
            table.rows[table.row_count-1].style = 'bright_blue'

        table.caption = f'Found {len(obj)} entries.'
        table.row_styles = ['none', 'dim']
        table.border_style = Style.parse(table_style)
        table.box = box.ROUNDED
        table.show_header = not hide_header

        #if justify_table == 'center':
        #    print('heha')
        #    table_aligned = Align.center(table)
        #elif justify_table == 'right':
        #    table_aligned = Align.right(table)
        #elif justify_table == 'left':
        #    table_aligned = Align.left(table)
        #else:
        table_aligned = Align.center(table)

        if return_table:
            return table_aligned
        else:
            print(table_aligned)
            return ''


    def createTableNoDependency(self, header: list or dict, objList: list, line_between_records=False):
        '''Creates and returns a formatted table. \n
        header input is a list of those keys you want to include in the table\n
        \t Ex. header = ['name', 'email', 'ssn', 'isManager'] \n
        objList is a list of model objects'''
        if type(header) is list: 
            show_keys = {}
            for key in header:
                show_keys.update({key: {}})
        else:
            show_keys = header

        # Add length of each key to dictionary
        for key in show_keys:
            show_keys[key].update({'length': len(key)})
            try:
                show_keys[key]['special_color']
            except KeyError:
                show_keys[key].update({'special_color': None})
            try:
                show_keys[key]['display_name']
            except KeyError:
                show_keys[key].update({'display_name': key})
            try:
                show_keys[key]['prefix']
            except KeyError:
                show_keys[key].update({'prefix': ''})
            try:
                show_keys[key]['suffix']
            except KeyError:
                show_keys[key].update({'suffix': ''})


        # Finds max length for each key
        for record in objList:
            try:
                record = record.__dict__
            except AttributeError:
                pass
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
            .format(*[show_keys[key]['display_name'] for key in show_keys])) + '\n'# Input all header keys
        
        printout += '|'+('-'*total_length)+'|\n' if line_between_records else ''

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
            try:
                record = record.__dict__
            except AttributeError:
                pass
            printout += (
                ''.join([
                    ((''.join(
                        ['| {:<',str(show_keys[key]['length']),'}', (" |" if (len(show_keys) - 1) is i else " " )]
                    )) #if type(record[key]) is not list else (''.join(
                       # ['| {:<',str(show_keys[key]['length']),'}',(" |" if (len(show_keys) - 1) is i else " " )]
                       # ).format(''.join([x+(', ' if i2 < (len(record[key])-1) else '') for i2, x in enumerate(record[key])]))
                    ) for i, key in enumerate(show_keys)
                ])
                .format(*[(str(show_keys[key]['prefix'])+str(record[key])+str(show_keys[key]['suffix']) if type(record[key]) is not list else ''.join(
                    [x+(', ' if i2 < (len(record[key])-1) else '') for i2, x in enumerate(record[key])]
                )) for key in show_keys]))+'\n'+(('|'+('-'*total_length)+'|\n') if line_between_records else '')

        # Adds bottom line
        printout += '|'+color((''.join([' {:<',str(total_length-2), '} '])).format('Nr. of records: '+str(len(objList))), 'black', 'blue', 'underline')+'|\n'
        printout += ' '+('‾'*total_length)+' '
            
        print(printout)
        return ''

    def waitForKeyPress(self, text_to_print: str='Press any key to continue ', print_text: bool=True):
        ''' Wait for a key press on the console and return it. '''
        # Script gotten from https://stackoverflow.com/questions/983354/how-to-make-a-python-script-wait-for-a-pressed-key
        # Which was rewritten code from the Python Docs
        if print_text:
            print(text_to_print, end='')
        if os.name == 'nt': # If user is on windows then use msvcrt
            import msvcrt
            key = msvcrt.getch()
            if ord(key) == 3:
                raise KeyboardInterrupt
            return key.decode('ASCII')
        else: # If user is on a unix based system then use termios
            import termios
            fd = sys.stdin.fileno()

            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)

            try:
                return sys.stdin.read(1)
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


