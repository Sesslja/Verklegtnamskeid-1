from model.AddressType import Address
from ui.BaseMenu import BaseMenu
from logic.ContractorLogic import ContractorAPI
from ui.ContractorsOverviewSubMenu import ContractorsOverviewSubMenu 


class ContractorsMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.contractorapi = ContractorAPI

        self.menu_title = "Menu\nContractors Menu"

        self.menu_options = {
            "1": {
                "title": "Create contractors",
                "access": "Manager",
                "function": "createcontractor"
            },                            
            "2": {
                "title": "Contractors overview",
                "class": ContractorsOverviewSubMenu
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
        company = input("Enter company's name: ")
        name = input("Enter contractors name: ")
        ssn = input("Enter Social-Security number: ")
        profession = input("Enter profession: ")
        phone = input("Enter phone number: ")
        openinghours = input("Enter opening hours: ")
        country = input('Country: ')
        city = input('City: ')
        zip_code = input('Zip code: ')
        address = Address(country=country, city=city, zip=zip_code)

        self.contractorapi.createContractor(company, name, ssn, profession, phone, openinghours, address)

        print("Contractor added!")