from constants import MENU_OPTIONS_DICT

from PropertiesMenu import PropertiesMenu #Properties

from MaintenanceMenu import MaintenanceMenu #Maintenance

from ContractorsMenu import ContractorsMenu #Contractors

from EmployeesMenu import EmployeesMenu #Employees

class MainMenu :

    def __init__(self):
        self.menu_options = MENU_OPTIONS_DICT

    def print_options(self):
        for key in  self.menu_options :
            print(f"{key} {self.menu_options[key]}")
        self.get_user_input()

    def get_user_input(self):

        while True :

            user_input = input("").upper() #User input P/M/C/E

            if user_input == "P":
                p_menu = PropertiesMenu()
                p_menu.print_options()
            elif user_input == "M":
                m_menu = MaintenanceMenu()
                m_menu.print_options() 
            elif user_input == "C":
                c_menu = ContractorsMenu()
                c_menu.print_options()
            elif user_input == "E":
                e_menu = EmployeesMenu()
                e_menu.print_options()
            else:
                print("Invalid Input ")
