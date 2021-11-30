from ui.MenuConstants import MenuConstants

class BaseMenu :
    def __init__(self):
        self.menu_constants = MenuConstants()
        self.menu_options = self.menu_constants.MENU_OPTIONS_DICT

    def print_options(self):
        for key in  self.menu_options :
            print(f"{key} {self.menu_options[key]['title']}")
        return self.get_user_input()

    def get_user_input(self):

        user_input = input("").upper() #User input P/M/C/E
        opt = self.menu_options

        if user_input in opt:
            if opt[user_input]['special']:
                if opt[user_input]['special'] == 'back':
                    return True
                elif opt[user_input]['special'] == 'main':
                    return 'main'
            elif opt[user_input]['class']:
                opt_class = opt[user_input]['class']
                new_menu = opt_class(self)
                if new_menu.print_options() == 'main':
                    return 'main'
            elif opt[user_input]['function']:
                opt_func = opt[user_input]['function']
                return False
            else:
                return False
        else:
            print(f'Invalid input: {user_input}')