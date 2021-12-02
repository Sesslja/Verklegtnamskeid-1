from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI

class EmployeeOverviewSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Employees Menu\nEmployee Overview"

        self.menu_options = {
            "1": {
                "title": "Search by name",
                "function": "search_employee_by_name"
            },                     
            "2": {
                "title": "See all employees",
                "function": "all_employees_overview"
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

def all_employees_overview():
    employee_list = []
    for employee in employee_list:
        print(employee)

def search_employee_by_name():
    employee_name = (input("Enter employee name: ")).upper()
    # employee_list = []
    # for item in employee_list:
    #     if employee_name == employee_name:
    #         print (item)
    def all_employees_overview(self):
        pass

    def search_employee_by_name(self):
        input('ha: ')

