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
        property_id = input("Enter Property ID: ")
        country = input("Country: ")
        city = input("City: ")
        zip = input("Zip code: ")
        addr1 = input("Address 1: ")
        addr2 = input("Address 2: ")
        addr3 = input("Address 3: ")

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
            user_input = input("    Enter room size: ")
            if user_input is "":
                break
            room.size = user_input

            rooms_list.append(room)
        
        self.propertyapi.createProperty(address=address, propertyId=property_id, amenities=amenities_list, rooms=rooms_list)
        
        

        