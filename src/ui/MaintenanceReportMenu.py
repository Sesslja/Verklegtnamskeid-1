from ui.BaseMenu import BaseMenu
from logic.MaintReportLogic import MaintReportAPI

class MaintenanceReportMenu(BaseMenu):
    '''Gives maintenace report optins'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)

        self.menu_title = "Maintenance Report Menu"
        self.maintreportAPI = MaintReportAPI()

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
                "title": "Find report by employee",
                "access": "",
                "function": "find_by_employee"
            },
            "4": {
                "title": "Find report by property",
                "access": "",
                "function": "find_by_property"
            },
            "5": {
                "title": "Find report by date",
                "access": "",
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

    def find_all_reports(self):
        report_list = self.maintreportAPI.findReport()
        show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
        print(self.createTable(show_keys, report_list))
        self.waitForKeyPress()

