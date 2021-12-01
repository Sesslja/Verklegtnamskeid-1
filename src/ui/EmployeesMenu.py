from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI
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
                "function": "employeesOverview"
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
        address = input("Enter address: ")

        self.userapi.createEmployee(name, email, ssn, address)

        

    def employeesOverview(self):
        print('show me employ over')