from model.BaseModel import BaseModel

class Property(BaseModel):
    def __init__(self, address: str, propertyId: str, amenities: list) -> None:
        super().__init__()
        # ID Er unique generated tala fyrir hvern og einn notanda
        self.address = address
        self.propertyId = propertyId
        self.amenities = amenities
