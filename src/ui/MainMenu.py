from ui.BaseMenu import BaseMenu
from ui.MaintenanceMenu import MaintenanceMenu
from ui.MaintenanceReportMenu import MaintenanceReportMenu
from ui.ContractorsMenu import ContractorsMenu
from ui.EmployeesMenu import EmployeesMenu
from ui.MaintenanceRequestMenu import MaintenanceRequestMenu
from ui.PropertiesMenu import PropertiesMenu


class MainMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Main Menu"
        self.isMainMenu = True
        self.menu_options = { 
            "P": {
                "title": "Properties",
                "access": "",
                "class": PropertiesMenu
            },  
            "M": {
                "title": "Maintenance",
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
            },
            "Q": {
                "title": "Exit program",
                "access": "",
                "special": "quit"
            }
        }