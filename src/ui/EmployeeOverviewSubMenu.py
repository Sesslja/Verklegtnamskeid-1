from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI

class EmployeeOverviewSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.userApi = UserAPI()

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

    def all_employees_overview(self):
        employee_list = []
        for employee in employee_list:
            print(employee)

    def search_employee_by_name(self):
        employees = self.userApi.findEmployees()
        list_employee_names = []
        list_employee_ids = []
        for employee in employees:
            list_employee_names.append(employee.name)
            list_employee_ids.append(employee._id)
    
        employee_name = self.autocomplete_input(list_employee_names)
        employee_id = list_employee_ids[list_employee_names.index(employee_name)]
    
        found_employee = self.userApi.findOneEmployee(employee_id)
        print(found_employee)
        input('la')
    
        #employee_name = (input("Enter employee name: ")).upper()
        # employee_list = []
        # for item in employee_list:
        #     if employee_name == employee_name:
        #         print (item)
    
