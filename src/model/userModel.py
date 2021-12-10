from model.AddressType import Address
from model.BaseModel import BaseModel

class User(BaseModel):
    '''Model for User Object'''
    # Make sure every input has a default value, validation should be done in the logic layer for this application.
    def __init__(self, name: str = None, email: str=None, ssn: str=None, address: Address=None, isManager: bool=False, phone: list[str] = []) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.isManager = isManager
        self.ssn = ssn
        self.Address: Address = address
        self.phone = phone
