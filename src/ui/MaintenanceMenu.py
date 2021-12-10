from datetime import datetime, date
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
from logic.DatetimeLogic import DateTime
from ui.ContractorsOverviewSubMenu import ContractorsOverviewSubMenu
from ui.EmployeeOverviewSubMenu import EmployeeOverviewSubMenu
try:
    from rich.text import Text
except ModuleNotFoundError:
    pass


class MaintenanceMenu(BaseMenu):
    '''Shows option for maintenance requests'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Request Menu"
        # Calls to APIs
        self.MaintenanceRequestAPI = MaintenanceRequestAPI()
        self.maintreportAPI = MaintReportAPI()
        self.propertyAPI = PropertyAPI()
        self.contractorAPI = ContractorAPI()
        self.userAPI = UserAPI()

        # Calls to other menus so we don't write the same thing often
        self.employeesMenu = EmployeesMenu(logged_in_user=logged_in_user)
        self.propertiesMenu = PropertiesMenu(logged_in_user=logged_in_user)
        self.maintenanceRequestMenu = MaintenanceRequestMenu(logged_in_user=logged_in_user)
        self.contractorsOverviewSubMenu = ContractorsOverviewSubMenu(logged_in_user=logged_in_user)
        self.employeeOverviewSubMenu = EmployeeOverviewSubMenu(logged_in_user=logged_in_user)

        self.datetime = DateTime()

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
        verificationNum = None
        while verificationNum == None:
            verificationNum = input("\nEnter the verification number of the maintenane request: ")
            try:
                verificationNum = self.MaintenanceRequestAPI.findOneByVerificationNumber(verificationNum)
            except RecordNotFoundError:
                find_request = input("Maintenance Request not found.\nDo you want to see a overview of the maintenance Requests? Y/N ")
                if find_request.lower() == 'y':
                    self.maintenanceRequestMenu.openedMRequest()
                verificationNum = None
    
        request_info = ""

        contractorID = None
        contractorsFee = None
        was_contractor = input("Did you hire a Contractor for the project? Y/N: ")
        if was_contractor.lower() == "y":
            while contractorID == None:
                contractorID = input("\nEnter contractors id: ")
                try:
                    int(contractorID)
                    contractor = self.contractorAPI.findContractorByContractorId(contractorID)
                except ValueError:
                    print("Enter a valid ID")
                    contractorID = None
                except RecordNotFoundError:
                    find_contractor = input("This contactor is not in the system - Would you lika a overview of the contractors? Y/N ")
                    if find_contractor.lower() == 'y':
                        self.contractorsOverviewSubMenu.all_contractors_overview()
                    contractorID = None
                    
            fee_input = float(input("Enter the contractors fee '%': "))
            contractorsFee = (fee_input / 100)

        user_input = None
        maintenanceList = []
        while user_input != "":
            user_input = input("Enter what Maintenance was done: (Enter empty string to continue) ")
            maintenanceList.append(user_input)

        materialCost = input("Enter the materalcost for the project ")
        if materialCost != "":
            materialCost = int(materialCost)
        else:
            materialCost = 0
        salary = input("Enter salary for the project: ")
        if salary != "":
            try:
                salary = int(salary)
            except ValueError:
                salary = 0
        else:
            salary = 0
        dt = self.datetime.generateDatetimeNow()

        report = self.maintreportAPI.createReport(
            request_info = request_info, 
            verification_number = verificationNum, 
            maintenance = maintenanceList, 
            contractorId = contractorID, 
            materialCost = materialCost, 
            salary = salary, 
            contractorsfee = contractorsFee, 
            dt = dt,
            creator_user=self.loggedInUser)

        if report != None:
            print(Text.from_markup(f":white_check_mark: Maintenance Report succesfully admitted to mananger at {dt}! "))
            self.waitForKeyPress()
        else:
           print(f"Something whent wrong - Try again")
           self.waitForKeyPress()
        

    def createMRequest(self):
        '''Gives option to create maintenace request '''
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
                #elif create_property.lower() == "n": #test
                #    return None #test
                property_id = None


        roomNumId = None
        while roomNumId == None:
            roomNumId = input("Do you want to sign it to a room number? [Y/N]: ")
            if roomNumId.lower() == 'y':
                found_prop = self.propertyAPI.findPropertyByPropertyId(property_id)
                rooms = found_prop.Rooms

                print(self.createTable(['size','roomId'], rooms))

                self.waitForKeyPress()

                room_signing = None
                while room_signing == None:
                    roomNumId = input("\nWhat room number do you want to sign it to? ")
                    room_signing = self.propertyAPI.findIfRoomInProperty(property_id, roomNumId)
                    if room_signing == False:
                        print("Enter a valid room number")
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

        date = False
        while date is False:
            start_date = input("Enter start date [yyyy,mm,dd]: ").split(',')
            if start_date == ['']:
                start_date = None
                date,dt = self.datetime.testDate(start_date)
            else:
                try:
                    start_date = [int(i) for i in start_date]
                    date, dt = self.datetime.testDate(start_date)
                    if date == False:
                        print("Date is out of range - Try again")
                except:
                    print("Date is out of range - Try again")
                    date = False
        status = 'Open'
        #self.datetime.relative_date(test_date)
            #print self.datetime.get_relative_date(days_ahead)
            #print self.datetime.get_relative_date(weeks_ahead)
            #print self.datetime.get_relative_date(month_ahead)
            #print self.datetime.get_relative_date(months_ahead)

        employee_Id = ""
        while employee_Id == "":
            employee_Id = str(input("Enter employee id: "))
            try:
                int(employee_Id)
            except ValueError:
                employee_Id = ""
                print("Enter a valid ID: ")
            try:
                find_employee = self.userAPI.findEmployeeByEmployeeId(employee_Id)
            except RecordNotFoundError:
                print("This employee is not in the system ")
                employeeOptions = input(
                    "1: Create a new employee?\n"
                    "2: Overview of all the employees?\n"
                    "3: Try again?\n")
                if employeeOptions == "1":
                    self.employeesMenu.createEmployee()
                elif employeeOptions == "2":
                    self.employeeOverviewSubMenu.allEmployeesOverview()
                    employee_Id = ""
                else:
                    employee_Id = ""

        try:
            self.MaintenanceRequestAPI.createMaintenanceRequest(status=status, property_id = property_id , to_do=input_list, isRegular=isRegular, occurrence=occurrence, priority=priority, start_date = dt, employees= find_employee._id, roomNumId=roomNumId)
            print(Text.from_markup(f"\n:white_check_mark: Maintenance Request succesfully created and set for {dt}! "))
            self.waitForKeyPress()
        except:
            print(f"Something went wrong")
