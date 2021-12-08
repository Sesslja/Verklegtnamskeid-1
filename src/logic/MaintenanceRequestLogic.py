from model.PropertyModel import Property
from model.AddressType import Address
from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB
from model.BaseModel import BaseModel

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.requestRepo = DB(MaintenanceRequest)

    def createMaintenanceRequest(self,status: str, property_id: str, to_do: list, isRegular: bool, occurrence: int, priority: str, start_date: str=None, employee_Id =None):
        new_request = MaintenanceRequest(status, property_id, to_do, isRegular, occurrence, priority, start_date, employee_Id, self.createVerificationNumber())
        return self.requestRepo.save(new_request)
    
    def MaintenanceRequestOverview(self) -> list :
        return self.requestRepo.find()
    
    def findOneByVerificationNumber(self, verification_number: str) -> dict:
        return self.requestRepo.findOne({
            'where': {
                'verification_number': verification_number
            }
        })

    def findMRequestByStatus(self, request_status: str): #Closed, Opened, Upcoming, Outstanding
        return self.requestRepo.find({
            'where': {
                'status': request_status
            }
        })

    def createVerificationNumber(self):
        used_numbers = self.requestRepo.find() # Find all maintenance request to see used numbers
        num_length = len(used_numbers) - 1
        last_number = used_numbers[num_length].verification_number
        last_number = int(last_number[2:])
        new_num = str(last_number+1).zfill(5)
        verification_number = 'VB'+new_num
        return verification_number
    
    def changeMRequestStatus(self, id, status):
        data = {
            'id': id,
            'status': status
        }
        return self.requestRepo.update(data)
    
    def findMRequestByVerificationId(self, verification_number: str):
        return self.requestRepo.find({
            'where': {
                'verification_number': verification_number
            }
        })
    
    
    def findRequestByEmployee(self, employeeId: str):
        user = self.userRepo.find({
            'where': {
                'ssn': employeeId
            }
        })

        return self.requestRepo.find({
            'where': {
                'employeeId': employeeId
            }
        })
    
    def findRequestByProperty(self, propertyId: str):
        property = self.propertyRepo.find({
            'where': {
                'propertyId': propertyId
            }
        })

        return self.requestRepo.find({
            'where': {
                'propertyId': propertyId
            }
        })

    def findRequestByDate(self, startDate: list, endDate: list):
        start_Date = BaseModel.datetimeToUtc(startDate)
        end_Date = BaseModel.datetimeToUtc(endDate)
        x = range(start_Date, end_Date)
        return self.requestRepo.find({
            'where': {
                'finish_date': x
                
            }
        })