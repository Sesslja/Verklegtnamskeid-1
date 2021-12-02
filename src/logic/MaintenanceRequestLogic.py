from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.maintenanceRequestRepo = DB(MaintenanceRequest)
        self.userRepo = DB(User)

    def createMaintenanceRequest(self, address: str, to_do: list, occurrence: str, expert: str, priority: str, date: str, employee: str, verification_number: str, request_status: str) :
        new_maintenance_request = MaintenanceRequest(address,to_do,occurrence,expert,priority,date,employee,verification_number,request_status)
        return self.maintenanceRequestRepo.save(new_maintenance_request)

    def findMaintenanceRequest(self) -> list:
        return self.maintenanceRequestRepo.find()

    def findMRequestByStatus(self, request_status: str): #Closed, Opened, Upcoming, Outstanding
        return self.maintenanceRequestRepo.find({
            'where': {
                'status': request_status
            }
        })

    def createVerificationNumber(self) -> str :
        used_numbers = self.maintenanceRequestRepo.find() # Find all maintenance request to see used numbers
        num_length = len(used_numbers)
        last_number = used_numbers[num_length]
        last_number = int(last_number[:5])
        new_num = last_number+1
        return 'VB'+new_num