from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI

class PropertiesOverviewSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.propertyapi = PropertyAPI()
        self.menu_title = "Properties Menu"

        self.menu_options = {
            "1": {
                "title": "View all properties",
                "access": "",
                "function": "print_all_properties"
            },                   
            "2":  {
                "title": "Search by region",
                "access": "",
                "function": "search_by_region"
            },
            "3":  {
                "title": "Search by property ID",
                "access": "",
                "function": "search_by_id"
            },
            "4":  {
                "title": "Search by Employee",
                "access": "Manager",
                "function": "search_by_employee"
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

def search_by_employee():
    pass

def search_by_id():
    pass

def search_by_region():
    pass

def print_all_properties():
    pass