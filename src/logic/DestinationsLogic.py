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
    
    def deleteDestination(self, _id) -> list:
        return self.destinationsRepo.delete(_id)
    
    #def createDestination(self, country: str=None, city: str=None, zip: str=None, address: Address=None):
    #    new_destination = Destination(country=country, city=city, zip=zip, address=address)
    #    return self.destinationsRepo.save(new_destination)

    def createDestination(self, name: str, address: Address=None, manager: str=None, employees: list[str]=[]):
        new_destination = Destination(name=name, address=address, managerId=manager, employeesIds=employees)
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

    def findCountriesOfDestinations(self) -> list[str]:
        found_destinations = self.destinationsRepo.find()
        country_list = []
        for destination in found_destinations:
            country = destination.Address["country"]
            country_list.append(country)
        
        return country_list

    def findCitiesOfDestinations(self) -> list[str]:
        found_destinations = self.destinationsRepo.find()
        city_list = []
        for destination in found_destinations:
            city = destination.Address["city"]
            city_list.append(city)
        
        return city_list