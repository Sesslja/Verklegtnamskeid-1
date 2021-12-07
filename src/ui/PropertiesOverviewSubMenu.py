from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI

class PropertiesOverviewSubMenu(BaseMenu):
    '''sub menu to property overview'''
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
        '''Finds all properties given a property ID'''
        try:
            property_id = input("Find property by property ID:\nEnter property ID: ")
            property_list = [self.propertyapi.findPropertyByPropertyId(property_id)]

            header_list = ['amenities', 'propertyId', 'isActive']
            print(self.createTable(header_list, property_list, line_between_records=True))
        except RecordNotFoundError:
            print("Property not found!")
        self.waitForKeyPress()

    def search_by_region(self):
        '''Finds all properties given a property Region'''
        property_region = input("Find property by region:\nEnter region: ").capitalize()
        try:
            property_list = self.propertyapi.findPropertyByCountry(property_region)

            header_list = ['amenities', 'propertyId', 'isActive']
            print(self.createTable(header_list, property_list, line_between_records=True))
        except RecordNotFoundError:
            print ("No properties found in region")
        self.waitForKeyPress()

    def findRoomsByPropertyId(self, propertyId: str=None):
        '''Finds all rooms of a property given property ID'''
        if propertyId == None:
            propertyId = input('Find rooms by property ID:\nEnter property ID: ')
        try:
            found_property = PropertyAPI().findPropertyByPropertyId(propertyId)

            # print(found_property)

            rooms = found_property.Rooms

            header = ['size', 'roomId']
            print(self.createTable(header, rooms))

        except RecordNotFoundError:
            print('Property not found')
        
        self.waitForKeyPress()


    def print_all_properties(self):
        '''prints a table of all properties og NAN'''
        try:
            property_list = self.propertyapi.findProperties()
            header_list = {
                'propertyId': {
                    'display_name': 'Property ID',
                    'header_style': 'bold'
                },
                'address_str': {
                    'display_name': 'Address',
                    'header_style': 'bold'
                },
                'amenities': {
                    'display_name': 'Amenities',
                    'header_style': 'bold'
                },
                'total_size': {
                    'display_name': 'Total size',
                    'suffix': ' m²',
                    'header_style': 'bold'
                },
                'room_amount': {
                    'display_name': 'Amount of rooms',
                    'header_style': 'bold'
                }
            }#
            #header = ['amenities', 'propertyId', 'isActive', 'total_size']

            print(self.createTable(header_list, property_list, line_between_records=True))
            #print(self.createTable(header_list, property_list, line_between_records=True))
        except RecordNotFoundError:
            print("There are no properties to show")

        print(self.waitForKeyPress())

        self.waitForKeyPress()

