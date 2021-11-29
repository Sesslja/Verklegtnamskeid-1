class BaseModel:
    id: str
    created_at: str
    isActive: bool
    isArchived: bool
    def __init__(self, isActive: bool=True, isArchived: bool = False) -> None:
        self.id = 'generated Id'
        self.created_at: str = 'date now'
        self.isActive = isActive
        self.isArchived = isArchived

    def modelLocals():
        return locals()