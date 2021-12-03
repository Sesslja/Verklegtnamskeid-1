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
        open_request_list = self.maintenanceRequestAPI.getOpenedMRequest()
        for request in open_request_list:
            print(request)

    def closedMRequest(self):
        closed_request_list = self.maintenanceRequestAPI.getClosedMRequest()
        for request in closed_request_list:
            print(request)

    def upcomingMaintenance(self):
        upcoming_request_list = self.maintenanceRequestAPI.upcomingMRequest()
        for request in upcoming_request_list:
            print(request)


    def outstandingMRequest(self):
        outstanding_request_list = self.maintenanceRequestAPI.outstandingMRequest()
        for request in outstanding_request_list:
            print(request)