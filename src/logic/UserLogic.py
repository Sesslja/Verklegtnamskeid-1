from model.AddressType import Address
from model.userModel import User
from data.database import DB

class UserAPI:
    def __init__(self) -> None:
        self.userRepo = DB(User)

    def createEmployee(self, name: str, email: str, ssn: int, address: Address=None):
        new_user = User(name=name, email=email, ssn=ssn, address=address)
        return self.userRepo.save(new_user)

    def findEmployees(self) -> list:
        return self.userRepo.find()

    def deleteEmployee(self, id) -> list:
        return self.userRepo.delete(id)

    def findEmployeesByEmployeeId(self, employeeId: int):
        return self.userRepo.find({ 
            'where': {
                'ssn': employeeId
            }
        })
    
    def findEmployeesByCountry(self, country: str):
        return self.userRepo.find({ 
            'where': {
                'address': {
                    'country': country
                }
            }
        })
