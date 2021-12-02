from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB
import random

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.requestRepo = DB(MaintenanceRequest)

    def createMaintenanceRequest(self, address: str, to_do: list, occurrence: str, priority: str, start_date: str, employeeid: int, verification_number: str) :
        new_maintenance_request = MaintenanceRequest(address,to_do,occurrence,priority,start_date,employeeid,verification_number)
        return self.requestRepo.save(new_maintenance_request)
    
    def findMaintenanceRequest(self) -> list:
        return self.requestRepo.find()

    def findOpenedMRequest(self, isOpen: bool=True) -> list : 
        p
        return self.reportRepo.find({
            'where': {
                'maintenanceId': maintenanceId
            }
        })

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