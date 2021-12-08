from model.AddressType import Address
from model.DestinationModel import Destination
from data.database import DB

class DestinationsAPI:
    def __init__(self) -> None:
        self.destinationsRepo = DB(Destination)

    def findDestinations(self) -> list:
        return self.destinationsRepo.find()

    def findDestinationsByZip(self, zip_code) -> list:
        return self.destinationsRepo.find({
            'where': {
                'Address': {
                    'zip': zip_code
                }
            }
        })
    
    def deleteContractor(self, _id) -> list:
        return self.destinationsRepo.delete(_id)
    
    #def createDestination(self, country: str=None, city: str=None, zip: str=None, address: Address=None):
    #    new_destination = Destination(country=country, city=city, zip=zip, address=address)
    #    return self.destinationsRepo.save(new_destination)

    def createDestination(self, address: Address=None):
        new_destination = Destination(address=address)
        return self.destinationsRepo.save(new_destination)

    def findDestinationByCountry(self, country: str):
        return self.destinationsRepo.find({ 
            'where': {
                'Address': {
                    'country': country
                }
            }
        })

    def findDestinationByCity(self, city: str):
        return self.destinationsRepo.find({ 
            'where': {
                'Address': {
                'city': city
                }
            }
        })