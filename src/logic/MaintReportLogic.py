from model.MaintenanceRequestModel import MaintenanceRequest
from model.MaintReportModel import Report
from model.userModel import User
from model.PropertyModel import Property
from data.database import DB
from model.AddressType import Address
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from model.BaseModel import BaseModel


class MaintReportAPI:
    '''Logic for maintanece report'''
    def __init__(self) -> None:
        self.reportRepo = DB(Report)
        self.userRepo = DB(User)
        self.propertyRepo = DB(Property)
        self.maintenanceStatus = DB(MaintenanceRequest)
        self.maintReqApi = MaintenanceRequestAPI()


    def createReport(self, request_info, verification_number: str, maintenance: list, contractorId: str, materialCost: int, salary: int, contractorsfee: float, finish_at: str, creator_user):
        '''Creates new report given user data'''
        self.maintReqApi.changeMRequestStatus(verification_number, 'Outstanding')
        new_report = Report(request_info,verification_number, maintenance, contractorId, materialCost, salary, contractorsfee, finish_at, creator_user._id)
        return self.reportRepo.save(new_report)

    def findReport(self) -> list:
        '''Finds all reports, returns list of objects'''
        return self.reportRepo.find()

    def findMReportByVerificationId(self, verification_number: str):
        '''Finds all reports  given verification ID, returns list of objects'''
        return self.reportRepo.find({
            'where': {
                'verification_number': verification_number
            }
        })

