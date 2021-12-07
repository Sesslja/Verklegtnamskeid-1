from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI
from ui.EmployeeOverviewSubMenu import EmployeeOverviewSubMenu
from model.AddressType import Address

class EmployeesMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.userapi = UserAPI()

        self.menu_title = "Employees Menu"

        self.menu_options = {
            "1": {
                "title": "Create employee",
                "access": "Manager",
                "function": "createEmployee"
            },                     
            "2": {
                "title": "Employees overview",
                "class": EmployeeOverviewSubMenu
            },                  
            "X": {
                "title": "Return to previous page",
                "special": "back"
            },
            "M": {
                "title": "Return to main menu",
                "special": "main"
            }
        }

    def createEmployee(self):
        name = input("Enter employee name: ")
        email = input("Enter email: ")
        ssn = input("Enter Social-Security number: ")
        country = input("enter country: ")
        city = input("Enter city: ")
        zip_code = input("Enter zip code: ")
        address = Address(country, city, zip_code)

        self.userapi.createEmployee(name, email, ssn, address)
