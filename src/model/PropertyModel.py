from model.BaseModel import BaseModel
from model.RoomType import RoomType

class Property(BaseModel):
    def __init__(self, address: str=None, propertyId: str=None, amenities: list=None, employees: list=None, rooms: list[RoomType]=[]) -> None:
        super().__init__()
        # ID Er unique generated tala fyrir hvern og einn notanda
        self.address = address
        self.propertyId = propertyId
        self.amenities = amenities
        self.employees = employees
        self.rooms = rooms
