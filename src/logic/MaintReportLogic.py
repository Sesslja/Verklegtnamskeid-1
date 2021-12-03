from datetime import datetime
from MaintenanceRequestModel import MaintenanceRequest
from model.MaintReportModel import Report
from model.userModel import User
from model.PropertyModel import Property
from data.database import DB
from model.AddressType import Address

class MaintReportAPI:
    def __init__(self) -> None:
        self.reportRepo = DB(Report)
        self.userRepo = DB(User)
        self.propertyRepo = DB(Property)

    def createReport(self, request_info: str, propertyId: str, maintenance: list, isRegular: bool, contractorId: str, materialcost: int, salary: int, contractorsfee: float, finish_at: datetime):
        new_report = Report(request_info, propertyId, maintenance, isRegular, contractorId, materialcost, salary, contractorsfee, finish_at)
        return self.reportRepo.save(new_report)

    def findReport(self) -> list:
        return self.reportRepo.find()
    
    def deleteReport(self, verification_number) -> list:
        return self.reportRepo.delete(verification_number)

    def findReportByVerification_number(self, verification_number):
        return self.reportRepo.find({
            'where': {
                'MaintenanceRequest': {
                    'verification_number': verification_number
                } 
            }
        })

    def findReportByEmployee(self, employeeId: str):
        user = self.userRepo.find({
            'where': {
                'ssn': employeeId
            }
        })

        return self.reportRepo.find({
            'where': {
                'MaintenanceRequest '
                    'employeeId': employeeId
            }
        })
    
    def findReportByProperty(self, propertyId: str):
        user = self.propertyRepo.find({
            'where': {
                'propertyId': propertyId
            }
        })

        return self.reportRepo.find({
            'where': {
                'propertyId': propertyId
            }
        })

    def findReportByDate(self, startDate: str, endDate: str):
        return self.reportRepo(find({
            'where': {
                ''
                
            }
        }))

