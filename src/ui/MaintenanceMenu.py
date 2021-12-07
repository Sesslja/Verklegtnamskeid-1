from model.AddressType import Address
from model.PropertyModel import Property
from model.MaintenanceRequestModel import MaintenanceRequest
from ui.BaseMenu import BaseMenu
from ui.MaintenanceReportMenu import MaintenanceReportMenu
from ui.MaintenanceRequestMenu import MaintenanceRequestMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from logic.MaintReportLogic import MaintReportAPI
from logic.PropertyLogic import PropertyAPI
from logic.ContractorLogic import ContractorAPI
from data.database import DB
from data.DBError import RecordNotFoundError
from logic.UserLogic import UserAPI
from ui.EmployeesMenu import EmployeesMenu
from ui.PropertiesMenu import PropertiesMenu
from ui.MaintenanceRequestMenu import MaintenanceRequestMenu


class MaintenanceMenu(BaseMenu):
    '''Shows option for maintenance requests'''
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Request Menu"
        self.MaintenanceRequestAPI = MaintenanceRequestAPI()
        self.maintreportAPI = MaintReportAPI()
        self.propertyAPI = PropertyAPI()
        self.contractorAPI = ContractorAPI()
        self.propertyRepo = DB(Property)
        self.userAPI = UserAPI()
        self.employeesMenu = EmployeesMenu()
        self.propertiesMenu = PropertiesMenu()
        self.maintenanceRequestMenu = MaintenanceRequestMenu()

        self.menu_options = {               
            "1": {
                "title": "Create maintenance requests",  
                "access": "",
                "function": "createMRequest"
            },
            "2": {
                "title": "Create report",
                "access": "",
                "function": "create_report"
            },
            "3": {
                "title": "More request options",  
                "access": "",
                "class": MaintenanceRequestMenu
            },
            "4": {
                "title": "More report options",  
                "access": "",
                "class": MaintenanceReportMenu
            },
            "X": {
                "title": "Return to previous page",
                "Access": "",
                "special": "back"
            },
            "M": {
                "title": "Return to main menu",
                "special": "main"
            }
        }
    
    def create_report(self):
        verification_num = None
        while verification_num == None:
            verification_num = input("Enter the verification number of the maintenane request: ")
            try:
                verification_num = self.MaintenanceRequestAPI.findOneByVerificationNumber(verification_num)
            except RecordNotFoundError:
                find_request = input("Maintenance Request not found.\nDo you want to see a overview of the maintenance Requests? Y/N ")
                if find_request.lower() == 'y':
                    self.maintenanceRequestMenu.menu_options("1")
                verification_num = None
    
        request_info = ""

        was_contractor = input("Did you hire a Contractor for the project? Y/N: ")
        if was_contractor == "Y".islower():
            contractor_id = None
            while contractor_id == None:
                contractor_id = self.contractorAPI.findContractorByContractorId()
                try:
                    contractor_id = int(contractor_id)
                except ValueError:
                    print("Enter a valid ID")
                    contractor_id = None

            fee_input = float(input("Enter the contractors fee '%': "))
            contractors_fee = (fee_input / 100)

        maintenance_list = []
        while user_input != "":
            user_input = input("Enter what Maintenance was done: [Enter to continue]")
            maintenance_list.append(user_input)

        materialcost = int(input("Enter the materalcost for the project"))
        salary = int(input("Enter salary for the project"))
        finish_at = []

        self.maintreportAPI.createReport(request_info, verification_num, maintenance_list, contractor_id, materialcost, salary, contractors_fee, finish_at)

    def createMRequest(self):
        '''Gives option to create maintenace request '''
        status = ""
        property_id = None
        while property_id == None:
            property_id = input("Enter Property ID: ")
            try:
                found_property = self.propertyAPI.findPropertyByPropertyId(property_id)
                property_id = property_id
            except RecordNotFoundError:
                print("This property is not in the system ")
                create_property = input("Do you want to create a new property?: Y/N ")
                if create_property.lower() == "y":
                    self.propertiesMenu.createProperty()
                else:
                    property_id = None
        room_number = None
        while room_number == None:
            room_number = input("Do you want to sign it to a room number? [Y/N]: ")
            if room_number.lower() == 'y':
                found_prop = self.propertyAPI.findPropertyByPropertyId(property_id)
                rooms = found_prop.Rooms

                print(self.createTable(['size','roomId'], rooms))

                self.waitForKeyPress()

                room_signing = None
                while room_signing == None:
                    room_signing = input("\nWhat room number do you want to sing it to? ")
                    room = self.propertyAPI.findIfRoomInProperty(property_id, room_signing)
                    if room == False: 
                        print("Enter a valid room number: ")
                        room_signing = None
        user_input = None
        input_list = []
        while user_input != "":
            user_input = input("What maintenance is requested: (Enter empty string to continue) ")
            input_list.append(user_input)
        occurrence = None
        isRegular = True
        while occurrence == None:
            occurrence = input("How often per year\n[0] if this is not regular: ")
            try:
                occurrence = int(occurrence)
                if occurrence == 0:
                    occurrence = False
                    isRegular = False
            except ValueError:
                print("Enter an integer: ")
                occurrence = None
        priority = ""
        while priority == "":
            priority = (input("Priority [A][B][C]: ")).upper()
            valid_priority_list = ["A","B","C"]
            if priority not in valid_priority_list:
                priority = ""
                print("Enter a valid priority: ")
        start_date = input("Enter start date [dd,mm,yyyy]: ")
        employee_Id = ""
        while employee_Id == "":
            employee_Id = str(input("Enter employee id: "))
            try:
                employee_Id = int(employee_Id)
            except ValueError:
                employee_Id = ""
                print("Enter a valid ID: ")
            try:
                find_employee = self.userAPI.findEmployeeByEmployeeId(employee_Id)
            except RecordNotFoundError:
                print("This employee is not in the system ")
                create_employee = input("Do you want to create a new employee?: Y/N ")
                if create_employee.lower() == "y":
                    self.employeesMenu.createEmployee()
                else:
                    employee_Id = ""

        self.MaintenanceRequestAPI.createMaintenanceRequest(status=status, property_id = property_id , to_do=input_list, isRegular=isRegular, occurrence=occurrence, priority=priority, start_date = None, employee_Id=None)
        
        print("Maintenance Request succesfully created! ")
