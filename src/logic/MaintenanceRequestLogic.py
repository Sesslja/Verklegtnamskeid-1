import re
from model.PropertyModel import Property
from model.AddressType import Address
from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB
from model.BaseModel import BaseModel
from logic.DatetimeLogic import DateTime
from model.MaintReportModel import Report

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.requestRepo = DB(MaintenanceRequest)
        self.reportRepo = DB(Report)
        self.propertyRepo = DB(Property)
        self.userRepo = DB(User)
        self.datetime = DateTime()

    def createMaintenanceRequest(self,status: str, property_id: str, to_do: list, isRegular: bool, occurrence: int, priority: str, start_date: str=None, employees: list=None, roomNumId: str=None):
        found_prop = self.propertyRepo.findOne({
            'where': {
                'propertyId': property_id
            }
        })

        new_request = MaintenanceRequest(
            status=status, 
            property_id=found_prop._id, 
            to_do=to_do, 
            isRegular=isRegular, 
            occurrence=occurrence, 
            priority=priority, 
            start_date=start_date, 
            employees=employees, 
            verification_number=self.createVerificationNumber(),
            roomNumId=roomNumId
        )
        return self.requestRepo.save(new_request)
    
    def MaintenanceRequestOverview(self) -> list:
        return self.requestRepo.find()
    
    def findOneByVerificationNumber(self, verification_number: str) -> object:
        return self.requestRepo.findOne({
            'where': {
                'verification_number': verification_number
            }
        })

    def findMRequestByStatus(self, request_status: str): #Opened, Closed, Outstanding
        return self.requestRepo.find({
            'where': {
                'status': request_status
            }
        })

    def createVerificationNumber(self):
        try:
            used_numbers = self.requestRepo.find() # Find all maintenance request to see used numbers
            num_length = len(used_numbers) - 1
            last_number = used_numbers[num_length].verification_number
            last_number = int(last_number[2:])
        except IndexError:
            last_number = 0
        new_num = str(last_number+1).zfill(5)
        verification_number = 'VB'+new_num
        return verification_number
    
    def changeMRequestStatus(self, verification_number: str, status):
        found_req = self.findOneByVerificationNumber(verification_number)
        data = {
            '_id': found_req._id,
            'status': status
        }
        return self.requestRepo.update(data)
    
    def findMRequestByVerificationId(self, verification_number: str):
        return self.requestRepo.find({
            'where': {
                'verification_number': verification_number
            }
        })
    
    
    def findRequestByEmployee(self, employeeId: str):
        user = self.userRepo.findOne({
            'where': {
                'ssn': employeeId
            }
        })

        return self.requestRepo.find({
            'where': {
                'employees': user._id
            }
        })
    
    def findRequestsByProperty(self, propertyId: str):
        found_property = self.propertyRepo.findOne({
            'where': {
                'propertyId': propertyId
            }
        })

        found_req = self.requestRepo.find({
            'where': {
                'property_id': found_property._id
            }
        })
        
        for i, req in enumerate(found_req): # Insert relationships into the Maintenance Request
            found_req[i] = self.insertRelationsIntoRequest(req)

        return found_req

    def findRequestByDate(self, startDate: list, endDate: list):
        startDate = startDate.split(',')
        endDate = endDate.split(',')
        request_list = []
        dateList = self.datetime.betweenTwoDates(startDate, endDate)
        for date in dateList:
            foundItem = self.requestRepo.find({
                'where': {
                    'start_date': date
                }
            })
            for foundRequest in foundItem:
                request_list.append(foundRequest)

        return request_list




    def insertRelationsIntoRequest(self, inp_obj) -> object:
        ''' Insert relationships into request '''
        employee_list = []
        for employee_id in inp_obj.employees:
            found_employee = self.userRepo.findOne({
                'where': {
                    '_id': employee_id
                }
            })
            employee_list.append(found_employee)
        
        inp_obj.employee_list = employee_list
        return inp_obj