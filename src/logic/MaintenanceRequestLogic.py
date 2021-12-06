from model.AddressType import Address
from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.requestRepo = DB(MaintenanceRequest)

    def createMaintenanceRequest(self,status: str, address: Address, to_do: list, isRegular: bool, occurrence: int, priority: str, start_date: str, employeeId: str, verification_number: str):
        new_request = MaintenanceRequest(self,status, address, to_do, isRegular, occurrence, priority, start_date, employeeId, verification_number)
        return self.requestRepo.save(new_request)
    
    def findMaintenanceRequest(self) -> list:
        return self.requestRepo.find()

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