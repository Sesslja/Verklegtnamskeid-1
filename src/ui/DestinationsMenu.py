from model.AddressType import Address
from ui.BaseMenu import BaseMenu
from logic.DestinationsLogic import DestinationsAPI

class DestinationsMenu(BaseMenu):

    def __init__(self):

        super().__init__()
        self.destinationsapi = DestinationsAPI()

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

        country = input('Country: ')
        city = input('City: ')
        zip_code = input('Zip code: ')
        address = Address(country=country, city=city, zip=zip_code)

        self.destinationsapi.createDestination(address)

        print(f"{city}, {country} added as a destination!")

        self.waitForKeyPress()

    def find_destination_by_country(self):
        destination_country = None
        while destination_country == None:
            
            destination_country = input("Enter the destination's country: ")

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

            destination_city = input("Enter the destination's country: ")

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

        if self.destinationsapi.deleteContractor(selected_dest_id) == True:
            print("Destination deleted")
        else: 
            print("Destination not found")
        self.waitForKeyPress()