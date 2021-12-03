from ui.BaseMenu import BaseMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI

class MaintenanceMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Menu"
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
                "title": "Create maintenance requests",  
                "access": "",
                "function": "createMRequest"
            },       
            "5": {
                "title": "Outstanding maintenance requests",
                "access": "Manager",
                "function": "outstandingMRequest"
            },
            "6": {
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

    def createMRequest(self):
        adress = input("Enter Adress: ")
        user_input = None
        input_list = []
        while user_input != "":
            user_input = input("Enter stuff to do: ")
            input_list.append(user_input)
        occurrence = None
        while occurrence == None:
            occurrence = input("How often per year\n[0] if this is not regular")
            try:
                occurrence = int(occurrence)
                if occurrence == 0:
                    occurrence = False
            except ValueError:
                print("Enter an integer")
                occurrence = None
        priority = ""
        while priority == None:
            priority = (input("Priority [A][B][C]")).upper()
            valid_priority_list = ["A","B","C"]
            if priority not in valid_priority_list:
                priority = None
                print("Enter a valid priority")
        start_date = input("Enter start date [dd.mm.yyyy]: ")
        employee_id = ""
        while employee_id == None:
            employee_id = input("Enter employee id: ")
            try:
                employee_id = int(employee_id)
            except ValueError:
                employee_id = None
                print("Enter a valid ID")

        self.maintenanceRequestAPI.createMaintenanceRequest(adress, input_list, occurrence, priority, start_date, employee_id)
        print("Maintenance Request succesfully created! ")


    def outstandingMRequest(self):
        outstanding_request_list = self.maintenanceRequestAPI.outstandingMRequest()
        for request in outstanding_request_list:
            print(request)