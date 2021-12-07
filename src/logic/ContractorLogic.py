from model.AddressType import Address
from model.ContractorModel import Contractor
from data.database import DB

class ContractorAPI:
    def __init__(self) -> None:
        self.contractorRepo = DB(Contractor)

    def createContractor(self, company: str=None, name: str=None, ssn: int=None, profession: str=None, phone: int=None, openinghours: str=None, address: Address=None):
        new_contractor = Contractor(company=company, name=name, ssn=ssn, profession=profession, phone=phone, openinghours=openinghours, address=address)
        return self.contractorRepo.save(new_contractor)

    def findContractor(self) -> list:
        return self.contractorRepo.find()

    def deleteContractor(self, id) -> list:
        return self.contractorRepo.delete(id)

    def findContractorByProfession(self, profession: str):
        return self.contractorRepo.find({ 
            'where': {
                'profession': profession
            }
        })
    
    def findContractorByContractorId(self, contractorId: str):
        return self.contractorRepo.find({ 
            'where': {
                'ssn': contractorId
            }
        })