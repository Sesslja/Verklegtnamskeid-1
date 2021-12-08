
from model.AddressType import Address
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
                "access": "",
                "function": "edit_employee_name"
            },
            "2": {
                "title": "Edit employee SSN",
                "access": "",
                "function": "edit_employee_ssn"
            },
            "3": {
                "title": "Edit employee email",
                "access": "",
                "function": "edit_employee_email"
            },
            "4": {
                "title": "Edit employee address",
                "access": "",
                "function": "edit_employee_address"
            },
            "5": {
                "title": "Delete employee",
                "access": "",
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

    def edit_employee_address(self):
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        comfirm = input("Do you want to change employee address?\n[1] Yes\n[2] No\n: ")
        if comfirm == "1":
            address = found_user.Address
            old_country = address["country"]
            old_city = address["city"]
            old_zip = address["zip"]
            new_country = input(f"Old country: {old_country}\nNew country:  ")
            new_city = input(f"Old city: {old_city}\nNew city:  ")
            new_zip = input(f"Old zip: {old_zip}\nNew zip:  ")
            print("Address successfully changed.")
        else:
            print("Okey, lets go back")
        self.waitForKeyPress()
        
    
    def edit_employee_name(self):
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        old_name = found_user.name
        new_name = input(f"Change name\n Old name: {old_name}\nNew name:  ")

        updated_user = self.userAPI.updateEmployeeInfo(found_user._id, {
            'name': new_name
        })
        print("Name successfully changed.")
        self.waitForKeyPress()

    def edit_employee_email(self):
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        old_email = found_user.email
        new_email = input(f"Change email\n Old email: {old_email}\nNew email:  ")

        updated_user = self.userAPI.updateEmployeeInfo(found_user._id, {
            'email': new_email
        })
        print("Email successfully changed.")
        self.waitForKeyPress()


    def edit_employee_ssn(self):
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        old_ssn = found_user.ssn
        new_ssn = input(f"Change SSN\nOld SSN: {old_ssn}\nNew SSN:  ")

        updated_user = self.userAPI.updateEmployeeInfo(found_user._id, {
            'ssn': new_ssn
        })
        print("SSN successfully changed.")
        self.waitForKeyPress()


    def delete_employee(self):
        comfirm = input("Are you sure? \n[1] Yes!\n[other] Cancel")
        if comfirm == "1":
            if self.userApi.deleteEmployee(self.employeeSSN) == True:
                print("Employee deleted")
            else:
                print("Employee not found")
        self.waitForKeyPress()