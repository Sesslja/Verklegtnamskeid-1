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


class MaintenanceMenu(BaseMenu):
    '''Shows option for maintenance requests'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Request Menu"
        self.MaintenanceRequestAPI = MaintenanceRequestAPI()
        self.maintreportAPI = MaintReportAPI()
        self.propertyAPI = PropertyAPI()
        self.contractorAPI = ContractorAPI()
        self.propertyRepo = DB(Property)
        self.userAPI = UserAPI()
        self.employeesMenu = EmployeesMenu(logged_in_user=logged_in_user)
        self.propertiesMenu = PropertiesMenu(logged_in_user=logged_in_user)
        self.maintenanceRequestMenu = MaintenanceRequestMenu(logged_in_user=logged_in_user)
        self.datetime = DateTime()
        self.contractorsOverviewSubMenu = ContractorsOverviewSubMenu(logged_in_user=logged_in_user)

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
            verification_num = input("\nEnter the verification number of the maintenane request: ")
            try:
                verification_num = self.MaintenanceRequestAPI.findOneByVerificationNumber(verification_num)
            except RecordNotFoundError:
                find_request = input("Maintenance Request not found.\nDo you want to see a overview of the maintenance Requests? Y/N ")
                if find_request.lower() == 'y':
                    self.maintenanceRequestMenu.openedMRequest()
                verification_num = None
    
        request_info = ""

        was_contractor = input("Did you hire a Contractor for the project? Y/N: ")
        if was_contractor.lower() == "y":
            contractor_id = None
            while contractor_id == None:
                contractor_id = input("\nEnter contractors id: ")
                try:
                    contractor_id = int(contractor_id)
                    contractor = self.contractorAPI.findContractorByContractorId(str(contractor_id))
                except ValueError:
                    print("Enter a valid ID")
                    contractor_id = None
                except RecordNotFoundError:
                    find_contractor = input("This contactor is not in the system - Would you lika a overview of the contractors? Y/N ")
                    if find_contractor.lower() == 'y':
                        self.contractorsOverviewSubMenu.all_contractors_overview()
                    contractor_id = None
                    
            fee_input = float(input("Enter the contractors fee '%': "))
            contractors_fee = (fee_input / 100)

        user_input = None
        maintenance_list = []
        while user_input != "":
            user_input = input("Enter what Maintenance was done: (Enter empty string to continue) ")
            maintenance_list.append(user_input)

        materialcost = input("Enter the materalcost for the project ")
        if materialcost != "":
            materialcost = int(materialcost)
        else:
            materialcost = 0
        salary = input("Enter salary for the project ")
        if salary != "":
            salary = int(salary)
        else:
            salary = 0
        dt = self.datetime.generateDatetimeNow()

        try:
            print(f"Maintenance Report succesfully admitted to mananger at {dt}! ")
            self.maintreportAPI.createReport(request_info, verification_num, maintenance_list, contractor_id, materialcost, salary, contractors_fee, dt)
            self.waitForKeyPress()
        except:
            print(f"Something whent wrong")
        

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
                property_id = None

        room_number_input = None
        room_number = None
        while room_number_input == None:
            room_number_input = input("Do you want to sign it to a room number? [y/N]: ")
            if room_number_input.lower() == 'y':
                found_prop = self.propertyAPI.findPropertyByPropertyId(property_id)
                rooms = found_prop.Rooms

                print(self.createTable(['size','roomId'], rooms))

                #self.waitForKeyPress()

                room_signing = None
                while room_signing == None:
                    room_signing = input("\nWhat room number do you want to sign it to? ")
                    room = self.propertyAPI.findIfRoomInProperty(property_id, room_signing)
                    if room == False: 
                        print("Enter a valid room number: ")
                        room_signing = None
                room_number = room_signing

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
            try:
                start_date = [int(i) for i in start_date]
                date, dt = self.datetime.testDate(start_date)
                if date == False:
                    print("Date is out of range - Try again")
            except:
                print("Date is out of range - Try again")
        status = 'Open'
        #self.datetime.relative_date(test_date)
            #print self.datetime.get_relative_date(days_ahead)
            #print self.datetime.get_relative_date(weeks_ahead)
            #print self.datetime.get_relative_date(month_ahead)
            #print self.datetime.get_relative_date(months_ahead)

        employee_id_input = None
        employee_list = []
        employee_name_list = []
        print('Add employees:')
        while employee_id_input != "":
            employee_id_input = input("Enter employee number: (Empty string to skip)")
            if employee_id_input != "":
                try:
                    find_employee = self.userAPI.findEmployeeByEmployeeId(employee_id_input)
                    employee_id = find_employee._id
                    employee_list.append(employee_id)
                    employee_name_list.append(f"{find_employee.name} (Num. {find_employee.ssn})")
                except RecordNotFoundError:
                    print("This employee is not in the system ")
                    create_employee = input("Do you want to create a new employee?: [y/N] ")
                    if create_employee.lower() == "y":
                        self.employeesMenu.createEmployee()
                    else:
                        employee_id_input = None

        try:
            created_maint_report = self.MaintenanceRequestAPI.createMaintenanceRequest(status=status, property_id = property_id , to_do=input_list, isRegular=isRegular, 
                                                                occurrence=occurrence, priority=priority, start_date = dt, employees=employee_list,
                                                                roomNumId=room_number)


            single_property_to_table_list = [
                {'1': 'Property ID', '2': property_id},
                {'1': 'To Do', '2': created_maint_report.to_do},
                {'1': 'Occurance', '2': created_maint_report.occurance},
                {'1': 'Priority', '2': created_maint_report.priority},
                {'1': 'Start Date', '2': created_maint_report.start_date},
                {'1': 'Employees', '2': employee_name_list},
            ]
            self.createTable(['1','2'], single_property_to_table_list, hide_entry_count=True, hide_header=True, line_between_records=True, table_title=f"Maintenance Request succesfully created and set for {dt}! ")
        except:
            print(f"Something whent wrong")
        self.waitForKeyPress()