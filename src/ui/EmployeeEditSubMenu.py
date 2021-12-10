
from model.AddressType import Address
from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI
try:
    from rich.prompt import Prompt, Confirm
except ModuleNotFoundError:
    pass

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
        ''' Update employee address '''
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        comfirm = input("Do you want to change employee address? [y/N]: ")
        if comfirm == "y":
            address = found_user.Address
            # old_country = address["country"]
            # old_city = address["city"]
            # old_zip = address["zip"]
            # new_country = input(f"Old country: {old_country}\nNew country:  ")
            # new_city = input(f"Old city: {old_city}\nNew city:  ")
            # new_zip = input(f"Old zip: {old_zip}\nNew zip:  ")
            new_country = Prompt.ask("Enter new country", default=address["country"])
            new_city = Prompt.ask("Enter new city", default=address["city"])
            new_zip = Prompt.ask("Enter new zip code", default=address["zip"])
            new_addr1 = Prompt.ask("Enter new address", default=address["address1"])

            print("Address successfully changed.")
        else:
            print("Okey, lets go back")
        self.waitForKeyPress()
        
    
    def edit_employee_name(self):
        ''' Update employee name '''
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        old_name = found_user.name
        new_name = input(f"Change name\n Old name: {old_name}\nNew name:  ")

        updated_user = self.userAPI.updateEmployeeInfo(found_user._id, {
            'name': new_name
        })
        print("Name successfully changed.")
        self.waitForKeyPress()

    def edit_employee_email(self):
        ''' Update employee email '''
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        old_email = found_user.email
        new_email = input(f"Change email\n Old email: {old_email}\nNew email:  ")

        updated_user = self.userAPI.updateEmployeeInfo(found_user._id, {
            'email': new_email
        })
        print("Email successfully changed.")
        self.waitForKeyPress()


    def edit_employee_ssn(self):
        ''' Update employee number '''
        found_user = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        old_ssn = found_user.ssn
        new_ssn = Prompt.ask('Change employee number?', default=old_ssn)

        updated_user = self.userAPI.updateEmployeeInfo(found_user._id, {
            'ssn': new_ssn
        })
        print("SSN successfully changed.")
        self.employeeSSN = new_ssn
        self.waitForKeyPress()


    def delete_employee(self):
        ''' Delete employee '''
        comfirm = input("Are you sure? \n[1] Yes!\n[other] Cancel\n: ")
        if comfirm == "1":
            try:
                employee_object = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
                self.userAPI.deleteEmployee(employee_object._id)
                print("Employee is deleted")
            except RecordNotFoundError:
                print("Employee not found")
        else:
            print("OK, no changes made")
        self.waitForKeyPress()

    def changeEmployeeStatus(self):
        ''' Change employee to manager and vice versa'''
        employee = self.userAPI.findEmployeeByEmployeeId(self.employeeSSN)
        confirm = False
        if employee.isManager: # Show if employee is a manager
            print('Employee is a manager')
            confirm = Confirm.ask('Do you want to demote the employee? ')
            if confirm:
                isManager = False
        else:
            confirm = Confirm.ask('Do you want to promote the employee to manager? ')
            if confirm:
                isManager = True
        
        if confirm:
            updated_user = self.userAPI.updateEmployeeInfo(employee._id, {
                'isManager': isManager
            })
            print(f"Sucess, Employee with number {self.employeeSSN} is now a manager" if isManager else f"Success, employee with number {self.employeeSSN} is no longer a manager")
        else :
            print("Okey, no changes made")
