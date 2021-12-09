from data.DBError import RecordNotFoundError
from logic.UserLogic import UserAPI
from model.AddressType import Address
from ui.BaseMenu import BaseMenu
from logic.DestinationsLogic import DestinationsAPI
try:
    from rich.prompt import Confirm, Prompt
except ModuleNotFoundError:
    pass

class DestinationsMenu(BaseMenu):

    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.destinationsapi = DestinationsAPI()
        self.userApi = UserAPI()

        self.menu_title = "Menu\nDestinations Menu"

        self.menu_options = {
            "1": {
                "title": "See all destinations",
                "access": "Manager",
                "function": "all_destinations_overview"
            },                            
            "2": {
                "title": "Find destination by country",
                "access": "",
                "function": "find_destination_by_country"
            },                            
            "3": {
                "title": "Find destination by city",
                "access": "",
                "function": "find_destination_by_city"
            },                            
            "4": {
                "title": "Create destination",
                "access": "",
                "function": "create_destination"
            },                            
            "5": {
                "title": "Delete destination",
                "access": "",
                "function": "delete_destination"
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

    def create_destination(self):
        print('Create destination:')

        name = input('Name: ')
        country = input('Country: ')
        city = input('City: ')
        zip_code = input('Zip code: ')
        manager_num_input = None
        manager_id = None
        while manager_num_input == None:
            manager_num_input = input("Manager's employee number: ")
            if manager_num_input != "":
                try:
                    found_manager = self.userApi.findEmployeeByEmployeeId(manager_num_input)
                    if found_manager.isManager:
                        manager_id = found_manager._id
                    else:
                        print("That's not a manager, please enter the number of a manager.")
                        manager_num_input = None
                except RecordNotFoundError:
                    print("Couldn't find a manager with that number.")
                    manager_num_input = None
        
        employees_input = None
        employees_list = []
        while employees_input != "":
            employees_input = input("Enter employee number (Empty string continues): ")
            if employees_input != "":
                try:
                    found_employee = self.userApi.findEmployeeByEmployeeId(employees_input)
                    employees_list.append(found_employee._id)
                except RecordNotFoundError:
                    print("Couldn't find an employee with that number.")
                    employees_input = None

        address = Address(country=country, city=city, zip=zip_code)

        self.destinationsapi.createDestination(name=name, address=address, manager=manager_id, employees=employees_list)

        print(f"{city}, {country} added as a destination with {found_manager.name} as a manager!")

        self.waitForKeyPress()

    def find_destination_by_country(self):
        destination_country = None
        while destination_country == None:
            
            destination_country = Prompt.ask("Enter the destinations country", choices=self.destinationsapi.findCountriesOfDestinations())

        try:
            destination_list = self.destinationsapi.findDestinationByCountry(destination_country)
            if len(destination_list) == 0:
                print("Destinations not found!")
                destination_country = None
            else:
                addresslist = []
                for i, dest in enumerate(destination_list):
                    record_dict = {}
                    for key in dest.Address:
                        record_dict.update({key: dest.Address[key]})
                    addresslist.append(record_dict)

                show_keys = ['country', 'city']

                print(self.createTable(show_keys, addresslist))

        except ValueError:
            print("No destination found")
        self.waitForKeyPress()

    def find_destination_by_city(self): 
        destination_city = None
        while destination_city == None:

            destination_city = Prompt.ask("Enter the destinations city", choices=self.destinationsapi.findCitiesOfDestinations())

        try:
            destination_list = self.destinationsapi.findDestinationByCity(destination_city)
            if len(destination_list) == 0:
                print("Destinations not found!")
                destination_city = None
            else:
                addresslist = []
                for i, dest in enumerate(destination_list):
                    record_dict = {}
                    for key in dest.Address:
                        record_dict.update({key: dest.Address[key]})
                    addresslist.append(record_dict)
                show_keys = ['country', 'city']
                print(self.createTable(show_keys, addresslist))

        except ValueError:
            print("No destination found")
        self.waitForKeyPress()

    def all_destinations_overview(self):

        try:
            destination_list = self.destinationsapi.findDestinations()
            if len(destination_list) == 0:
                print("No destinations to show")
            else:
                for i, dest in enumerate(destination_list):
                    for key in dest.Address:
                        setattr(destination_list[i], key, dest.Address[key])

                print(destination_list)
                show_keys = {
                    'country': {
                        'display_name': 'Country'
                    },
                    'city': {
                        'display_name': 'City'
                    }
                }
                print(self.createTable(show_keys, destination_list))

        except ValueError:
            print("No destinations found")
        self.waitForKeyPress()
    
    def delete_destination(self):

        selected_dest_id = input('Enter destination id: ')

        if Confirm.ask('Are you sure you want to delete that destination?'):
            if self.destinationsapi.deleteDestination(selected_dest_id) == True:
                print("Destination deleted")
            else: 
                print("Destination not found")
            self.waitForKeyPress()