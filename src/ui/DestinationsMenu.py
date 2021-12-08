from model.AddressType import Address
from ui.BaseMenu import BaseMenu
from logic.DestinationsLogic import DestinationsAPI
#from logic.ContractorLogic import ContractorAPI
#from ui.ContractorsOverviewSubMenu import ContractorsOverviewSubMenu 

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
        address = Address(country=country, city=city, zip_code=zip_code)#, zip_code=zip_code)

        self.destinationsapi.createDestination(address)

        print(f"{city}, {country} added as a destination!")

        self.waitForKeyPress()

    def find_destination_by_country(self): #1
        destination_country = None
        while destination_country == None:
            try:
                destination_country = input("Enter the destination's country: ")
            except ValueError:
                print("Please enter a valid country")
        try:
            destination_list = self.destinationsapi.findDestinationByCountry(destination_country)
            if len(destination_list) == 0:
                print("Destinations not found!")
                destination_country = None
            else:
                show_keys = ['country', 'city']
                print(self.createTable(show_keys, destination_list))
                self.waitForKeyPress()
        except ValueError:
            print("No destination found")
        self.waitForKeyPress()

    def find_destination_by_city(self): 
        destination_city = None
        while destination_city == None:
            try:
                destination_city = input("Enter the destination's city: ")
            except ValueError:
                print("Please enter a valid city")
        try:
            destination_list = self.destinationsapi.findDestinationByCity(destination_city)
            if len(destination_list) == 0:
                print("Destinations not found!")
                destination_city = None
            else:
                show_keys = ['country', 'city']
                print(self.createTable(show_keys, destination_list))
                self.waitForKeyPress()
        except ValueError:
            print("No destination found")
        self.waitForKeyPress()

    def all_destinations_overview(self):

        try:
            destination_list = self.destinationsapi.findDestination()
            if len(destination_list) == 0:
                print("No destinations to show")
            else:
                show_keys = ['country','city']
                print(self.createTable(show_keys, destination_list))
                self.waitForKeyPress()
        except ValueError:
            print("No destinations found")
        self.waitForKeyPress()