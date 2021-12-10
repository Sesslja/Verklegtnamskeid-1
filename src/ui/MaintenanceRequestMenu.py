from ui.BaseMenu import BaseMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from ui.EmployeeOverviewSubMenu import EmployeeOverviewSubMenu
from logic.UserLogic import UserAPI
from logic.PropertyLogic import PropertyAPI
from ui.PropertiesOverviewSubMenu import PropertiesOverviewSubMenu

class MaintenanceRequestMenu(BaseMenu):
    '''Gives Maintenance request options'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Request Menu"
        self.maintenanceRequestAPI = MaintenanceRequestAPI()
        self.employeeOverview = EmployeeOverviewSubMenu(logged_in_user=logged_in_user)
        self.userAPI = UserAPI(logged_in_user=logged_in_user)
        self.propertyAPI = PropertyAPI(logged_in_user=logged_in_user)
        self.propertyOverview = PropertiesOverviewSubMenu(logged_in_user=logged_in_user)

        self.menu_options = {
            "1": {
                "title": "Upcoming maintenance request",
                "access": "manager",
                "function": "openedMRequest"
            },
            "2": {
                "title": "Closed maintenance requests",
                "access": "",
                "function": "closedMRequest"
            },                         
            "3": {
                "title": "Outstanding maintenance requests",
                "access": "manager",
                "function": "outstandingMRequest"
            },
            "4": {
                "title": "All requests!",
                "access": "manager",
                "function": "allMaintRequest"
            },
            "5": {
                "title": "Find maintenance request by id",
                "access": "manager",
                "function": "find_by_maintenance_id"
            },
            "6": {
                "title": "Find maintenance request by employee",
                "access": "manager",
                "function": "find_by_employee"
            },
            "7": {
                "title": "Find maintenance request by property",
                "access": "manager",
                "function": "find_by_property"
            },
            "8": {
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
            # TODO: request employee names so we can show that
            show_keys = {
                'verification_number': {
                    'display_name': 'Verification Number'
                },
                'property_id': {
                    'display_name': 'Property Id'
                },
                'to_do': {
                    'display_name': 'To do'
                },
                'priority': {
                    'display_name': 'Priority'
                },
                'status': {
                    'display_name': 'Status'
                },
                'start_date': {
                    'display_name': 'Start Date'
                }
            }#["verification_number",'occurance', 'priority', 'employees'] old table keys
            print(self.createTable(show_keys, request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()


    def openedMRequest(self):
        '''prints out a table of all opened requests'''
        try:
            open_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Open")
            # TODO: request employee names so we can show that
            show_keys = {
                'verification_number': {
                    'display_name': 'Verification Number'
                },
                'property_id': {
                    'display_name': 'Property Id'
                },
                'to_do': {
                    'display_name': 'To do'
                },
                'priority': {
                    'display_name': 'Priority'
                },
                'start_date': {
                    'display_name': 'Start date'
                }
            }#["verification_number",'occurance', 'priority', 'employee_id', 'start_date']
            print(self.createTable(show_keys, open_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()

    def closedMRequest(self):
        '''prints out a table of all closed requests'''
        try:
            closed_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Closed")
            show_keys = show_keys = {
                'verification_number': {
                    'display_name': 'Verification Number'
                },
                'occurance': {
                    'display_name': 'Occurance'
                },
                'priority': {
                    'display_name': 'Priority'
                },
                'start_date': {
                    'display_name': 'Start date'
                }
            }#["verification_number",'occurance', 'priority', 'employeeId']
            print(self.createTable(show_keys, closed_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()


    def outstandingMRequest(self):
        '''prints out a table of all outstanding requests'''
        outstanding_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Outstanding")
        show_keys = show_keys = {
                'verification_number': {
                    'display_name': 'Verification Number'
                },
                'occurance': {
                    'display_name': 'Occurance'
                },
                'priority': {
                    'display_name': 'Priority'
                },
                'start_date': {
                    'display_name': 'Start date'
                }
            }#["verification_number",'occurance', 'priority', 'employeeId']
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
                show_keys = show_keys = {
                'verification_number': {
                    'display_name': 'Verification Number'
                },
                'occurance': {
                    'display_name': 'Occurance'
                },
                'priority': {
                    'display_name': 'Priority'
                },
                'start_date': {
                    'display_name': 'Start date'
                }
            }#["verification_number", "property_id",'maintenance', 'contractor_id', 'salary', 'contractors_fee']
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
                        show_keys = show_keys = {
                            'verification_number': {
                                'display_name': 'Verification Number'
                            },
                            'occurance': {
                                'display_name': 'Occurance'
                            },
                            'priority': {
                                'display_name': 'Priority'
                            },
                            'start_date': {
                                'display_name': 'Start date'
                            }
                        }#["verification_number", "property_id",'maintenance', 'contractor_id', 'salary', 'contractors_fee']
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
        propertyId = None
        while propertyId == None:
            propertyId = input("Enter property ID: ")
            try:
                findProperty = self.propertyAPI.findPropertyByPropertyId(propertyId)
                if findProperty != []:
                    requestList = self.maintenanceRequestAPI.findRequestsByProperty(propertyId)
                    if requestList != []:
                        show_keys = show_keys = {
                            'verification_number': {
                                'display_name': 'Verification Number'
                            },
                            'occurance': {
                                'display_name': 'Occurance'
                            },
                            'priority': {
                                'display_name': 'Priority'
                            },
                            'start_date': {
                                'display_name': 'Start date'
                            }
                        }#["property_id",'maintenance', 'contractor_id', 'salary', 'contractors_fee']
                        print(self.createTable(show_keys, requestList))
                        self.waitForKeyPress()
                    else:
                        print("There are no maintenance requests signed to this property")   
            except:
                print("This property is not in the system ")
                findProperty = input("Do you want to see an overview of all the properties?: Y/N ")
                if findProperty.lower() == "y":
                    self.propertyOverview.print_all_properties()
                propertyId = None

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
                    show_keys = {
                        'verification_number': {
                            'display_name': 'Verification Number'
                        },
                        'occurance': {
                            'display_name': 'Occurance'
                        },
                        'priority': {
                            'display_name': 'Priority'
                        },
                        'start_date': {
                            'display_name': 'Start date'
                        }
                    }#["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
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