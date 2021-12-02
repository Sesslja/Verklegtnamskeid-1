from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI

class EmployeeOverviewSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.userApi = UserAPI()

        self.menu_title = "Employees Menu\nEmployee Overview"

        self.menu_options = {
            "1": {
                "title": "Search employee by id",
                "function": "search_employee_by_id"
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

    def all_employees_overview(self):
        employee_list = self.userApi.findEmployees()
        if len(employee_list) == 0:
            print("No employees to show ")
        else:
            for employee in employee_list:
                print (employee)

    def search_employee_by_id(self):
        employee_id = None
        while employee_id == None:
            try:
                employee_id = int(input("Enter employee ID: "))
            except ValueError:
                print("Please enter a valid ID")

        employee_list = self.userApi.findEmployeesByEmployeeId(employee_id)
        if len(employee_list) == 0:
            print("employee not found!")
            employee_id = None
        else:
            for employee in employee_list:
                print (employee)


