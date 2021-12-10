class RoomType:
    '''Model for Room Object'''
    def __init__(self, size: float=None, roomId: str=None) -> None:
        self.size = size # Size in m^2
        self.roomId = roomId
