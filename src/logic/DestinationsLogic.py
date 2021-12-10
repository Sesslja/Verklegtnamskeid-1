from model.AddressType import Address
from model.DestinationModel import Destination
from data.database import DB

class DestinationsAPI:
    '''logic for destination'''
    def __init__(self) -> None:
        self.destinationsRepo = DB(Destination)

    def findDestinations(self) -> list:
        '''Finds all destinations in a list of objects'''
        return self.destinationsRepo.find()

    def findDestinationsByZip(self, zip_code) -> list:
        '''Finds all destinations given zip code in a list of objects '''
        return self.destinationsRepo.find({
            'where': {
                'Address': {
                    'zip': zip_code
                }
            }
        })
    
    def deleteDestination(self, _id) -> list:
        '''Delets destination given destination ID'''
        return self.destinationsRepo.delete(_id)

    def createDestination(self, name: str, address: Address=None, manager: str=None, employees: list[str]=[]):
        '''Creates new destination'''
        new_destination = Destination(name=name, address=address, managerId=manager, employeesIds=employees, verification_number=self.createVerificationNumber())
        return self.destinationsRepo.save(new_destination)

    def findDestinationByCountry(self, country: str):
        '''Finds destination given country string and returns list of objects'''
        return self.destinationsRepo.find({ 
            'where': {
                'Address': {
                    'country': country
                }
            }
        })

    def findDestinationByCity(self, city: str):
        '''Finds destination given city string and returns list of objects'''
        return self.destinationsRepo.find({ 
            'where': {
                'Address': {
                'city': city
                }
            }
        })

    def findCountriesOfDestinations(self) -> list[str]:
        '''Finds destination  and returns list of objects'''
        found_destinations = self.destinationsRepo.find()
        country_list = []
        for destination in found_destinations:
            country = destination.Address["country"]
            country_list.append(country)
        
        return country_list

    def findCitiesOfDestinations(self) -> list[str]:
        '''Finds cities given country string and returns list of objects'''
        found_destinations = self.destinationsRepo.find()
        city_list = []
        for destination in found_destinations:
            city = destination.Address["city"]
            city_list.append(city)
        
        return city_list
    
    def findDestinationByID(self, destinationId: str):
        '''Finds destination given destination ID string and returns list of objects'''
        return self.destinationsRepo.findOne({
            'where': {
                '_id': destinationId
            }
        })

    def updateDestinationInfo(self, id, data):
        '''updates destination info given destination ID and new data'''
        data['_id'] = id
        return self.destinationsRepo.update(data)

    def createVerificationNumber(self):
        '''Creates verification number to a new destination'''
        try:
            used_numbers = self.destinationsRepo.find() # Find all maintenance request to see used numbers
            num_length = len(used_numbers) - 1
            last_number = used_numbers[num_length].verification_number
            last_number = int(last_number[2:])
        except IndexError:
            last_number = 0
        new_num = str(last_number+1).zfill(5)
        verification_number = 'D'+new_num
        return verification_number

    def findDestinationByVerificationNumber(self, verification_number: str):
        '''Finds destination given verification number string and returns list of objects'''
        return self.destinationsRepo.find({
            'where': {
                'verification_number': verification_number
            }
        })

    def findOneByVerificationNumber(self, verification_number: str) -> dict:
        return self.destinationsRepo.findOne({
            'where': {
                'verification_number': verification_number
            }
        })