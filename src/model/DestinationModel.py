from model.AddressType import Address
from model.BaseModel import BaseModel

class Destination(BaseModel):
    '''Model for destinations Object'''
    def __init__(self, address: Address=None, name: str=None, employeesIds: list[str]=[], managerId: str=None, verification_number: str=None) -> None:
        super().__init__()
        self.Address: Address = address
        self.name = name
        self.employees = employeesIds
        self.manager = managerId
        self.verification_number = verification_number