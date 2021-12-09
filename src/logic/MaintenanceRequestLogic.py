import re
from model.PropertyModel import Property
from model.AddressType import Address
from model.MaintenanceRequestModel import MaintenanceRequest
from model.userModel import User
from data.database import DB
from model.BaseModel import BaseModel

class MaintenanceRequestAPI :

    def __init__(self) -> None :
        self.requestRepo = DB(MaintenanceRequest)
        self.propertyRepo = DB(Property)
        self.userRepo = DB(User)

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
    
    def MaintenanceRequestOverview(self) -> list :
        return self.requestRepo.find()
    
    def findOneByVerificationNumber(self, verification_number: str) -> dict:
        return self.requestRepo.findOne({
            'where': {
                'verification_number': verification_number
            }
        })

    def findMRequestByStatus(self, request_status: str): #Closed, Opened, Upcoming, Outstanding
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
    
    def changeMRequestStatus(self, verification_number, status):
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
        user = self.userRepo.find({
            'where': {
                'ssn': employeeId
            }
        })

        return self.requestRepo.find({
            'where': {
                'employeeId': employeeId
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
        start_Date = BaseModel.datetimeToUtc(startDate)
        end_Date = BaseModel.datetimeToUtc(endDate)
        x = range(start_Date, end_Date)
        return self.requestRepo.find({
            'where': {
                'finish_date': x
                
            }
        })

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