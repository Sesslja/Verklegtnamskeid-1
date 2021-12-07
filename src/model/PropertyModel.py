from model.AddressType import Address
from model.BaseModel import BaseModel
from model.RoomType import RoomType


class Property(BaseModel):
    def __init__(self, address: str=None, propertyId: str=None, amenities: list=None, employees: list=[], Rooms: list[RoomType]=[]) -> None:
        super().__init__()
        # ID Er unique generated tala fyrir hvern og einn notanda
        self.Address: Address = address
        self.propertyId = propertyId
        self.amenities = amenities
        self.employees: list = employees
        self.Rooms: list[RoomType] = Rooms
