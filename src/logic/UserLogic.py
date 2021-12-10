from model.AddressType import Address
from model.userModel import User
from data.database import DB
from model.MaintenanceRequestModel import MaintenanceRequest

class UserAPI:
    def __init__(self) -> None:
        self.userRepo = DB(User)
        self.maintReqRepo = DB(MaintenanceRequest)

    def createEmployee(self, name: str, email: str, ssn: int, address: Address=None, isManegar: bool=False, phone: list = None):
        new_user = User(name=name, email=email, ssn=ssn, address=address, isManager=isManegar, phone=phone)
        return self.userRepo.save(new_user)

    def allEmployeesOverview(self, limit=0, page=0) -> list:
        return self.userRepo.find({
            'limit': {
                'limit': limit,
                'page': page
            }
        })

    def FindRequestsByUserID(self, userID):
        '''Shows all requests assigned to contractor\ngiven contractor SSN'''
        maint_reqs = self.maintReqRepo.find({
            'where': {
                'employees': userID
            }
        })
        return maint_reqs


    def deleteEmployee(self, id) -> list:
        return self.userRepo.delete(id)

    def findEmployeesByEmployeeId(self, employeeId: str) -> list:
        '''Deprecated do not use.'''
        return self.userRepo.find({ 
            'where': {
                'ssn': employeeId
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
    
    def findManagersByCountry(self, country: str):
        return self.userRepo.find({
            'where': {
                'isManager': True,
                'Address': {
                    'country': country
                }
            }
        })

    def updateEmployeeInfo(self, id, data):
        data['_id'] = id
        return self.userRepo.update(data)
    
    def findByAttributy(self, *attr):
        ({"name":"jón"},)
