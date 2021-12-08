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

    def createProperty(self, address: str, propertyId: str, amenities: list, rooms: list):
        new_property = Property(address=address, propertyId=propertyId, amenities=amenities, Rooms=rooms)
        return self.propertyRepo.save(new_property)


    def FindRequestsByPropertyID(self, propID):
        '''Shows all requests assigned to property\ngiven property ID'''
        maint_reqs = self.maintReqRepo.find({
            'where': {
                'property_id': propID
            }
        })
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

        for i, f_property in enumerate(properties):
            total_size = 0
            for room in f_property.Rooms:
                total_size += room['size']
            properties[i].total_size = round(total_size)
            properties[i].room_amount = len(f_property.Rooms)
            
            
            properties[i].address_str = Address().addrToString(f_property.Address)


        return properties

    
    def deleteProperty(self, propertyId) -> list:
        return self.propertyRepo.delete(propertyId)

    def findPropertyByPropertyId(self, propertyID: str):
        found_prop = self.propertyRepo.findOne({
            'where': {
                'propertyId': propertyID
            }
        })
        found_prop.address_str = Address().addrToString(found_prop.Address)
        return found_prop

    def findPropertyByCountry(self, country: str):
        return self.propertyRepo.find({
            'where': {
                'Address': {
                    'country': country

                }
            }
        })

    def findPropertyByEmployeeSsn(self, employeeSsn: int):
        try:
            user = self.userRepo.findOne({
                'where': {
                    'ssn': employeeSsn
                }
            })
        except RecordNotFoundError:
            raise RecordNotFoundError

        return self.propertyRepo.find({
            'where': {
                'employees': user._id
            }
        })

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