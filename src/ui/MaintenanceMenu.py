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


class MaintenanceMenu(BaseMenu):
    '''Shows option for maintenance requests'''
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Menu"
        self.MaintenanceRequestAPI = MaintenanceRequestAPI
        self.maintreportAPI = MaintReportAPI
        self.propertyAPI = PropertyAPI
        self.contractorAPI = ContractorAPI
        self.propertyRepo = DB(Property)

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
                verification_num = self.maintenanceRequestAPI.findMRequestByVerificationId()
            except ValueError:
                print("Enter a valid ID")
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
                find_property = self.propertyAPI().findPropertyByPropertyId(property_id)
            except ValueError:
                print("Enter a valid ID")
                property_id = None
        property = self.propertyAPI.findPropertyByPropertyId(self, property_id)
        room_number = None
        while room_number == None:
            room_number = input("Do you want to add a room number? [Y/N]: ")
            if room_number == 'Y'.lower():
                self.propertyAPI.findRoomsByPropertyId()
                room_input = input("What is the room number?: ")

        user_input = None
        input_list = []
        while user_input != "":
            user_input = input("What maintenance is requested: ")
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


        self.MaintenanceRequestAPI.createMaintenanceRequest(status=status, property_id=property_id, to_do=input_list, isRegular=isRegular, occurrence=occurrence, priority=priority, start_date = None, employee_Id=None)
        print("Maintenance Request succesfully created! ")
