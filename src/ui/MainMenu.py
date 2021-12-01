from ui.BaseMenu import BaseMenu

from ui.ContractorsMenu import ContractorsMenu
from ui.EmployeesMenu import EmployeesMenu
from ui.MaintenanceMenu import MaintenanceMenu
from ui.PropertiesMenu import PropertiesMenu


class MainMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Main Menu"

        self.menu_options = { 
            "P": {
                "title": "Properties",
                "access": "",
                "class": PropertiesMenu
            },  
            "R": {
                "title": "Maintenance Requests",
                "access": "",
                "class": MaintenanceMenu
            },     
            "C": {
                "title": "Contractors",
                "access": "",
                "class": ContractorsMenu
            },
            "E": {
                "title": "Employees",
                "access": "Manager",
                "class": EmployeesMenu
            }
        }