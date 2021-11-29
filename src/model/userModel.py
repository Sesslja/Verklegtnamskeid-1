from model.BaseModel import BaseModel

class User(BaseModel):
    def __init__(self, name: str = None, email: str=None, ssn: int=None, isManager: bool=False) -> None:
        super().__init__()
        # ID Er unique generated tala fyrir hvern og einn notanda
        self.name = name
        self.email = email
        self.isManager = isManager
        self.ssn = ssn
