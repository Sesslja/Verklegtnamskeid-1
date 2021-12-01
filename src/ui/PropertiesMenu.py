from ui.BaseMenu import BaseMenu

class PropertiesMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = {
            "A": {
                "title": "Record property",
                "access": "manager",
                "function": "createProperty"
            },                   
            "B":  {
                "title": "Properties overview",
                "access": "",
                "function": "propertiesOverview"
            },                
            "X": {
                "title": "Return to previous page",
                "access": "",
                "special": "back"
            },
            "M": {
                "title": "Return to main menu",
                "special": "main"
            }
        }

    def createProperty(self):
        print('no love no create')
    
    def propertiesOverview(self):
        print('no love no overview')