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
    def __init__(self) -> None:
        self.propertyRepo = DB(Property)
        self.userRepo = DB(User)
        self.destinationApi = DestinationsAPI()
        self.maintReqApi = MaintenanceRequestAPI()
        self.maintReqRepo = DB(MaintenanceRequest)

    def createProperty(self, address: str, propertyId: str, amenities: list, rooms: list):
        new_property = Property(address=address, propertyId=propertyId, amenities=amenities, Rooms=rooms)
        return self.propertyRepo.save(new_property)


    def findRequestsByPropertyID(self, propID):
        '''Shows all maintenance requests requests assigned to property\ngiven property ID'''
        maint_reqs = self.maintReqApi.findRequestsByProperty(propID)
        
        return maint_reqs


    def findIfRoomInProperty(self, propertyId: str, roomId: str):
        try:
            property = self.propertyRepo.find({
                'where': {
                    'propertyId': propertyId,
                    'Rooms': roomId
                }
            })
            return True
        except RecordNotFoundError:
            return False
        

    def findProperties(self, limit=0, page=0) -> list:
        properties = self.propertyRepo.find({
            'limit': {
                'limit': limit,
                'page': page
            }
        })

        new_prop_list = self.insertPropInfo(properties)

        return new_prop_list

    def insertPropInfo(self, prop_list: list[object] | object) -> list[object]:
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
        return self.propertyRepo.delete(propertyId)

    def findPropertyByPropertyId(self, propertyID: str):
        found_prop = self.propertyRepo.findOne({
            'where': {
                'propertyId': propertyID
            }
        })
        
        return self.insertPropInfoSingle(found_prop)

    def findPropertyByCountry(self, country: str):
        found_properties = self.propertyRepo.find({
            'where': {
                'Address': {
                    'country': country

                }
            }
        })

        return self.insertPropInfo(found_properties)

    def findPropertyByEmployeeSsn(self, employeeSsn: int):
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
        '''Creates a room for a property'''
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

    def assignEmployeeToProperty(self, employeeSSN, propertyId):
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