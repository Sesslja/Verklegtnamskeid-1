from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from model.MaintenanceRequestModel import MaintenanceRequest
from logic.DestinationsLogic import DestinationsAPI
from model.AddressType import Address
from data.DBError import RecordNotFoundError
from model.RoomType import RoomType
from model.PropertyModel import Property
from model.userModel import User
from data.database import DB

class PropertyAPI:
    '''Logic for property'''
    def __init__(self) -> None:
        self.propertyRepo = DB(Property)
        self.userRepo = DB(User)
        self.destinationApi = DestinationsAPI()
        self.maintReqApi = MaintenanceRequestAPI()
        self.maintReqRepo = DB(MaintenanceRequest)

    def createProperty(self, address: str, propertyId: str, amenities: list, rooms: list):
        '''Creates property given user data'''
        new_property = Property(address=address, propertyId=propertyId, amenities=amenities, Rooms=rooms)
        return self.propertyRepo.save(new_property)


    def findRequestsByPropertyID(self, propID):
        '''Shows all maintenance requests requests assigned to property\ngiven property ID'''
        maint_reqs = self.maintReqApi.findRequestsByProperty(propID)
        
        return maint_reqs


    def findIfRoomInProperty(self, propertyId: str, roomId: str):
        '''Returns list of property room, given property ID and room id'''
        return self.propertyRepo.find({
                'where': {
                    'propertyId': propertyId,
                    'Rooms': {
                        'roomId': roomId
                    }
                }
            })

        

    def findProperties(self, limit=0, page=0) -> list:
        '''Returns list of all property objects'''
        properties = self.propertyRepo.find({
            'limit': {
                'limit': limit,
                'page': page
            }
        })

        new_prop_list = self.insertPropInfo(properties)

        return new_prop_list

    def insertPropInfo(self, prop_list: list[object] ) -> list[object]:
        '''Inserts room info and address string into object'''
        
        for i, f_property in enumerate(prop_list):
            total_size = 0
            for room in f_property.Rooms:
                total_size += room['size']
            prop_list[i].total_size = round(total_size)
            prop_list[i].room_amount = len(f_property.Rooms)
            
            
            prop_list[i].address_str = Address().addrToString(f_property.Address)
        return prop_list

    def insertPropInfoSingle(self, prop_obj: object) -> list[object]:
        '''Inserts room info and address string into object'''
        total_size = 0
        for room in prop_obj.Rooms:
            total_size += room['size']
        prop_obj.total_size = round(total_size)
        prop_obj.room_amount = len(prop_obj.Rooms)
        
        
        prop_obj.address_str = Address().addrToString(prop_obj.Address)

        return prop_obj


    
    def deleteProperty(self, propertyId) -> list:
        '''Delets property given property ID'''
        return self.propertyRepo.delete(propertyId)

    def findPropertyByPropertyId(self, propertyID: str):
        '''Returns list of property objects, given property ID'''
        found_prop = self.propertyRepo.findOne({
            'where': {
                'propertyId': propertyID
            }
        })
        
        return self.insertPropInfoSingle(found_prop)

    def findPropertyByCountry(self, country: str):
        '''Returns list of property objects, given country'''
        found_properties = self.propertyRepo.find({
            'where': {
                'Address': {
                    'country': country

                }
            }
        })

        return self.insertPropInfo(found_properties)

    def findPropertyByEmployeeSsn(self, employeeSsn: int):
        '''Returns list of property objects, given employee SSN'''
        try:
            user = self.userRepo.findOne({
                'where': {
                    'ssn': employeeSsn
                }
            })
        except RecordNotFoundError:
            raise RecordNotFoundError

        found_prop = self.propertyRepo.find({
            'where': {
                'employees': user._id
            }
        })

        return self.insertPropInfo(found_prop)

    def createRoom(self, propertyId: str, roomId: str=None, size: float=None):
        '''Creates a room for a property given prop ID and user input'''
        if type(size) is not float:
            size = float(size)

        room = RoomType(size=size, roomId=roomId)
        
        found_property = self.propertyRepo.findOne({
            'where': {
                'propertyId': propertyId
            }
        })

        try:
            rooms = found_property.Rooms
        except KeyError:
            rooms = []
        
        rooms.append(room.__dict__)

        found_property.rooms = rooms

        return self.propertyRepo.update({
            '_id': found_property._id,
            'Rooms': rooms
        })

    def updateRooms(self, propertyId, roomList):
        '''updates data of room'''
        updated = self.propertyRepo.update({
            '_id': propertyId,
            'Rooms': roomList
        })
        return updated

    def assignEmployeeToProperty(self, employeeSSN, propertyId):
        '''Assignes employee to a property given employee ssn and Prop ID'''
        user = self.userRepo.findOne({
            'where': {
                'ssn': employeeSSN
            }
        })
        userId = user._id

        found_prop = self.findPropertyByPropertyId(propertyId)

        try:
            current_employees = found_prop.employees
        except KeyError:
            current_employees = []

        current_employees.append(userId)

        return self.propertyRepo.update({
            '_id': found_prop._id,
            'employees': current_employees
        })

    def findEmployeesByPropertyId(self, propertyId):
        '''Returns list of employee objects, given property ID'''
        found_property = self.findPropertyByPropertyId(propertyId)
        employee_ids_in_prop = found_property.employees

        employees_list = []
        for e in employee_ids_in_prop:
            try:
                user = self.userRepo.findOne({
                    'where': {
                        '_id': e
                    }
                })
                employees_list.append(user)
            except RecordNotFoundError:
                pass

        return employees_list

    def findAvailableCountries(self):
        '''Finds countries that are available to create a property in, according to destinations.'''
        return self.destinationApi.findCountriesOfDestinations()