from ui.BaseMenu import BaseMenu

class EmployeesMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Employees Menu"

        self.menu_options = {
            "A": {
                "title": "Create employee",
                "function": "createEmployee"
            },                     
            "B": {
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
        print('create me employee')

    def employeesOverview(self):
        print('show me employ over')