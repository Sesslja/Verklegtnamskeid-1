from model.AddressType import Address
from model.userModel import User
from data.database import DB

class UserAPI:
    def __init__(self) -> None:
        self.userRepo = DB(User)

    def createEmployee(self, name: str, email: str, ssn: int, address: Address=None):
        new_user = User(name=name, email=email, ssn=ssn, address=address)
        return self.userRepo.save(new_user)

    def allEmployeesOverview(self, limit=0, page=0) -> list:
        return self.userRepo.find({
            'limit': {
                'limit': limit,
                'page': page
            }
        })

    def deleteEmployee(self, id) -> list:
        return self.userRepo.delete(id)

    def findEmployeesByEmployeeId(self, employeeSsn: str) -> list:
        '''Deprecated do not use.'''
        return self.userRepo.find({ 
            'where': {
                'ssn': employeeSsn
            }
        })

    def findEmployeeByEmployeeId(self, employeeSsn: str):
        return self.userRepo.findOne({ 
            'where': {
                'ssn': employeeSsn
            }
        })
    
    def findEmployeesByCountry(self, country: str):
        return self.userRepo.find({ 
            'where': {
                'Address': {
                    'country': country
                }
            }
        })

    def findEmployee(self, id):
        found = self.userRepo.findOne({
            'where': {
                '_id': id
            }
        })
        try:
            return found['ERROR']
        except TypeError:
            return found

    def findManagers(self):
        return self.userRepo.find({
            'where': {
                'isManager': True
            }
        })

    def updateEmployeeInfo(self, id, data):
        data['_id'] = id
        return self.userRepo.update(data)
    
    def findByAttributy(self, *attr):
        ({"name":"jón"},)
