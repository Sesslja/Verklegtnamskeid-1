from rich import prompt
from model.MaintenanceRequestModel import MaintenanceRequest
from data.DBError import RecordNotFoundError
from ui.BaseMenu import BaseMenu
from logic.ContractorLogic import ContractorAPI
from model.AddressType import Address
try:
    from rich.prompt import Prompt
except:
    None

class ContractorsEditSubMenu(BaseMenu):
    '''gives menu options to edit property'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.contractorsapi = ContractorAPI()
        self.contractorSSN = self.contractorSSNInput()
        if self.contractorSSN is 'q':
            self.failed = True

        self.menu_title = f"Edit Contractor\n SSN: {self.contractorSSN}"


        self.menu_options = {
            "1": {
                "title": "Assign contractor to maintenance request",
                "access": "",
                "function": "assignEmployeeToProperty"
            },
            "2": {
                "title": "Edit contractor name",
                "access": "",
                "function": "edit_contractor_name"
            },
            "3": {
                "title": "Edit contractor SSN",
                "access": "",
                "function": "edit_contractor_ssn"
            },
            "4": {
                "title": "Edit contractor company",
                "access": "",
                "function": "edit_contractor_company"
            },
            "5": {
                "title": "Edit contractor profession",
                "access": "",
                "function": "edit_contractor_profession"
            },
            "6": {
                "title": "Edit contractor phone",
                "access": "",
                "function": "edit_contractor_phone"
            },
            "7": {
                "title": "Edit contractor email",
                "access": "",
                "function": "edit_contractor_email"
            },
            "8": {
                "title": "Edit contractor opening hours",
                "access": "",
                "function": "edit_contractor_openinghours"
            },
            "9": {
                "title": "Edit contractor address",
                "access": "",
                "function": "edit_contractor_address"
            },
            "D": {
                "title": "Delete contractor",
                "access": "",
                "function": "deleteContractor"
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

    def contractorSSNInput(self, retry: bool = False):
        self.clear()
        print('No contractor found please input a correct SSN') if retry else None
        contractorSSN_input = input("Please input the contractor's SSN ([Q] to Quit): ")
        if contractorSSN_input.lower() == 'q':
            return 'q'
        try:
            found_contractor = self.contractorsapi.findContractorByContractorId(contractorSSN_input)
        except RecordNotFoundError:
            return self.contractorSSNInput(True)

        return found_contractor.ssn

    def edit_contractor_address(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        comfirm = input("Do you want to change contractor address?\n[1] Yes\n[2] No\n: ")
        if comfirm == "1":
            address = found_contractor.Address
            old_country = address["country"]
            old_city = address["city"]
            old_zip = address["zip"]
            new_country = input(f"Old country: {old_country}\nNew country:  ")
            new_city = input(f"Old city: {old_city}\nNew city:  ")
            new_zip = input(f"Old zip: {old_zip}\nNew zip:  ")
            print("Address successfully changed.")
        else:
            print("Okey, lets go back")
        self.waitForKeyPress()


    def edit_contractor_openinghours(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        old_openinghours = found_contractor.openinghours
        new_openinghours = input(f"Change opening hours\n Old opening hours: {old_openinghours}\nNew opening hours:  ")

        updated_user = self.contractorsapi.updateContractorInfo(found_contractor._id, {
            'openinghours': new_openinghours
        })
        print("Opening hours successfully changed.")
        self.waitForKeyPress()


    def edit_contractor_email(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        old_email = found_contractor.email
        new_email = input(f"Change email\n Old email: {old_email}\nNew email:  ")

        updated_user = self.contractorsapi.updateContractorInfo(found_contractor._id, {
            'email': new_email
        })
        print("Email successfully changed.")
        self.waitForKeyPress()


    def edit_contractor_phone(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        old_phone = found_contractor.phone
        new_phone = input(f"Change phone\n Old phone: {old_phone}\nNew phone:  ")

        updated_user = self.contractorsapi.updateContractorInfo(found_contractor._id, {
            'phone': new_phone
        })
        print("Phone successfully changed.")
        self.waitForKeyPress()


    def edit_contractor_profession(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        old_profession = found_contractor.profession
        new_profession = input(f"Change profession\n Old profession: {old_profession}\nNew profession:  ")

        updated_user = self.contractorsapi.updateContractorInfo(found_contractor._id, {
            'profession': new_profession
        })
        print("Professioin successfully changed.")
        self.waitForKeyPress()


    def edit_contractor_name(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        old_name = found_contractor.name
        new_name = input(f"Change name\n Old name: {old_name}\nNew name:  ")

        updated_user = self.contractorsapi.updateContractorInfo(found_contractor._id, {
            'name': new_name
        })
        print("Name successfully changed.")
        self.waitForKeyPress()


    def edit_contractor_ssn(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        old_ssn = found_contractor.ssn
        new_ssn = input(f"Change SSN\n Old SSN: {old_ssn}\nNew SSN:  ")

        updated_user = self.contractorsapi.updateContractorInfo(found_contractor._id, {
            'ssn': new_ssn
        })
        print("SSN successfully changed.")
        self.waitForKeyPress()
        
    def edit_contractor_company(self):
        found_contractor = self.contractorsapi.findContractorByContractorId(self.contractorSSN)
        old_company = found_contractor.company
        new_company = input(f"Change company\n Old company: {old_company}\nNew company:  ")

        updated_user = self.contractorsapi.updateContractorInfo(found_contractor._id, {
            'company': new_company
        })
        print("Company successfully changed.")
        self.waitForKeyPress()


    def assignContractorToMaintenance(self):

        contractor_ssn = input('Enter contractor SSN: ')

        try:
            updated = self.contractorsapi.assignContractorToProperty(contractorSSN=contractor_ssn, aintenanceRequest_id=self.contractorSSN)

            print(f'Successfully added contractor with SSN: {contractor_ssn}, to maintenance with ID: {self.contractorSSN}')

        except RecordNotFoundError:
            print('Employee not found')
        
        self.waitForKeyPress()

    def deleteContractor(self):
        confirm = Prompt.ask('Are you sure you want to delete this contractor?\n[1] Yes! \n Press any other key to Cancel\n')
        #confirm = Prompt.choices('Are you sure?' 'Yes', 'No')
        if confirm == '1':
            try: 
                contractorID= self.contractorsapi.findContractorByContractorId(self.contractorSSN)
                self.contractorsapi.deleteContractorId(contractorID._id)
                print('Contractor deleted')
            except RecordNotFoundError:
                print('Contractor not found')
        else:
            print('No changes made')
        self.waitForKeyPress()
