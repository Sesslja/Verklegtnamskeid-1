from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI

class EmployeeOverviewSubMenu(BaseMenu):
    '''Shows sub menu to employee overview'''
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
                "title": "Search employee by id",
                "function": "search_employee_by_id"
            },
            "3": {
                "title": "Edit employee",
                "function": "update_employee"
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
        '''Shows all employees of NAN'''
        try:
            employee_list = self.userApi.findEmployees()

            # What keys from record list to use
            show_keys = ['name', 'email', 'ssn']
            print(self.createTable(show_keys, employee_list))
        except ValueError:
            print("No employees to show")
        self.waitForKeyPress()

    def search_employee_by_id(self):
        '''option to search for employees \ngiven employee ID'''
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

    def update_employee(self):
        '''option to edit employee \ngiven employee SSN'''
        '''Býður notenda upp á að breyta eiginleikum starfsmanns\ngefið að notandi viti ssn starfsmanns'''
        employee_id = input("Enter employee SSN: ")
        try:
            employee = self.userApi.findEmployeesByEmployeeId(employee_id)
            try:
                employee['ERROR']
                print("Employee not found")
            except TypeError:
                print(employee)
                dictionary = employee[0].__dict__
                for i, key in enumerate(dictionary):
                    print(f"| {key:<15}:  {(dictionary[key])}")
                factor = input("\nSelect factor you want to change: ")

        except ValueError:
            print("No employee found")



        self.userApi.updateEmployeeInfo('suhdfsuohf898f2-32f2h3f',{
            'name': 'Bónus'
        })

    def delete_employee(self):
        employee_ssn = input("Enter employees SSN: ")
        if self.userApi.deleteEmployee(employee_ssn) == True:
            print("Employee deleted")
        else:
            print("Employee not found")
        self.waitForKeyPress()

    def find_employees_by_country(self):
        pass

    def find_employee(self):
        pass

    def find_manager(self):
        pass

    def update_employee_info(self):
        pass

    def find_by_attributy(self):
        pass
    

