from rich.prompt import Prompt, FloatPrompt
from model.AddressType import Address
from model.RoomType import RoomType
from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI
from ui.PropertiesOverviewSubMenu import PropertiesOverviewSubMenu
from ui.PropertiesEditSubMenu import PropertiesEditSubMenu

class PropertiesMenu(BaseMenu):
    '''Main menu for property options'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.propertyapi = PropertyAPI()
        self.menu_title = "Properties Menu"

        self.menu_options = {
            "1": {
                "title": "Create new property",
                "access": "manager",
                "function": "createProperty"
            },
            "2": {
                "title": "Edit property",
                "access": "manager",
                "class": PropertiesEditSubMenu
            },
            "3":  {
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
                "access": "",
                "special": "main"
            }
        }

    def createProperty(self):
        '''creates a property object'''
        available_countries = self.propertyapi.findAvailableCountries()

        property_id = Prompt.ask("Enter Property ID: ")
        country = Prompt.ask("Country", choices=available_countries)
        city = Prompt.ask("City").capitalize()
        zip = Prompt.ask("Zip code")
        addr1 = Prompt.ask("Address 1")
        addr2 = input("Address 2: ")
        addr2 = addr2 if addr2 is not "" else None
        addr3 = input("Address 3: ")
        addr3 = addr3 if addr3 is not "" else None

        address = Address(country=country, city=city, zip=zip, address1=addr1, address2=addr2, address3=addr3)

        amenities_list = []
        user_input = None
        print("Enter amenities (Enter empty string to continue): ")
        while user_input != "":
            user_input = input("    Enter amenity: ")
            if user_input is not "":
                amenities_list.append(user_input)

        rooms_list = []
        user_input = None
        print("Enter rooms (Enter empty string to continue): ")
        while user_input != "":
            room = RoomType()
            user_input = input("    Enter room ID: ")
            if user_input is "":
                break
            room.roomId = user_input
            room.size = FloatPrompt.ask('  Enter room size')

            rooms_list.append(room)
            print(f'Added room with id: {room.roomId}, and size: {room.size}')
        
        
        self.propertyapi.createProperty(address=address, propertyId=property_id, amenities=amenities_list, rooms=rooms_list)
        print(':checkmark: Successfully created a property!')

        self.waitForKeyPress()

        
        

        