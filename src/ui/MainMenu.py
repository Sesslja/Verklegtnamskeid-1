from ui.BaseMenu import BaseMenu
from ui.MaintenanceMenu import MaintenanceMenu
from ui.MaintenanceReportMenu import MaintenanceReportMenu
from ui.ContractorsMenu import ContractorsMenu
from ui.EmployeesMenu import EmployeesMenu
from ui.MaintenanceMenu import MaintenanceMenu
from ui.PropertiesMenu import PropertiesMenu


class MainMenu(BaseMenu):
    '''Shows main menu and restricts access to employees'''
    def __init__(self):
        super().__init__()

        self.menu_title = "Main Menu"
        self.isMainMenu = True
        self.PropertiesMenu = PropertiesMenu
        self.MaintenanceMenu = MaintenanceMenu
        self.ContractorsMenu = ContractorsMenu
        self.EmployeesMenu = EmployeesMenu


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
                "access": "Manager",
                "class": EmployeesMenu
            },
            "5": {
                "title": "Employees",
                "access": "Manager",
                "function": "printTable"
            },
            "Q": {
                "title": "Exit program",
                "access": "",
                "special": "quit"
            }
        }

    def printTable(self):
        self.createRichTable(['la'], ['heho'])