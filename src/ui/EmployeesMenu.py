from ui.EmployeeEditSubMenu import EmployeeEditMenu
from model.AddressType import Address
from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI
from ui.EmployeeOverviewSubMenu import EmployeeOverviewSubMenu
from model.AddressType import Address
try:
    from rich.text import Text
except ModuleNotFoundError:
    pass

class EmployeesMenu(BaseMenu):
    '''Shows employee options'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.userapi = UserAPI()

        self.menu_title = "Employees Menu"

        self.menu_options = {
            "1": {
                "title": "Create employee",
                "access": "manager",
                "function": "createEmployee"
            },                     
            "2": {
                "title": "Employees overview",
                "access": "manager",
                "class": EmployeeOverviewSubMenu
            },  
            "3": {
                "title": "Edit Employee",
                "class": EmployeeEditMenu,
                "access": ""
            },                 
            "X": {
                "title": "Return to previous page",
                "special": "back",
                "access": ""
            },
            "M": {
                "title": "Return to main menu",
                "special": "main",
                "access": ""
            }
        }

    def createEmployee(self):
        '''option to create new employee'''
        name = input("Enter employee name: ")
        isManager = input("Is employee Manager? [y/N]: ").lower()
        email = input("Enter email: ")
        ssn = input("Enter Social-Security number: ")
        country = input("enter country: ")
        city = input("Enter city: ")
        zip_code = input("Enter zip code: ")
        addr1 = input("Enter address: ")
        
        address = Address(country=country, city=city, zip=zip_code, address1=addr1) # Create address object

        isManager = True if isManager == "y" else False

        self.userapi.createEmployee(name, email, ssn, address, isManager) # Create employee
        try:
            print(Text.from_markup(f":white_check_mark: Hurrah! {name} created as employee"))
        except:
            print(f"Hurrah! {name} created as employee")
        self.waitForKeyPress()
