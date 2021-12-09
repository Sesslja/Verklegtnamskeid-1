
from model.AddressType import Address
from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI

class EmployeeEditMenu(BaseMenu):
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.userAPI = UserAPI()
        self.employeeSSN = self.employeeSSN_input()
        if self.employeeSSN is 'q':
            self.failed = True

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
            "6": {
                "title": "Change employee status",
                "access": "",
                "function": "changeEmployeeStatus"
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
        employeeSSN_input = input("Please input the employee's SSN ([Q] to Quit): ")
        if employeeSSN_input.lower() == 'q':
            return 'q'

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
        comfirm = input("Are you sure? \n[1] Yes!\n[other] Cancel\n: ")
        if comfirm == "1":
            try:
                employee_object = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
                self.userAPI.deleteEmployee(employee_object._id)
                print("Employee is deleted")
            except FileNotFoundError:
                print("Employee not found")
        else:
            print("OK, no changes made")
        self.waitForKeyPress()

    def changeEmployeeStatus(self):

        confirm = input(f"Do you want to change {self.employeeSSN} to manager? (Y/N): ")

        if confirm.lower() == "y":
            
            employee_object = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
            updated_user = self.userAPI.updateEmployeeInfo(employee_object._id, {
                'isManager': True
            })
            print("Sucess, Employee is now a manager")
        else :
            print("Okey, no changes made")