from ui.BaseMenu import BaseMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI

class MaintenanceRequestMenu(BaseMenu):
    '''Gives Maintenance request options'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Request Menu"
        self.maintenanceRequestAPI = MaintenanceRequestAPI()

        self.menu_options = {
            "1": {
                "title": "Opened maintenance request",
                "access": "Manager",
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
                "access": "Manager",
                "function": "outstandingMRequest"
            },
            "5": {
                "title": "All requests!",
                "access": "Manager",
                "function": "All_M_Request"
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
    
    def All_M_Request(self):
        '''prints out a table of all maintenance Requests'''
        try:
            request_list = self.maintenanceRequestAPI.MaintenanceRequestOverview()
            show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
            print(self.createTable(show_keys, request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()


    def openedMRequest(self):
        '''prints out a table of all opened requests'''
        try:
            open_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Open")
            show_keys = ["verification_number",'occurance', 'priority', 'employeeId', 'start_date']
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
            upcoming_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Upcoming")
            show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
            print(self.createTable(show_keys, upcoming_request_list))
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
        '''Gives option to find maintenace report given the id of request'''
        maintenence_id = None
        while maintenence_id == None:
            maintenence_id = input("Enter maintenance ID: ")
            try:
                int(maintenence_id)
                request_list = self.maintrequestAPI.findRequestByMaintenanceId(maintenence_id)
                if len(request_list) == 0:
                    print ("No items to show")
                    request_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                    print(self.createTable(show_keys, request_list))
                    self.waitForKeyPress()
            except ValueError:
                print("Please enter a valid ID")
                maintenence_id = None


    def find_by_employee(self):
        '''Gives option to find maintenace request given the id of employee'''
        employee_id = None
        while employee_id == None:
            employee_id = input("Enter employee ID: ")
            try:
                int(employee_id)
                request_list = self.maintrequestAPI.findRequestByEmployee(employee_id)
                if len(request_list) == 0:
                    print ("No items to show")
                    request_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                    print(self.createTable(show_keys, request_list))
                    self.waitForKeyPress()
            except ValueError:
                print("Please enter a valid ID")
                employee_id = None

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
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
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