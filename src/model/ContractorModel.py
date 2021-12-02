from model.AddressType import Address
from model.BaseModel import BaseModel

class Contractor(BaseModel):
    '''Model for Contractor Object'''
    def __init__(self, companyname: str=None, name: str=None, ssn: int=None, profession: str=None, phone: int=None, openinghours: str=None, address: Address=None) -> None:
        super().__init__()
        self.companyname = companyname
        self.name = name
        self.ssn = ssn
        self.profession = profession
        self.phone = phone
        self.Address: Address = address
