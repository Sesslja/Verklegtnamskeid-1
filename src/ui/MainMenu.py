from ui.BaseMenu import BaseMenu
from ui.MaintenanceMenu import MaintenanceMenu
from ui.MaintenanceReportMenu import MaintenanceReportMenu
from ui.ContractorsMenu import ContractorsMenu
from ui.EmployeesMenu import EmployeesMenu
from ui.MaintenanceMenu import MaintenanceMenu
from ui.PropertiesMenu import PropertiesMenu
from ui.DestinationsMenu import DestinationsMenu


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
            "Q": {
                "title": "Exit program",
                "access": "",
                "special": "quit"
            }
        }

