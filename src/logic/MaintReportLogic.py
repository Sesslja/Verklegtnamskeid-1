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


    def createReport(self, request_info, verification_number: str, propertyId: str, maintenance: list, contractorId: str, materialcost: int, salary: int, contractorsfee: float, finish_at: float):
        MaintenanceRequestAPI.changeMRequestStatus(self, verification_number, 'Finished')
        new_report = Report(request_info,verification_number, propertyId, maintenance, contractorId, materialcost, salary, contractorsfee, finish_at)
        return self.reportRepo.save(new_report)

    def findReport(self) -> list:
        return self.reportRepo.find()


    def findReportByEmployee(self, employeeId: str):
        user = self.userRepo.find({
            'where': {
                'ssn': employeeId
            }
        })

        return self.reportRepo.find({
            'where': {
                'employeeId': employeeId
            }
        })
    
    def findReportByProperty(self, propertyId: str):
        property = self.propertyRepo.find({
            'where': {
                'propertyId': propertyId
            }
        })

        return self.reportRepo.find({
            'where': {
                'propertyId': propertyId
            }
        })

    def findReportByDate(self, startDate: list, endDate: list):
        start_Date = BaseModel.datetimeToUtc(startDate)
        end_Date = BaseModel.datetimeToUtc(endDate)
        x = range(start_Date, end_Date)
        return self.reportRepo.find({
            'where': {
                'finish_date': x
                
            }
        })

