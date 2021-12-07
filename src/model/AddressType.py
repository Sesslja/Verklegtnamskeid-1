class Address:
    def __init__(self, country: str=None, city: str=None, zip: str=None, address1: str=None, address2: str=None, address3: str=None) -> None:
        self.country = country
        self.city = city
        self.zip = zip
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3

    def addrToString(self, addr_dict: dict=None):
        addr_obj = addr_dict
        addr_str = ""
        addr_str += (addr_obj['address3'] +', ' if addr_obj['address3'] is not None else '')
        addr_str += (addr_obj['address2'] +', ' if addr_obj['address2'] is not None else '')
        addr_str += (addr_obj['address1'] +', ' if addr_obj['address1'] is not None else '')
        addr_str += (addr_obj['city'] +', ' if addr_obj['city'] is not None else '')
        addr_str += (addr_obj['country'] +', ' if addr_obj['country'] is not None else '')
        addr_str += (str(addr_obj['zip']) +'' if addr_obj['zip'] is not None else '')
        return addr_str