class DBError:
    def __init__(self, error):
        self.error = error

    def __str__(self) -> bool:
        return False

class RecordNotFoundError(LookupError): ...