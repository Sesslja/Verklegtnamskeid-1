from ui.BaseMenu import BaseMenu
from ui.MaintenanceRequestMenu import MaintenanceRequestMenu
from ui.MaintenanceReportMenu import MaintenanceReportMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from logic.MaintReportLogic import MaintReportAPI

class MaintenanceMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Request Menu"
        self.maintenanceRequestAPI = MaintenanceRequestAPI
        self.maintreportAPI = MaintReportAPI

        self.menu_options = {               
            "1": {
                "title": "Create maintenance requests",  
                "access": "",
                "function": "createMRequest"
            },
            "2": {
                "title": "Create report",
                "access": "",
                "function": "create_report"
            },
            "3": {
                "title": "More request options",  
                "access": "",
                "class": MaintenanceRequestMenu
            },
            "4": {
                "title": "More report options",  
                "access": "",
                "class": MaintenanceReportMenu
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
    
    def create_report(self):
        pass

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
