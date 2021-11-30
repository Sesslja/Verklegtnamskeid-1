from model.PropertyModel import Property
from data.database import DB

class PropertyAPI:
    def __init__(self) -> None:
        self.propertyRepo = DB(Property)

    def createProperty(self, address: str, propertyId: str, amenities: list):
        new_property = Property(address, propertyId, amenities)
        return self.propertyRepo.save(new_property)

    def findProperty(self) -> list:
        return self.propertyRepo.find()
    
    def deleteProperty(self, propertyId) -> list:
        return self.propertyRepo.delete(propertyId)

