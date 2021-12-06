from model.PropertyModel import Property
from model.userModel import User
from data.database import DB

class PropertyAPI:
    def __init__(self) -> None:
        self.propertyRepo = DB(Property)
        self.userRepo = DB(User)

    def createProperty(self, address: str, propertyId: str, amenities: list, rooms: list):
        new_property = Property(address=address, propertyId=propertyId, amenities=amenities, rooms=rooms)
        return self.propertyRepo.save(new_property)

    def findProperties(self, limit=0, page=0) -> list:
        properties = self.propertyRepo.find({
            'limit': {
                'limit': limit,
                'page': page
            }
        })

        for i, property in enumerate(properties):
            total_size = 0
            for room in property.rooms:
                total_size += room['size']
            properties[i].total_size = round(total_size)
            properties[i].room_amount = len(property.rooms)

        return properties

    
    def deleteProperty(self, propertyId) -> list:
        return self.propertyRepo.delete(propertyId)

    def findPropertyByPropertyId(self, propertyID: str):
        return self.propertyRepo.findOne({
            'where': {
                'propertyId': propertyID
            }
        })

    def findPropertyByCountry(self, country: str):
        return self.propertyRepo.find({
            'where': {
                'Address': {
                    'country': country

                }
            }
        })

    def findPropertyByEmployee(self, employeeIds: int):
        user = self.userRepo.find({
            'where': {
                'ssn': employeeIds
            }
        })

        return self.propertyRepo.find({
            'where': {
                'employeeIds': employeeIds
            }
        })
