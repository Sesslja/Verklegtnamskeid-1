from model.AddressType import Address
from model.BaseModel import BaseModel
from datetime import datetime

class Report(BaseModel):
    '''Model for Maintenance Report Object'''
    def __init__(self, maintenanceId: int, propertyId: str=None,address: Address=None, maintenance: list=None, isRegular: bool=True, employeeId: str=None, contractorId: str=None, materialcost: int=None, salary: int=None, contractorsfee: float=None, finish_at: datetime=None) -> None:
        super().__init__()
        self.maintenanceId = maintenanceId
        self.propertyId = propertyId
        self.Adress = Address = address
        self.maintenance = maintenance
        self.isRegular = isRegular
        self.employeeId = employeeId
        self.contractorId = contractorId
        self.materialcost = materialcost
        self.salary = salary
        self.contractorsfee = contractorsfee
        self.finish_at = datetime.now()
