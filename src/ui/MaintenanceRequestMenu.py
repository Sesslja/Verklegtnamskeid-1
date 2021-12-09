from ui.BaseMenu import BaseMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from ui.EmployeeOverviewSubMenu import EmployeeOverviewSubMenu
from logic.UserLogic import UserAPI

class MaintenanceRequestMenu(BaseMenu):
    '''Gives Maintenance request options'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Request Menu"
        self.maintenanceRequestAPI = MaintenanceRequestAPI()
        self.employeeOverview = EmployeeOverviewSubMenu(logged_in_user=logged_in_user)
        self.userAPI = UserAPI()

        self.menu_options = {
            "1": {
                "title": "Opened maintenance request",
                "access": "manager",
                "function": "openedMRequest"
            },
            "2": {
                "title": "Closed maintenance requests",
                "access": "",
                "function": "closedMRequest"
            },        
            "3": {
                "title": "Upcoming maintenance",
                "access": "",
                "function": "upcomingMaintenance"
            },                  
            "4": {
                "title": "Outstanding maintenance requests",
                "access": "manager",
                "function": "outstandingMRequest"
            },
            "5": {
                "title": "All requests!",
                "access": "manager",
                "function": "allMaintRequest"
            },
            "6": {
                "title": "Find maintenance request by id",
                "access": "manager",
                "function": "find_by_maintenance_id"
            },
            "7": {
                "title": "Find maintenance request by employee",
                "access": "manager",
                "function": "find_by_employee"
            },
            "8": {
                "title": "Find maintenance request by property",
                "access": "manager",
                "function": "find_by_property"
            },
            "9": {
                "title": "Find maintenance request by date",
                "access": "manager",
                "function": "find_by_date"  
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
    
    def allMaintRequest(self):
        '''prints out a table of all maintenance Requests'''
        try:
            request_list = self.maintenanceRequestAPI.MaintenanceRequestOverview()
            show_keys = ["verification_number",'occurance', 'priority', 'employees']
            print(self.createTable(show_keys, request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()


    def openedMRequest(self):
        '''prints out a table of all opened requests'''
        try:
            open_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Open")
            show_keys = ["verification_number",'occurance', 'priority', 'employee_id', 'start_date']
            print(self.createTable(show_keys, open_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()

    def closedMRequest(self):
        '''prints out a table of all closed requests'''
        try:
            closed_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Closed")
            show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
            print(self.createTable(show_keys, closed_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()

    def upcomingMaintenance(self):
        '''prints out a table of all upcoming requests'''
        try:
            open_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Open")
            show_keys = ["verification_number",'start_date','employeeId','priority','occurance']
            print(self.createTable(show_keys, open_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()


    def outstandingMRequest(self):
        '''prints out a table of all outstanding requests'''
        outstanding_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Outstanding")
        show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
        print(self.createTable(show_keys, outstanding_request_list))
        self.waitForKeyPress()

    def find_by_maintenance_id(self):
        '''Gives option to find maintenace request given the id of request'''
        maintenence_id = None
        while maintenence_id == None:
            maintenence_id = input("Enter maintenance ID: ")
            request_list = self.maintenanceRequestAPI.findMRequestByVerificationId(maintenence_id)
            if request_list == []:
                find_request = input("Maintenance Id not found.\nDo you want to see a overview of the maintenance Requests? Y/N ")
                if find_request.lower() == 'y':
                    self.allMaintRequest()
                maintenence_id = None
            else:
                show_keys = ["verification_number", "property_id",'maintenance', 'contractor_id', 'salary', 'contractors_fee']
                print(self.createTable(show_keys, request_list))
                self.waitForKeyPress()

        
    def find_by_employee(self):
        '''Gives option to find maintenace request given the id of employee'''
        employeeId = None
        while employeeId == None:
            employeeId = str(input("Enter employee id: "))
            try:
                findEmployee = self.userAPI.findEmployeeByEmployeeId(employeeId)
                if findEmployee != []:
                    requestList = self.maintenanceRequestAPI.findRequestByEmployee(employeeId)
                    if requestList != []:
                        show_keys = ["verification_number", "property_id",'maintenance', 'contractor_id', 'salary', 'contractors_fee']
                        print(self.createTable(show_keys, requestList))
                        self.waitForKeyPress()
                    else:
                        print("There are no maintenance requests signed to this Employee")
            except:
                print("This employee is not in the system ")
                findEmployee = input("Do you want to an overview of all the employees?: Y/N ")
                if findEmployee.lower() == "y":
                    self.employeeOverview.allEmployeesOverview()
                employeeId = None   


    def find_by_property(self):
        '''Gives option to find maintenace request given the id of property'''
        property_id = None
        while property_id == None:
            property_id = input("Enter property ID: ")
            try:
                int(property_id)
                request_list = self.maintrequestAPI.findRequestByProperty(property_id)
                if len(request_list) == 0:
                    print ("No items to show")
                    request_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["property_id",'maintenance', 'contractor_id', 'salary', 'contractors_fee']
                    print(self.createTable(show_keys, request_list))
                    self.waitForKeyPress()
            except ValueError:
                print("Please enter a valid ID")
                property_id = None

    def find_by_date(self):
        '''Gives option to find maintenace request given the date of report'''
        start_date = None
        end_date = None
        while start_date == None or end_date == None:
            start_date = input("Enter start date: ")
            end_date = input("Enter start date: ")
            if start_date == "" or  end_date == "":
                start_date == None
                end_date == None
            else:
                request_list = self.maintrequestAPI.findRequestByDate(start_date, end_date)
                if len(request_list) == 0:
                    print ("No items to show")
                    request_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                    print(self.createTable(show_keys, request_list))
                    self.waitForKeyPress()
    

#test hér fyrir neðan

#    def approveReadyMRequest(self):
        
#        is_ready = None
#
#        while is_ready == None :

#            is_ready = input('Would you like to mark this request as closed or opened? (C/O): ')
#
#            if is_ready.lower() == 'c' :
#                self.closedMRequest()
#            elif is_ready.lower() == 'o' :
#                self.openedMRequest()
#            else :
#                print('Invalid input')