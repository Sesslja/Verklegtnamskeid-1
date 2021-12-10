from ui.BaseMenu import BaseMenu
from ui.ContractorsMenu import ContractorsMenu
from ui.EmployeesMenu import EmployeesMenu
from ui.PropertiesMenu import PropertiesMenu
from ui.DestinationsMenu import DestinationsMenu
from ui.MaintenanceMenu import MaintenanceMenu
import time


class MainMenu(BaseMenu):
    '''Shows main menu and restricts access to employees'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Main Menu"
        self.isMainMenu = True
        self.PropertiesMenu = PropertiesMenu
        self.MaintenanceMenu = MaintenanceMenu
        self.ContractorsMenu = ContractorsMenu
        self.EmployeesMenu = EmployeesMenu
        self.DestinationsMenu = DestinationsMenu


        self.menu_options = { 
            "1": {
                "title": "Properties",
                "access": "",
                "class": PropertiesMenu
            },  
            "2": {
                "title": "Maintenance Menu",
                "access": "",
                "class": MaintenanceMenu
            },   
            "3": {
                "title": "Contractors",
                "access": "",
                "class": ContractorsMenu
            },
            "4": {
                "title": "Employees",
                "access": "manager",
                "class": EmployeesMenu
            },
            "5": {
                "title": "Destinations",
                "access": "",
                "class": DestinationsMenu
            },
            "D": {
                "title": "Divide by Zero",
                "access": "",
                "function": "divideByZero"
            },
            "Q": {
                "title": "Exit program",
                "access": "",
                "special": "quit"
            }
        }

    def divideByZero(self):
        ''' So you want to play that game? '''
        confirmation = input('Are you sure you want to divide by zero? [y/n]: ').lower()
        if confirmation == "y":
            for i in range(5, 0, -1):
                self.clear()
                print(f"Dividing by zero in: {i}")
                time.sleep(1)
            for i in range(0, 5):
                self.clear()
                print("Initiating division ", ("(       )" if i <= 1 else ("(   /   )" if i <= 2 else ("( 1 /   )" if i <= 3 else ("( 1 / 0 )")))))
                time.sleep(1)
            print(str( 1 / 0 ))