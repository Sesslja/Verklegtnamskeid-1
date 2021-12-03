from model.PropertyModel import Property
from model.userModel import User
from data.database import DB
from model.AddressType import Address

class PropertyAPI:
    def __init__(self) -> None:
        self.propertyRepo = DB(Property)
        self.userRepo = DB(User)

    def createProperty(self, address: str, propertyId: str, amenities: list):
        new_property = Property(address, propertyId, amenities)
        return self.propertyRepo.save(new_property)

    def findProperty(self) -> list:
        return self.propertyRepo.find()
    
    def deleteProperty(self, propertyId) -> list:
        return self.propertyRepo.delete(propertyId)

    def findPropertyByPropertyId(self, propertyID: int):
        return self.propertyRepo.find({
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
