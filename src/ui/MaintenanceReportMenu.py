from rich import prompt
from ui.BaseMenu import BaseMenu
from logic.MaintReportLogic import MaintReportAPI
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from ui.MaintenanceRequestMenu import MaintenanceRequestMenu
from data.DBError import RecordNotFoundError
try:
    from rich.prompt import Prompt
except:
    pass

class MaintenanceReportMenu(BaseMenu):
    '''Gives maintenace report optins'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Report Menu"
        self.maintreportAPI = MaintReportAPI()
        self.maintrequestAPI = MaintenanceRequestAPI()
        self.maintanenceRequestMenu = MaintenanceRequestMenu(logged_in_user=logged_in_user)

        self.menu_options = {
            
            "1": {
                "title": "Find all reports",
                "access": "",
                "function": "find_all_reports"
            },                        
            "2": {
                "title": "Find report by maintenance ID",
                "access": "",
                "function": "find_by_maintenance_id"
            },
            "3": {
                "title": "Manager can accept report ",
                "access": "manager",
                "function": "managerAcceptsReport"
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

    def find_all_reports(self):
        '''Prints a table of all reports'''
        report_list = self.maintreportAPI.findReport()
        show_keys = {
            'verification_number': {
                'display_name': 'Verification Number'
            },
            'maintenance': {
                'display_name': 'Maintenance'
            },
            'materialcost': {
                'display_name': 'Material Cost'
            },
            'salary': {
                'display_name': 'Salary'
            },
            'contractorId': {
                'display_name': 'Contractor Id'
            },
            'contractorsfee': {
                'display_name': 'Contractors Fee'
            },
            'finish_at': {
                'display_name': 'Finished at'
            }
        } #['maintenance', 'contractorId', 'salary', 'contractorsfee', 'verification_number']
        print(self.createTable(show_keys, report_list))
        self.waitForKeyPress()
    
    def find_by_maintenance_id(self):
        '''Gives option to find maintenace report given the id of request'''
        verificationNum = None
        while verificationNum == None:
            verificationNum = input("Enter maintenance ID: ")
            report_list = self.maintreportAPI.findMReportByVerificationId(verificationNum)
            if report_list == []:
                find_request = input("Maintenance Id not found.\nDo you want to see a overview of the maintenance Requests? Y/N ")
                if find_request.lower() == 'y':
                    self.find_all_reports()
                verificationNum = None
            else:
                show_keys = show_keys = {
                'verification_number': {
                    'display_name': 'Verification Number'
                },
                'maintenance': {
                    'display_name': 'Maintenance'
                },
                'materialcost': {
                    'display_name': 'Material Cost'
                },
                'salary': {
                    'display_name': 'Salary'
                },
                'contractorId': {
                    'display_name': 'Contractor Id'
                },
                'contracotrsfee': {
                    'display_name': 'Contractors Fee'
                },
                'finish_at': {
                    'display_name': 'Finished at'
            }
                }#["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                print(self.createTable(show_keys, report_list))
                self.waitForKeyPress()

    def managerAcceptsReport(self):
        ''' Manager can accept report, if he accepts the report it will close otherwise it will reopen '''
        verificationNum = None
        while verificationNum == None:
            verificationNum = Prompt.ask("Enter the verification number of the maintenance report")
            request_list = self.maintreportAPI.findMReportByVerificationId(verificationNum)
            if request_list == []:
                find_request = input("No maintenance report was found with this verification number\nDo you want to see an overview of the maintenance Requests? Y/N ")
                if find_request.lower() == 'y':
                    self.maintanenceRequestMenu.outstandingMRequest()
                verificationNum = None
            else:
                show_keys = {
                    'verification_number': {
                        'display_name': 'Verification Number'
                    },
                    'maintenance': {
                        'display_name': 'Maintenance'
                    },
                    'contractorId': {
                        'display_name': 'Contractor'
                    },
                    'materialcost': {
                        'display_name': 'Material Cost'
                    },
                    'salary': {
                        'display_name': 'Salary'
                    },
                    'contractorId': {
                        'display_name': 'Contractor Id'
                    },
                    'contractorsfee': {
                        'display_name': 'Contractors Fee'
                    },
                    'finish_at': {
                        'display_name': 'Finished at'
                    }
                } #['maintenance', 'contractorId', 'salary', 'contractorsfee', 'verification_number']
                print(self.createTable(show_keys,request_list))
                self.waitForKeyPress()
                question = Prompt.ask('\nDo you accept this report? Y/N: ')
                if question == 'Y'.lower():
                    self.maintrequestAPI.changeMRequestStatus(verificationNum, 'Closed')
                    print('The report is now closed!')
                elif 'N'.lower():
                    self.maintrequestAPI.changeMRequestStatus(verificationNum, 'Opened')
                    print('You reopened this report!')
                self.waitForKeyPress()



