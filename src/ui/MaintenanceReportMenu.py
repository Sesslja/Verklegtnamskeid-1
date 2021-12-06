from ui.BaseMenu import BaseMenu
from logic.MaintReportLogic import MaintReportAPI

class MaintenanceReportMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Report Menu"
        self.maintreportAPI = MaintReportAPI

        self.menu_options = {
            
            "1": {
                "title": "find_report",
                "access": "",
                "function": "find_report"
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

    def find_report(self):
        pass


    def find_by_maintenance_id(self):
        pass

    def find_by_employee(self):
        pass

    def find_by_property(self):
        pass

    def find_by_date(self):
        pass