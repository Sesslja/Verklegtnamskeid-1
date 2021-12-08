from model.AddressType import Address
from model.DestinationModel import Destination
from data.database import DB

class DestinationsAPI:
    def __init__(self) -> None:
        self.destinationsRepo = DB(Destination)

    def findDestination(self) -> list:
        return self.destinationsRepo.find()
    
    def createDestination(self, country=None, city=None, zip_code=None, address: Address=None):
        new_destination = Destination(country=country, city=city, zip_code=zip_code, address=address)
        return self.destinationsRepo.save(new_destination)

    def findDestinationByCountry(self, country: str):
        return self.destinationsRepo.find({ 
            'where': {
                'country': country
            }
        })

    def findDestinationByCity(self, city: str):
        return self.destinationsRepo.find({ 
            'where': {
                'city': city
            }
        })