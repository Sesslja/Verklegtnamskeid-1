
from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI

class EmployeeEditMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.userAPI = UserAPI()
        self.employeeSSN = self.employeeSSN_input()

        self.menu_title = f"Edit Employee\n SSN: {self.employeeSSN}"
        
        self.menu_options = {
            "1": {
                "title": "Edit name",
                "access": "manager",
                "function": "edit_employee_name"
            },
            "4": {
                "title": "Delete employee",
                "access": "manager",
                "function": "delete_employee"
            },
            "X": {
                "title": "Return to previous page",
                "access": "",
                "special": "back"
            },
            "M": {
                "title": "Return to main menu",
                "special": "main"
            }
        }

    def employeeSSN_input(self, retry: bool= False):
        self.clear()
        print('No User found\nplease input a correct one') if retry else None
        employeeSSN_input = input("Please enter employee ssn: ")

        try:
            found_employee = self.userAPI.findEmployeeByEmployeeId(employeeSsn=employeeSSN_input)
        except RecordNotFoundError:
            return self.employeeSSN_input(True)
        
        return found_employee.ssn
    
    def edit_employee_name(self):
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        new_name = input("Enter new name: ")


    def edit_user_ssn(self):
        pass

    def delete_employee(self):
        comfirm = input("Are you sure? \n[1] Yes!\n[other] Cancel")
        if comfirm == "1":
            if self.userApi.deleteEmployee(self.employeeSSN) == True:
                print("Employee deleted")
            else:
                print("Employee not found")
        self.waitForKeyPress()