from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI
from data.DBError import RecordNotFoundError
try: 
    from rich.prompt import Prompt
except:
    None
 
class EmployeeOverviewSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.userApi = UserAPI()

        self.menu_title = "Employees Menu\nEmployee Overview"

        self.menu_options = {
            "1": {
                "title": "See all employees",
                "function": "all_employees_overview"
            },
            "2": {
                "title": "Find employee by employeeID",
                "function": "search_employee_by_id"
            },
            "3": {
                "title": "Find employee by country",
                "function": "find_employees_by_country"
            },
            "4": {
                "title": "Find one employee by ID",
                "function": "find_one_employee"
            },
            "5": {
                "title": "Find managers",
                "function": "find_managers_by_country"
            },
            "6": {
                "title": "Find all managers",
                "function": "find_managers"
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
        '''Shows all employees working for NAN'''
        try:
            employee_list = self.userApi.allEmployeesOverview()
            # What keys from record list to use
            show_keys = ['name', 'email', 'ssn', 'isManager']
            print(self.createTable(show_keys, employee_list))

        except RecordNotFoundError:
            print("No employees to show")
        self.waitForKeyPress()

    def search_employee_by_id(self):
        employee_id = None
        while employee_id == None:
            try:
                employee_id = int(input("Enter employee ID: "))
            except ValueError:
                print("Please enter a valid ID")
        try:
            employee_list = self.userApi.findEmployeesByEmployeeId(employee_id)
            if len(employee_list) == 0:
                print("employee not found!")
                employee_id = None
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, employee_list))
        except ValueError:
            print("No employee found")
        self.waitForKeyPress()


    def find_employees_by_country(self):
        '''Option to search for employees \ngiven country'''
        country = None
        while country == None:
            try:
                country = input("Enter a Country: ")
            except ValueError:
                print("Please enter a valid Country")
        try:
            country_list = self.userApi.findEmployeesByCountry(country)
            if len(country_list) == 0:
                print("No employee found by this country!")
                country = None
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, country_list))
        except ValueError:
            print("No employee found")
        self.waitForKeyPress()


    def find_managers_by_country(self):
        '''Option to search for manager \n given country'''
    
        country = Prompt.ask('Please enter a country')
        try:
            manager_list = self.userApi.findManagersByCountry(country)

            for record in manager_list:
                name = record.name 
                print(name)

        except RecordNotFoundError:
            print("Manager not found")
        self.waitForKeyPress()



    def find_by_attributy(self):
        pass

    def find_one_employee(self):
        pass