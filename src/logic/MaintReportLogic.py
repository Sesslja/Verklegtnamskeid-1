from model.MaintenanceRequestModel import MaintenanceRequest
from model.MaintReportModel import Report
from model.userModel import User
from model.PropertyModel import Property
from data.database import DB
from model.AddressType import Address
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from model.BaseModel import BaseModel


class MaintReportAPI:
    def __init__(self) -> None:
        self.reportRepo = DB(Report)
        self.userRepo = DB(User)
        self.propertyRepo = DB(Property)
        self.maintenanceStatus = DB(MaintenanceRequest)
        self.maintReqApi = MaintenanceRequestAPI()


    def createReport(self, request_info, verification_number: str, maintenance: list, contractorId: str, materialcost: int, salary: int, contractorsfee: float, dt: str):
        self.maintReqApi.changeMRequestStatus(verification_number, 'Finished')
        new_report = Report(request_info,verification_number, maintenance, contractorId, materialcost, salary, contractorsfee, dt)
        return self.reportRepo.save(new_report)

    def findReport(self) -> list:
        return self.reportRepo.find()

    def findMReportByVerificationId(self, verification_number: str):
        return self.reportRepo.find({
            'where': {
                'verification_number': verification_number
            }
        })

