from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI
from rich.prompt import Confirm, Prompt, FloatPrompt


class PropertiesEditSubMenu(BaseMenu):
    '''gives menu options to edit property'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.propertyapi = PropertyAPI()
        self.propertyId = self.propertyIdInput()
        if self.propertyId is 'q':
            self.failed = True

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
                "title": "Edit room",
                "access": "manager",
                "function": "editRoom"
            },
            "4":  {
                "title": "Delete room",
                "access": "manager",
                "function": "deleteRoom"
            },
            "5": {
                "title": "Assign employees to property",
                "access": "",
                "function": "assignEmployeeToProperty"
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
        propId = input('Please input ID of property ([Q] to Quit): ')
        if propId.lower() == "q":
            return "q"

        try:
            foundProp = self.propertyapi.findPropertyByPropertyId(propId)
        except RecordNotFoundError:
            return self.propertyIdInput(True)

        return foundProp.propertyId

    def addRoom(self):
        '''adds a room to property'''
        
        roomSize = input('How large is the room?: ')
        roomId = input('What is the property ID of the room? (ID of parent Property will be used if none): ')

        created_room = self.propertyapi.createRoom(size=roomSize, roomId=roomId, propertyId=self.propertyId)

        created_room = created_room.Rooms

        print('Successfully created new room')
        header = {
            'roomId': {
                'display_name': 'Room ID'
            },
            'size': {
                'display_name': 'Room Size',
                'suffix': ' m²'
            }
        }
        print(self.createTable(header, created_room, table_title='Rooms in property', color_newest=True))

        self.waitForKeyPress()

    def editRoom(self):
        ''' Edit room size and ID'''
        property_list = self.propertyapi.findPropertyByPropertyId(self.propertyId)
        header = {
            'roomId': {
                'display_name': 'Room ID'
            },
            'size': {
                'display_name': 'Size (m²)',
                'suffix': ' m²'
            }
        }
        roomList = property_list.Rooms[:]

        roomIdList = []
        for room in property_list.Rooms:
            roomIdList.append(room["roomId"])


        self.createTable(header, roomList, table_title='Rooms in property', line_between_records=True)

        print('Edit rooms')
        roomId = Prompt.ask("Enter room ID", choices=roomIdList, show_choices=False)
        roomIndex = roomIdList.index(roomId)

        print('Edit room info\nPress enter with an empty line of you do not wish to change.')
        confirm_change = None
        cancel_op = None
        while confirm_change != "y":
            property_list = self.propertyapi.findPropertyByPropertyId(self.propertyId)

            new_size = FloatPrompt.ask('Enter new size (m²)', default=property_list.Rooms[roomIndex]["size"])
            new_id = Prompt.ask('Enter new ID', default=property_list.Rooms[roomIndex]["roomId"])

            if new_id != roomId or new_size != property_list.Rooms[roomIndex]["size"]:
                print('Are you sure you want to change')
                if new_id != roomId:
                    print(f'The rooms ID from {roomId} to {new_id}.')
                if new_size != property_list.Rooms[roomIndex]["size"]:
                    print(f'The rooms size from {property_list.Rooms[roomIndex]["size"]} m² to {new_size} m².')
                confirm_change = input("[y/N]: ").lower()
            else:
                print('Nothing changed, operation cancelled.')
            if confirm_change != "y":
                cancel_op = input("Do you want to cancel? [y/N]").lower()
                if cancel_op == "y":
                    confirm_change = "y"
            if confirm_change == "y" and cancel_op != "y":
                property_list.Rooms[roomIndex]["size"] = new_size
                property_list.Rooms[roomIndex]["roomId"] = new_id

        updated_rooms = self.propertyapi.updateRooms(property_list._id, property_list.Rooms)
        self.createTable(header, updated_rooms.Rooms, table_title='Rooms in property', line_between_records=True)
        print(f"Successfully updated room nr. {new_id}\n")

        self.waitForKeyPress()


        
            
        


    def assignEmployeeToProperty(self):
        '''assignes employee to a specific property\n(needs employee ssn)'''
        empl_ssn = input('Enter employee SSN: ')

        try:
            updated = self.propertyapi.assignEmployeeToProperty(employeeSSN=empl_ssn, propertyId=self.propertyId)

            print(f'Successfully added employee with SSN: {empl_ssn}, to property with ID: {self.propertyId}')

        except RecordNotFoundError:
            print('Employee not found')
        
        self.waitForKeyPress()
