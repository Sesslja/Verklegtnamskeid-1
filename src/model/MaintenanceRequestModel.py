from model.AddressType import Address
from model.BaseModel import BaseModel
from datetime import datetime

class MaintenanceRequest(BaseModel) :
    '''Model for Maintenance Request information'''
    def __init__(self,isOpen: bool=True, isFinished: bool = False, isClosed: bool=False, address: Address=None, to_do: list=None, occurrence: str=None, priority: str=None, start_date: datetime=None, employeeId: int=None, verification_number: str=None) -> None :
        super().__init__()
        self.isOpen = isOpen
        self.isFinished = isFinished
        self.isClosed = isClosed
        self.Address: Address = address
        self.to_do = to_do
        self.occurance = occurrence
        self.priority = priority
        self.start_date = datetime.now()
        self.employeeId = employeeId
        self.verification_number = verification_number