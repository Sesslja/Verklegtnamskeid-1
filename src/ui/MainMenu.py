from ui.BaseMenu import BaseMenu

from ui.ContractorsMenu import ContractorsMenu
from ui.EmployeesMenu import EmployeesMenu
from ui.MaintenanceRequestMenu import MaintenanceRequestMenu
from ui.MaintenanceReportMenu import MaintenanceReportMenu
from ui.PropertiesMenu import PropertiesMenu


class MainMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Main Menu"
        self.isMainMenu = True
        self.menu_options = { 
            "1": {
                "title": "Properties",
                "access": "",
                "class": PropertiesMenu
            },  
            "2": {
                "title": "Maintenance Requests",
                "access": "",
                "class": MaintenanceRequestMenu
            },
            "3": {
                "title": "Maintenance Report",
                "access": "Manager",
                "class": MaintenanceReportMenu
            },     
            "4": {
                "title": "Contractors",
                "access": "",
                "class": ContractorsMenu
            },
            "5": {
                "title": "Employees",
                "access": "Manager",
                "class": EmployeesMenu
            },
            "Q": {
                "title": "Exit program",
                "access": "",
                "special": "quit"
            }
        }