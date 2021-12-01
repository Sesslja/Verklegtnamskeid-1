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

    def getOpenedMRequest(self) -> list : 
        pass

    def getClosedMRequest(self) -> list : 
        pass

    def upcomingMRequest(self) -> list : 
        pass

    def outstandingMRequest(self) -> list :
        pass
    
    def createVerificationNumber(self) -> str :
        pass