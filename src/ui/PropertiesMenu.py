from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI
from ui.PropertiesOverviewSubMenu import PropertiesOverviewSubMenu

class PropertiesMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.propertyapi = PropertyAPI()
        self.menu_title = "Properties Menu"

        self.menu_options = {
            "1": {
                "title": "Create new properties",
                "access": "manager",
                "function": "createProperty"
            },                   
            "2":  {
                "title": "Properties overview",
                "access": "",
                "class": PropertiesOverviewSubMenu
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
        adress = input("Property adress: ")
        property_id = input("Enter Property ID: ")
        amenities_list = []
        user_input = None
        while user_input != "":
            user_input = input("Enter amenities: ")
            amenities_list.append(user_input)
        
        self.propertyapi.createProperty(adress, property_id, amenities_list)
        
        

        