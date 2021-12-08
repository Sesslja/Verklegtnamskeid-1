from model.AddressType import Address
from model.BaseModel import BaseModel

class Destination(BaseModel):
    def __init__(self, address: Address=None, name: str=None) -> None:
        super().__init__()
        self.Address: Address = address
        self.name = name