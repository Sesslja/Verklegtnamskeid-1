from model.AddressType import Address
from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.requestRepo = DB(MaintenanceRequest)

    def createMaintenanceRequest(self, address: Address, to_do: list, occurrence: str, priority: str, start_date: str, employeeid: str, verification_number: str) :
        new_maintenance_request = MaintenanceRequest(address,to_do,occurrence,priority,start_date,employeeid,verification_number)
        return self.requestRepo.save(new_maintenance_request)
    
    def findMaintenanceRequest(self) -> list:
        return self.requestRepo.find()

    def findMRequestByStatus(self, request_status: str): #Closed, Opened, Upcoming, Outstanding
        return self.requestRepo.find({
            'where': {
                'status': request_status
            }
        })

    def createVerificationNumber(self) -> str :
        used_numbers = self.requestRepo.find() # Find all maintenance request to see used numbers
        num_length = len(used_numbers)
        last_number = used_numbers[num_length]
        last_number = int(last_number[:5])
        new_num = last_number+1
        return 'VB'+new_num
    
    def changeMRequestStatus(self, id, status):
        data = {
            'id': id,
            'status': status
        }
        return self.requestRepo.update(data)