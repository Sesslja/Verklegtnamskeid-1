from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI

class PropertiesOverviewSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.propertyapi = PropertyAPI()
        self.menu_title = "Properties Menu\nProperties overview"

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

    def search_by_employee(self):
        try:
            employee_id = input("Find property by employee:\nEnter employee ID: ")
            property_list = self.propertyapi.findPropertyByEmployee(employee_id)
            if len(property_list) == 0:
                print("No properties found with that ID")
            else:
                header_list = ['address', 'amenities', 'propertyId', 'isActive']
                print(self.createTable(header_list, property_list, line_between_records=True))
        except ValueError:
            print("No properties found with that ID")
        self.waitForKeyPress()

    def search_by_id(self):
        try:
            property_id = input("Find property by property ID:\nEnter property ID: ")
            property_list = self.propertyapi.findPropertyByPropertyId(property_id)
            if len(property_list) == 0:
                print("Property not found!")
            else:
                header_list = ['address', 'amenities', 'propertyId', 'isActive']
                print(self.createTable(header_list, property_list, line_between_records=True))
        except ValueError:
            print("Property not found!")
        self.waitForKeyPress()

    def search_by_region(self):
        property_region = input("Find property by region:\nEnter region: ")
        try:
            property_list = self.propertyapi.findPropertyByCountry(property_region)
            if len(property_list) == 0:
                print("There do not seem to be any properties in that region")
            else:
                header_list = ['address', 'amenities', 'propertyId', 'isActive']
                print(self.createTable(header_list, property_list, line_between_records=True))
        except ValueError:
            print ("Region not found")
        self.waitForKeyPress()


    def print_all_properties(self):
        try:
            property_list = self.propertyapi.findProperty()
            if len(property_list) == 0:
                print("There are no properties to show")
            else:
                header_list = ['address', 'amenities', 'propertyId', 'isActive']
                print(self.createTable(header_list, property_list, line_between_records=True))
        except ValueError:
            print("There are no properties to show")

        self.waitForKeyPress()

