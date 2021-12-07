from datetime import datetime
from datetime import timezone
from typing import List

class BaseModel:
    '''Base Model that all other models inherit from'''
    # Make sure every input has a default value, validation should be done in the logic layer for this application.
    def __init__(self, isActive: bool=True, isArchived: bool = False, created_at: str=None,_id: str=None) -> None:
        self._id = _id
        self.created_at: str = created_at
        self.isActive = isActive
        self.isArchived = isArchived

    def modelLocals():
        return locals()

    def datetimeToUtc(self, start_date: list=None):
        start_date = start_date
        if start_date is None:
            dt = datetime.now()
            date = dt.replace(tzinfo=timezone.utc).timestamp()
        else:
            dt = datetime(start_date[0], start_date[1], start_date[2])
            date = dt.replace(tzinfo=timezone.utc).timestamp()
        return int(date) 

