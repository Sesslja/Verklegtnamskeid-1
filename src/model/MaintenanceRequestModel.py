from PropertyModel import Property
from model.AddressType import Address
from model.BaseModel import BaseModel
from datetime import datetime
from model.StatusModel import Status

class MaintenanceRequest(BaseModel) :
    '''Model for Maintenance Request information'''
    def __init__(self,status: str='Open' , property: Property = None, to_do: list=None, isRegular: bool=True, occurrence: int=None, priority: str=None, start_date: str=None, employeeId = None, verification_number: str=None) -> None :
        super().__init__()
        self.status = Status(status)
        self.property: Property = property
        self.to_do = to_do
        self.isRegular = isRegular
        self.occurance = occurrence
        self.priority = priority
        self.start_date = self.datetimeToUtc()
        self.employeeId = employeeId
        self.verification_number = verification_number



