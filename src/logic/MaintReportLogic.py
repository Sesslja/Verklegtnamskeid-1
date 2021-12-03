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

    def createReport(self, maintenanceId: int, propertyId: str=None,address: Address=None, maintenance: list=None, isRegular: bool=True, employeeId: str=None, contractorId: str=None, materialcost: int=None, salary: int=None, contractorsfee: float=None, finish_at: str=None):
        new_report = Report(maintenanceId, propertyId,address, maintenance, isRegular, employeeId, contractorId, materialcost, salary, contractorsfee, finish_at)
        return self.reportRepo.save(new_report)

    def findReport(self) -> list:
        return self.reportRepo.find()

    def findReportByMaintenanceId(self, maintenanceId: int):
        return self.reportRepo.find({
            'where': {
                'maintenanceId': maintenanceId
            }
        })

    def findReportByEmployee(self, employeeId: int):
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
    
    def findReportByProperty(self, propertyId: int):
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
                
            }
        }))

