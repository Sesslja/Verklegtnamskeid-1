from ui.BaseMenu import BaseMenu

class MaintenanceMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = {
            "A": {
                "title": "Opened maintenance request",
                "access": "Manager",
                "function": "openedMRequest"
            },
            "B": {
                "title": "Closed maintenance requests",
                "access": "",
                "function": "closedMRequest"
            },        
            "C": {
                "title": "Upcoming maintenance",
                "access": "",
                "function": "upcomingMaintenance"
            },                
            "D": {
                "title": "Create maintenance requests",  
                "access": "",
                "function": "createMRequest"
            },       
            "E": {
                "title": "Outstanding maintenance requests",
                "access": "Manager",
                "function": "outstandingMRequest"
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