from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI
from data.DBError import RecordNotFoundError
from rich.prompt import Prompt

class EmployeeOverviewSubMenu(BaseMenu):
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.userApi = UserAPI()

        self.menu_title = "Employees Menu\nEmployee Overview"

        self.menu_options = {
            "1": {
                "title": "Show all employees",
                "function": "allEmployeesOverview"
            },
            "2": {
                "title": "Find employee by employee Number",
                "function": "findEmployeeByEmplyeeNum"
            },
            "3": {
                "title": "Find employee by country",
                "function": "findEmployeesByCountry"
            },
            "4": {
                "title": "Find managers by Country",
                "function": "findManagerByCountry"
            },
            "5": {
                "title": "Find all managers",
                "function": "findManagers"
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

    def allEmployeesOverview(self):
        '''Shows all employees working for NAN'''
        try:
            employee_list = self.userApi.allEmployeesOverview()
            # What keys from record list to use
            show_keys = ['name', 'email', 'ssn', 'isManager']
            print(self.createTable(show_keys, employee_list))

        except RecordNotFoundError:
            print("No employees to show")
        self.waitForKeyPress()

    def findEmployeeByEmplyeeNum(self):
        '''Option to find employee by employee number'''
        employee_num = Prompt.ask('Please enter employee number: ')
        try:
            found_employee = self.userApi.findEmployeeByEmployeeId(employee_num)

            header = ['1', '2']

            single_employee_to_table_list = [
                {'1': 'Name', '2': found_employee.name},
                {'1': 'Email', '2': found_employee.email},
            ]

            self.createTable(header, 
            single_employee_to_table_list,
            hide_header=True,
            line_between_records=True)
        except RecordNotFoundError:
            print('User not found')

        self.waitForKeyPress()


    def findEmployeesByCountry(self):
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


    def findManagerByCountry(self):
        '''Option to search for manager \n given country'''
    
        country = Prompt.ask('Please enter a country')
        try:
            manager_list = self.userApi.findManagersByCountry(country)

            for record in manager_list:
                record.name 
            
            if len(manager_list) == 0:
                print("No manager found!")
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, manager_list))

        except RecordNotFoundError:
            print("No manager found")
        self.waitForKeyPress()

    def findManagers(self):
        ismanager = True
        try:
            employee_list = self.userApi.findManagers()
            # What keys from record list to use
            show_keys = ['name', 'email', 'ssn', 'isManager']
            print(self.createTable(show_keys, employee_list))

        except RecordNotFoundError:
            print("No employees to show")
        self.waitForKeyPress()
    