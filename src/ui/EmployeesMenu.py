from ui.EmployeeEditSubMenu import EmployeeEditMenu
from model.AddressType import Address
from ui.BaseMenu import BaseMenu
from logic.UserLogic import UserAPI
from ui.EmployeeOverviewSubMenu import EmployeeOverviewSubMenu
from model.AddressType import Address
from data.DBError import RecordNotFoundError
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
        employee_num_exist= False
        while employee_num_exist==False:
            ssn = input("Enter employee number: ")
            try:
                self.userapi.findEmployeeByEmployeeId(ssn)
                print('A employee already exists with that number, please enter another one.')
            except RecordNotFoundError:
                employee_num_exist = True
        phone_input = None
        phone_list = []
        while phone_input != "":
            phone_input = input("Enter phone number (Empty line to continue): ")
            if phone_input != "":
                phone_list.append(phone_input)
        country = input("Enter country: ")
        city = input("Enter city: ")
        zip_code = input("Enter zip code: ")
        addr1 = input("Enter address: ")
        addr2 = input("Address 2: ")
        addr2 = addr2 if addr2 is not "" else None # If we don't get an input then we want it as None
        addr3 = input("Address 3: ")
        addr3 = addr3 if addr3 is not "" else None # Same here as above
        
        address = Address(country=country, city=city, zip=zip_code, address1=addr1, address2=addr2, address3=addr3) # Create address object

        isManager = True if isManager == "y" else False

        self.userapi.createEmployee(name=name, email=email, ssn=ssn, address=address, isManegar=isManager, phone=phone_list) # Create employee
        try:
            print(Text.from_markup(f":white_check_mark: Hurrah! {name} created as employee"))
        except:
            print(f"Hurrah! {name} created as employee")
        self.waitForKeyPress()
