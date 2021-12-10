from data.DBError import RecordNotFoundError
from model.MaintenanceRequestModel import MaintenanceRequest
from model.AddressType import Address
from model.ContractorModel import Contractor
from data.database import DB

class ContractorAPI:
    '''Logic for contractor'''
    def __init__(self) -> None:
        self.contractorRepo = DB(Contractor)
        self.maintReqRepo = DB(MaintenanceRequest)

    def createContractor(self, company: str=None, name: str=None, ssn: int=None, profession: str=None, phone: int=None, openinghours: str=None, email: str=None, address: Address=None):
        '''Creates contractor given user input'''
        new_contractor = Contractor(company=company, name=name, ssn=ssn, profession=profession, phone=phone, openinghours=openinghours, email=email, address=address)
        return self.contractorRepo.save(new_contractor)

    def find_requests_by_contractorID(self, contractor_id):
        '''Shows all requests assigned to contractor \n
        given contractor SSN'''
        maint_reqs = self.maintReqRepo.find({
            'where': {
                'contractor_id': contractor_id
            }
        })
        return maint_reqs

    
    
    def findContractor(self) -> list:
        '''Find contractor given contractor object'''
        return self.contractorRepo.find()

    def updateContractorInfo(self, id, data):
        '''updates contractor info'''
        data['_id'] = id
        return self.contractorRepo.update(data)

    def deleteContractor(self, id) -> list:
        '''Delets contractor given contractor ID'''
        return self.contractorRepo.delete(id)

    def findContractorByProfession(self, profession: str):
        '''Find contractor given proffession'''
        return self.contractorRepo.find({ 
            'where': {
                'profession': profession
            }
        })
    
    def findContractorByContractorId(self, contractorId: str):
        '''finds contractor given contractor SSN'''
        return self.contractorRepo.findOne({ 
            'where': {
                'ssn': contractorId
            }
        })
    
    def findContractorByName(self, name: str):
        '''finds contractor given contractor name'''
        return self.contractorRepo.find({ 
            'where': {
                'name': name
            }
        })

    def assignContractorToMaintenance(self, contractorSSN, maintReqId):
        '''Assaigns contractor to a maintanence request'''
        contractor = self.contractorRepo.findOne({
            'where': {
                'ssn': contractorSSN
            }
        })
        contractorId = contractor._id
        
        maint_req = self.maintReqRepo.findOne({
            'where': {
                '_id': maintReqId
            }
        })

        return self.maintReqRepo.update({
            '_id': maintReqId,
            'contractors': contractorId
        })
