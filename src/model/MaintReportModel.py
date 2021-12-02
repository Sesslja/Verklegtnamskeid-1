from model.MaintenanceRequestModel import MaintenanceRequest
from datetime import datetime

class Report(MaintenanceRequest):
    '''Model for Maintenance Report Object'''
    def __init__(self, request_info: MaintenanceRequest=None, propertyId: str=None,maintenance: list=None, isRegular: bool=True, employeeId: str=None, contractorId: str=None, materialcost: int=None, salary: int=None, contractorsfee: float=None, finish_at: datetime=None) -> None:
        super().__init__()
        self.request_info: MaintenanceRequest = request_info
        self.propertyId = propertyId
        self.maintenance = maintenance
        self.isRegular = isRegular
        self.employeeId = employeeId
        self.contractorId = contractorId
        self.materialcost = materialcost
        self.salary = salary
        self.contractorsfee = contractorsfee
        self.finish_at = datetime.now()


