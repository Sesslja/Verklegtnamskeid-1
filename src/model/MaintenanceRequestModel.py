from model.PropertyModel import Property
from model.AddressType import Address
from model.BaseModel import BaseModel
from datetime import datetime

class MaintenanceRequest(BaseModel) :
    '''Model for Maintenance Request information'''
    def __init__(self,status: str='Open' , property_id: str=None, to_do: list=None, isRegular: bool=True, occurrence: int=None, priority: str=None, start_date: str=None, employeeId = None, verification_number: str=None, contractor_id: str=None) -> None :
        super().__init__()
        self.status = status
        self.property_id = property_id
        self.to_do = to_do
        self.isRegular = isRegular
        self.occurance = occurrence
        self.priority = priority
        self.start_date = datetime(start_date)
        self.employeeId = employeeId
        self.verification_number = verification_number
        self.contractor_id = contractor_id