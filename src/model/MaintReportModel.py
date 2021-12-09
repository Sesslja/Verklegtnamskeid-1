from model.MaintenanceRequestModel import MaintenanceRequest
from model.BaseModel import BaseModel

class Report(BaseModel):
    '''Model for Maintenance Report Object'''
    def __init__(self, request_info: MaintenanceRequest=None,verificationNumber: MaintenanceRequest=None,maintenance: list=None, contractorId: str=None, materialcost: int=None, salary: int=None, contractorsfee: float=None, finish_at: str=None) -> None:
        super().__init__()
        self.request_info: MaintenanceRequest = request_info
        self.verification_number = MaintenanceRequest().verification_number = verificationNumber
        self.maintenance = maintenance
        self.contractorId = contractorId
        self.materialcost = materialcost
        self.salary = salary
        self.contractorsfee = contractorsfee
        self.finish_at = self.datetimeToUtc()


