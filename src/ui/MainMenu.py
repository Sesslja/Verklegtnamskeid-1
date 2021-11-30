from MenuConstants import MENU_OPTIONS_DICT

from PropertiesMenu import PropertiesMenu #Properties

from MaintenanceMenu import MaintenanceMenu #Maintenance

from ContractorsMenu import ContractorsMenu #Contractors

from EmployeesMenu import EmployeesMenu #Employees

class MainMenu :

    def __init__(self):
        self.menu_options = MENU_OPTIONS_DICT

    def print_options(self):
        for key in  self.menu_options :
            print(f"{key} {self.menu_options[key]['title']}")
        return self.get_user_input()

    def get_user_input(self):

        user_input = input("").upper() #User input P/M/C/E
        opt = self.menu_options

        if user_input in opt:
            if opt[user_input]['special']:
                if opt[user_input]['special'] is 'back':
                    return True
                elif opt[user_input]['special'] is 'main':
                    return 'main'
            elif opt[user_input]['class']:
                opt_class = opt[user_input]['class']
                new_menu = opt_class()
                if new_menu.print_options() is 'main':
                    return 'main'
            elif opt[user_input]['function']:
                opt_func = opt[user_input]['function']
                return False
            else:
                return False
        else:
            print(f'Invalid input: {user_input}')
        


        if user_input == "1":
            p_menu = PropertiesMenu()
            return_option = p_menu.print_options()
        elif user_input == "2":
            m_menu = MaintenanceMenu()
            return_option = m_menu.print_options() 
        elif user_input == "3":
            c_menu = ContractorsMenu()
            return_option = c_menu.print_options()
        elif user_input == "4":
            e_menu = EmployeesMenu()
            return_option = e_menu.print_options()
        elif user_input == "R" :
            return "R"
        elif user_input == "M" :
            return "M"
        else:
            print("Invalid Input ")