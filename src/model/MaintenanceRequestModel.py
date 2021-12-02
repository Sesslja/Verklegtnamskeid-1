from model.AddressType import Address
from model.BaseModel import BaseModel
from datetime import datetime

class MaintenanceRequest(BaseModel) :
    '''Model for Maintenance Request information'''
    def __init__(self, address: Address=None, to_do: list=None, occurrence: str=None, priority: str=None, start_date: datetime=None, verification_number: str=None) -> None :
        super().__init__()
        self.Address: Address = address
        self.to_do = to_do
        self.occurance = occurrence
        self.priority = priority
        self.start_date = datetime.now()
        self.verification_number = verification_number