from model.AddressType import Address
from model.BaseModel import BaseModel

class Destination(BaseModel):
    def __init__(self, address: Address=None) -> None:
        super().__init__()
        #self.country = country
        #self.city = city
        #self.zip_code = zip_code
        self.address: Address = address