from data.DBError import RecordNotFoundError
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
            "5":  {
                "title": "Find rooms by property ID",
                "access": "Manager",
                "function": "findRoomsByPropertyId"
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
        ''' Finds all properties assigned to an employee '''
        try:
            employee_id = input("Find property by employee:\nEnter employee SSN: ")
            property_list = self.propertyapi.findPropertyByEmployeeSsn(employee_id)

            header_list = ['amenities', 'propertyId', 'isActive']
            print(self.createTable(header_list, property_list, line_between_records=True))
        except RecordNotFoundError:
            print("No employees found with that SSN")
        self.waitForKeyPress()

    def search_by_id(self):
        try:
            property_id = input("Find property by property ID:\nEnter property ID: ")
            property_list = [self.propertyapi.findPropertyByPropertyId(property_id)]

            header_list = ['amenities', 'propertyId', 'isActive']
            print(self.createTable(header_list, property_list, line_between_records=True))
        except RecordNotFoundError:
            print("Property not found!")
        self.waitForKeyPress()

    def search_by_region(self):
        property_region = input("Find property by region:\nEnter region: ").capitalize()
        try:
            property_list = self.propertyapi.findPropertyByCountry(property_region)

            header_list = ['amenities', 'propertyId', 'isActive']
            print(self.createTable(header_list, property_list, line_between_records=True))
        except RecordNotFoundError:
            print ("No properties found in region")
        self.waitForKeyPress()

    def findRoomsByPropertyId(self):
        propertyId = input('Find rooms by property ID:\nEnter property ID: ')
        try:
            found_property = self.propertyapi.findPropertyByPropertyId(propertyId)

            # print(found_property)

            rooms = found_property.Rooms

            header = ['size', 'roomId']
            print(self.createTable(header, rooms))

        except RecordNotFoundError:
            print('Property not found')
        
        self.waitForKeyPress()


    def print_all_properties(self):
        try:
            property_list = self.propertyapi.findProperties()
            if len(property_list) == 0:
                print("There are no properties to show")
            else:
                header_list = {
                    'amenities': {
                        'display_name': 'Amenities'
                    },
                    'propertyId': {
                        'display_name': 'Property ID'
                    },
                    'total_size': {
                        'display_name': 'Total size',
                        'suffix': ' m²'
                    }
                }#['amenities', 'propertyId', 'isActive', 'total_size']
                print(self.createTable(header_list, property_list, line_between_records=True))
        except ValueError:
            print("There are no properties to show")

        print(self.waitForKeyPress())

        self.waitForKeyPress()

