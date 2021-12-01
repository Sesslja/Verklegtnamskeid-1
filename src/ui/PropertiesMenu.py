from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI

class PropertiesMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Properties Menu"

        self.menu_options = {
            "A": {
                "title": "Create new properties",
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
        pass
        
    
    def propertiesOverview(self):
        print('no love no overview')