from ui.BaseMenu import BaseMenu

class MaintenanceMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Menu"

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
        print('show me open req')

    def closedMRequest(self):
        print('show me closed req')

    def upcomingMaintenance(self):
        print('show me upcoming maint')

    def createMRequest(self):
        print('create me maint req')

    def outstandingMRequest(self):
        print('show me outstanding req')