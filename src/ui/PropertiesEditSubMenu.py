from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.PropertyLogic import PropertyAPI


class PropertiesEditSubMenu(BaseMenu):
    '''gives menu optins to edit property'''
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
        propId = input('Please input the property ID: ')


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
            'size': {
                'display_name': 'Room Size'
            },
            'roomId': {
                'display_name': 'Room ID'
            }
        }
        print(self.createTable(header, created_room))

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