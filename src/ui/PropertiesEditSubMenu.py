from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI


class PropertiesEditSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.propertyapi = PropertyAPI()
        self.propertyId = self.propertyIdInput()

        self.menu_title = f"Edit property nr. {self.propertyId}"


        self.menu_options = {
            "1": {
                "title": "Edit property",
                "access": "manager",
                "function": "createProperty"
            },
            "2": {
                "title": "Add new room",
                "access": "manager",
                "function": "addRoom"
            },
            "3":  {
                "title": "Edit rooms",
                "access": ""
            },
            "4": {
                "title": "Assign employees to property",
                "access": ""
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

    def propertyIdInput(self, retry: bool= False):
        self.clear()
        print('No property ID found please input a correct one') if retry else None
        propId = input('Please input the property ID: ')

        foundProp = self.propertyapi.findPropertyByPropertyId(propId)

        if len(foundProp) > 0:
            return propId
        else:
            return self.propertyIdInput(True)

    def addRoom(self):
        found_property = self.propertyapi.findPropertyByPropertyId(self.propertyId)

        
        roomSize = input('How large is the room?')

    def createRoomId(self):
        found_property = self.propertyapi.findPropertyByPropertyId(self.propertyId)

        try:
            for room in found_property['rooms']:
                pass
        except KeyError:
            pass
