from ui.BaseMenu import BaseMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI

class MaintenanceRequestMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Request Menu"
        self.maintenanceRequestAPI = MaintenanceRequestAPI

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

    def openedMRequest(self):
        try:
            open_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Opened")
            show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
            print(self.createTable(show_keys, open_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()

    def closedMRequest(self):
        try:
            closed_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Closed")
            show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
            print(self.createTable(show_keys, closed_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()

    def upcomingMaintenance(self):
        try:
            upcoming_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Upcoming")
            show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
            print(self.createTable(show_keys, upcoming_request_list))
        except ValueError:
            print("Nothing to Show :(")
        self.waitForKeyPress()


    def outstandingMRequest(self):
        outstanding_request_list = self.maintenanceRequestAPI.findMRequestByStatus("Outstanding")
        show_keys = ["verification_number",'occurance', 'priority', 'employeeId']
        print(self.createTable(show_keys, outstanding_request_list))
        self.waitForKeyPress()