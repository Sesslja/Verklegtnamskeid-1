import os

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
            print(self.menu_title)
            print("-"*30)
            for key in  self.menu_options :
                print(f"[{key}] {self.menu_options[key]['title']}")
            print("-"*30)
            menuState = self.get_user_input()
            if menuState == 'main':
                if self.isMainMenu == False:
                    return menuState
                else:
                    menuState = 'run'

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
                run_func = getattr(self, opt_func, None)
                self.clear()
                run_func()
                return 'run'
            else:
                return 'run'
        else:
            print(f'Invalid input: {user_input}')
            return 'run'