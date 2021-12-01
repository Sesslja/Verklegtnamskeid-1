from model.BaseModel import BaseModel

class Property(BaseModel):
    def __init__(self, address: str=None, propertyId: str=None, amenities: list=None, employees: list=None) -> None:
        super().__init__()
        # ID Er unique generated tala fyrir hvern og einn notanda
        self.address = address
        self.propertyId = propertyId
        self.amenities = amenities
        self.employees = employees

