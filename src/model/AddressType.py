class Address:
    def __init__(self, country: str=None, city: str=None, zip: str=None, address1: str=None, address2: str=None, address3: str=None) -> None:
        self.country: str = country
        self.city: str = city
        self.zip: int = zip
        self.address1: str = address1
        self.address2: str = address2
        self.address3: str = address3
