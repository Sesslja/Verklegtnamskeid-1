from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.ContractorLogic import ContractorAPI


class ContractorsEditSubMenu(BaseMenu):
    '''gives menu options to edit property'''
    def __init__(self):
        super().__init__()
        self.contractorsapi = ContractorAPI()
        self.contractorId = self.contractorIdInput()

        self.menu_title = f"Edit property nr. {self.contractorId}"


        self.menu_options = {
            "1": {
                "title": "Edit contractor",
                "access": "manager",
                "function": "createContractor"
            },
            "2": {
                "title": "Assign contractor to maintenance request",
                "access": "",
                "function": "assignEmployeeToProperty"
            },
            "X": {
                "title": "Return to previous page",
                "access": "",
                "special": "back"
            },
            "M": {
                "title": "Return to main menu",
                "special": "main"
            }
        }

    def contractorIdInput(self, retry: bool= False):
        self.clear()
        print('No contractor ID found please input a correct one') if retry else None
        contractorId = input("Please input the contractor's ID: ")


        try:
            foundProp = self.contractorsapi.findContractorByContractorId(contractorId)
        except RecordNotFoundError:
            return self.contractorIdInput(True)

        return foundProp.contractorId

    def assignContractorToMaintenance(self):

        contractor_ssn = input('Enter contractor SSN: ')

        try:
            updated = self.contractorsapi.assignContractorToMaintenance(employeeSSN=contractor_ssn, propertyId=self.contractorId)

            print(f'Successfully added contractor with SSN: {contractor_ssn}, to maintenance with ID: {self.contractorId}')

        except RecordNotFoundError:
            print('Employee not found')
        
        self.waitForKeyPress()