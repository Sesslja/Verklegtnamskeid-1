from data.DBError import RecordNotFoundError
from model.MaintenanceRequestModel import MaintenanceRequest
from model.AddressType import Address
from model.ContractorModel import Contractor
from data.database import DB

class ContractorAPI:
    def __init__(self) -> None:
        self.contractorRepo = DB(Contractor)
        self.maintReqRepo = DB(MaintenanceRequest)

    def createContractor(self, company: str=None, name: str=None, ssn: int=None, profession: str=None, phone: int=None, openinghours: str=None, email: str=None, address: Address=None):
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
        return self.contractorRepo.find()

    def updateContractorInfo(self, id, data):
        data['_id'] = id
        return self.contractorRepo.update(data)

    def deleteContractor(self, id) -> list:
        return self.contractorRepo.delete(id)

    def findContractorByProfession(self, profession: str):
        return self.contractorRepo.find({ 
            'where': {
                'profession': profession
            }
        })
    
    def findContractorByContractorId(self, contractorId: str):
        return self.contractorRepo.findOne({ 
            'where': {
                'ssn': contractorId
            }
        })
    
    def findContractorByName(self, name: str):
        return self.contractorRepo.find({ 
            'where': {
                'name': name
            }
        })

    def assignContractorToMaintenance(self, contractorSSN, maintReqId):
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
