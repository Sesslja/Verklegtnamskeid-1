from ui.BaseMenu import BaseMenu

class MaintenanceMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = {
            "A": {
                "title": "Opened maintenance request",
                "Access": "Manager",
                "Function": "openedMRequest"
            },
            "B": {
                "title": "Closed maintenance requests",
                "Acess": "",
                "Function": "closedMRequest"
            },        
            "C": {
                "title": "Upcoming maintenance",
                "Access": "",
                "Function": "upcomingMaintenance"
            },                
            "D": {
                "title": "Create maintenance requests",  
                "Access": "",
                "Function": "createMRequest"
            },       
            "E": {
                "title": "Outstanding maintenance requests",
                "Access": "Manager",
                "Function": "outstandingMRequest"
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