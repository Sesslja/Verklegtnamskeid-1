from model.AddressType import Address
from model.BaseModel import BaseModel


class Property(BaseModel):
    def __init__(self, address: Address = None, propertyId: str=None, amenities: list=None,  employeeIds: list=None) -> None:
        super().__init__()
        # ID Er unique generated tala fyrir hvern og einn notanda
        self.Address: Address = address
        self.propertyId = propertyId
        self.amenities = amenities
        self.employeeIds = employeeIds

Property(Address())