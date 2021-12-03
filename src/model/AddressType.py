class Address:
    def __init__(self, country: str=None, city: str=None, zip: str=None, address1: str=None, address2: str=None, address3: str=None) -> None:
        self.country = country
        self.city = city
        self.zip = zip
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
