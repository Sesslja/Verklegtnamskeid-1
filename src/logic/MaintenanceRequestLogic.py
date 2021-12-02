from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB
import random

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.maintenanceRequestRepo = DB(MaintenanceRequest)

    def createMaintenanceRequest(self, address: str, to_do: list, occurrence: str, expert: str, priority: str, date: str, employee: str, verification_number: str) :
        new_maintenance_request = MaintenanceRequest(address,to_do,occurrence,expert,priority,date,employee,verification_number)
        return self.maintenanceRequestRepo.save(new_maintenance_request)
    
    def findMaintenanceRequest(self) -> list:
        return self.maintenanceRequestRepo.find()

    def findOpenedMRequest(self) -> list : 
        pass

    def findClosedMRequest(self) -> list : 
        pass

    def findUpcomingMRequest(self) -> list : 
        pass

    def findOutstandingMRequest(self) -> list :
        pass
    
    def createVerificationNumber(self) -> str :
        pass

    def findOpenedMRequest(self, request_status: str):
        return self.maintenanceRequestRepo.find({
            'where': {
                'propertyId': request_status
            }
        })