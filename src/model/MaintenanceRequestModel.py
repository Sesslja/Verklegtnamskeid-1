

from model.AddressType import Address
from model.BaseModel import BaseModel

class MaintenanceRequest(BaseModel) :
    '''Model for Maintenance Request information'''
    def __init__(self, address: str=None, to_do: list=None, occurrence: str=None, expert: str=None, priority: str=None, date: str=None, contractor: str=None, verification_number: str=None) -> None :
        super().__init__()
        self.address = address
        self.to_do = to_do
        self.occurance = occurrence
        self.expert = expert
        self.priority = priority
        self.date = date
        self.contractor = contractor
        self.verification_number = verification_number