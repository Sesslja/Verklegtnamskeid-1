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
        self.maintreportAPI = MaintReportAPI(logged_in_user=logged_in_user)
        self.maintrequestAPI = MaintenanceRequestAPI(logged_in_user=logged_in_user)
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
        maintenence_id = None
        while maintenence_id == None:
            maintenence_id = input("Enter maintenance ID: ")
            report_list = self.maintreportAPI.findMReportByVerificationId(maintenence_id)
            if report_list == []:
                find_request = input("Maintenance Id not found.\nDo you want to see a overview of the maintenance Requests? Y/N ")
                if find_request.lower() == 'y':
                    self.find_all_reports()
                maintenence_id = None
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
        ''' Manager can accept report, if he accepts the report will close otherwise it will reopen '''

        verificationNum = Prompt.ask("Enter the verification number of the maintenane report: ")
        try:
            found_maint = self.maintreportAPI.findMReportByVerificationId(verificationNum)
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
            print(self.createTable(show_keys,found_maint))
            self.waitForKeyPress()
            question = Prompt.ask(' Do you accept this report? Y/N: ')
            if question == 'Y'.lower():
                self.maintrequestAPI.changeMRequestStatus(verificationNum, 'Closed')
                print('This report is now closed!')
            elif 'N'.lower():
                self.maintrequestAPI.changeMRequestStatus(verificationNum, 'Opened')
                print('You reopened this report!')
        except RecordNotFoundError:
            print('Maintenance report not found')
        self.waitForKeyPress()


