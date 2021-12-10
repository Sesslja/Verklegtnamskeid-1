from ui.BaseMenu import BaseMenu
from logic.MaintReportLogic import MaintReportAPI
from ui.MaintenanceRequestMenu import MaintenanceRequestMenu

class MaintenanceReportMenu(BaseMenu):
    '''Gives maintenace report optins'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Report Menu"
        self.maintreportAPI = MaintReportAPI()
        self.maintanenceRequestMenu = MaintenanceRequestMenu(logged_in_user)

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
                "title": "Manager approves report ",
                "access": "",
                "function": "managerApprovesReport"
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

    def managerApprovesReport(self):
        pass


