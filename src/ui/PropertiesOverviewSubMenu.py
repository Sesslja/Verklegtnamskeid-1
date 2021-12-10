from os import name
from re import L
from typing import Text
from data.DBError import RecordNotFoundError
from ui.BaseMenu import RICH_AVAILABLE, BaseMenu
from logic.PropertyLogic import PropertyAPI
from logic.UserLogic import UserAPI
from ui.Colors import color

try:
    from rich.layout import Layout
    from rich import print
    from rich.prompt import Prompt
    from rich.panel import Panel
    from rich.text import Text
except ModuleNotFoundError:
    pass

class PropertiesOverviewSubMenu(BaseMenu):
    '''sub menu to property overview'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.propertyapi = PropertyAPI()
        self.userApi = UserAPI()
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
                "function": "searchById"
            },
            "4":  {
                "title": "Search by Employee",
                "access": "manager",
                "function": "search_by_employee"
            },
            "5":  {
                "title": "Find rooms by property ID",
                "access": "manager",
                "function": "findRoomsByPropertyId"
            },
            "6":  {
                "title": "Find Maintenance Requests assigned to property",
                "access": "manager",
                "function": "showPropertyMaintenanceRequests"
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

    def showPropertyMaintenanceRequests(self):
        '''Shows all request assigned to property'''
        property_id = input("Enter property ID: ")
        try:    
            found_property = self.propertyapi.findPropertyByPropertyId(property_id)
            requests = self.propertyapi.findRequestsByPropertyID(found_property.propertyId)
            
            show_keys = {
                'verification_number': {
                    'display_name': 'Verification Number'
                },
                'status': {
                    'display_name': 'Status'
                },
                'to_do': {
                    'display_name': 'Todo'
                }
            }
            print(self.createTable(show_keys, requests, table_title=f'Maintenance requests for property with ID:[bold] {property_id} [/bold]'))
        except RecordNotFoundError:
            print('Nothing foud :(')
        self.waitForKeyPress()
    


    def search_by_employee(self):
        ''' Finds all properties assigned to an employee '''
        try:
            employee_id = input("Find property by employee:\nEnter employee SSN: ")
            property_list = self.propertyapi.findPropertyByEmployeeSsn(employee_id)

            header_list = ['amenities', 'propertyId', 'isActive']
            self.createTable(header_list, property_list, line_between_records=True, justify_table='center')
        except RecordNotFoundError:
            print("No employees found with that SSN")
        self.waitForKeyPress()

    def searchById(self):
        '''Finds a property given a property ID'''
        try:
            property_id = input("Find property by property ID:\nEnter property ID: ")
            property_list = self.propertyapi.findPropertyByPropertyId(property_id)

            employee_list = self.propertyapi.findEmployeesByPropertyId(property_id)

            maintenance_requests_list = self.propertyapi.findRequestsByPropertyID(property_id)

            if RICH_AVAILABLE:
                main_layout = Layout()
                property_layout = Layout()
                maint_reqs_layout = Layout()

                main_layout.split_column(
                    Layout(name="header", size=1),
                    Layout(name="main")
                )
                main_layout["header"].update(
                    Text('')
                )
                main_layout["main"].split_row(
                    Layout(name="prop_info"),
                    Layout(name="maint_req_info"),
                )

                main_layout["prop_info"].update(
                    Panel(
                        property_layout,
                    title="Property Info")
                )

                main_layout["maint_req_info"].update(
                    Panel(
                        maint_reqs_layout,
                    title="Open maintenance requests")
                )

                property_layout.split_column(
                    Layout(name="info"),
                    Layout(name="related", ratio=2)
                )

                property_layout["related"].split_row(
                    Layout(name="employees", ratio=2),
                    Layout(name="rooms"),
                    Layout(name="amenities")
                )

                single_property_to_table_list = [
                    {'1': 'Property ID', '2': property_list.propertyId},
                    {'1': 'Address', '2': property_list.address_str},
                    {'1': 'Total size', '2': property_list.total_size},
                    {'1': 'Amount of rooms', '2': property_list.room_amount},
                ]

                property_layout["info"].update(
                    self.createTable(['1', '2'], single_property_to_table_list, line_between_records=True, return_table=True, hide_header=True, table_style='red', hide_entry_count=True),
                )

                header_employees = {
                    'name': {
                        'display_name': 'Name'
                    },
                    'email': {
                        'display_name': 'E-Mail'
                    },
                    'ssn': {
                        'display_name': 'SSN'
                    }
                }

                property_layout["related"]["employees"].update(
                    self.createTable(header_employees, employee_list, table_title='Assigned Employees', line_between_records=True, return_table=True)
                )

                header_rooms = {
                    'roomId': {
                        'display_name': 'Room ID'
                    },
                    'size': {
                        'display_name': 'Size',
                        'suffix': ' m²'
                    }
                }
#
                property_layout["related"]["rooms"].update(
                    self.createTable(header_rooms, property_list.Rooms, table_title='Rooms', line_between_records=True, return_table=True, entry_limit=10)
                )

                amenities_list = []
                for amen in property_list.amenities:
                    amenities_list.append({'amenity': amen})

                property_layout["related"]["amenities"].update(
                    self.createTable(['amenity'], amenities_list, hide_header=True, table_title='Amenities', line_between_records=True, return_table=True)
                )

                header_maint_reqs = {
                    'verification_number': {
                        'display_name': 'Verification Number'
                    },
                    'occurance': {
                        'display_name': 'Occurance'
                    },
                    'priority': {
                        'display_name': 'Priority'
                    }
                }

                maint_reqs_layout.update(
                    self.createTable(header_maint_reqs, maintenance_requests_list, return_table=True)
                )

                print(main_layout)
            else:
                print(color('Rich module not installed, unable to display', backgroundColor='red'))

            #print(self.createTable(header_list, property_list, line_between_records=True))
        except RecordNotFoundError:
            print("Property not found!")
        self.waitForKeyPress()


    def search_by_region(self):
        '''Finds all properties given a property Region'''
        print('Find property by region:\n')
        property_region = Prompt.ask("Enter region: ", choices=self.propertyapi.findAvailableCountries()).capitalize()
        try:
            property_list = self.propertyapi.findPropertyByCountry(property_region)

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
            }#['amenities', 'propertyId', 'isActive']
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

        self.waitForKeyPress(text_to_print='Press any key to return')

