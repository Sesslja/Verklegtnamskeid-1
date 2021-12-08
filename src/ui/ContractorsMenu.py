from model.AddressType import Address
from ui.BaseMenu import BaseMenu
from logic.ContractorLogic import ContractorAPI
from ui.ContractorsOverviewSubMenu import ContractorsOverviewSubMenu 
from ui.ContractorsEditSubMenu import ContractorsEditSubMenu

class ContractorsMenu(BaseMenu):
    '''Shows main contractor menu'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.contractorapi = ContractorAPI()

        self.menu_title = "Menu\nContractors Menu"

        self.menu_options = {
            "1": {
                "title": "Create contractors",
                "access": "manager",
                "function": "createContractor"
            },                            
            "2": {
                "title": "Contractors overview",
                "class": ContractorsOverviewSubMenu
            },
            "3": {
                "title": "Edit Contractor",
                "access": "manager",
                "class": ContractorsEditSubMenu
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

    def createContractor(self):
        '''Býður notenda upp á að búa til verktaka'''
        company = input("Enter company's name: ")
        name = input("Enter contractors name: ")
        ssn = input("Enter Social-Security number: ")
        profession = input("Enter profession: ")
        phone = input("Enter phone number: ")
        openinghours = input("Enter opening hours: ")
        email = input('Email: ')
        country = input('Country: ')
        city = input('City: ')
        zip_code = input('Zip code: ')
        address = Address(country=country, city=city, zip=zip_code)

        self.contractorapi.createContractor(company, name, ssn, profession, phone, openinghours, email, address)

        print(f"{name} added as a contractor!")

        self.waitForKeyPress()