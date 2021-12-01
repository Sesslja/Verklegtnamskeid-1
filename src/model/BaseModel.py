import uuid
from datetime import datetime

class BaseModel:
    '''Base Model that all other models inherit from'''
    # Make sure every input has a default value, validation should be done in the logic layer for this application.
    def __init__(self, isActive: bool=True, isArchived: bool = False, created_at: str=None,_id: str=None) -> None:
        self._id = _id
        self.created_at: str = datetime.now()
        self.isActive = isActive
        self.isArchived = isArchived

    def modelLocals():
        return locals()