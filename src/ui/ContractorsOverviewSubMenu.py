from typing import Container
from ui.BaseMenu import BaseMenu
from logic.ContractorLogic import ContractorAPI

class ContractorsOverviewSubMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.contractorapi = ContractorAPI

        self.menu_title = "ContractorsMenu\nContractors Overview"

        self.menu_options = {
            "1": {
                "title": "Search our contractors",
                "access": "Manager",
                "function": "search_contractors_by_id"
            },
            "2": {
                "title": "Find new contractors",
                "access": "Manager",
                "function": "find_new_contractors"
            },                             
            "3": {
                "title": "Contractors overview",
                "access": "",
                "function": "all_contractors_overview"
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

    def find_new_contractors(self):
        print('serach me contractors')

    def all_contractors_overview(self):
        contractor_list = self.contractorapi.findContractor()
        
        for contractor in contractor_list:
            print (contractor)

    def search_contractor_by_id(self):
        contractor_id = None
        while contractor_id == None:
            try:
                contractor_id = int(input("Enter contractors ID: "))
            except ValueError:
                print("Please enter a valid ID")
        
        contractor_list = self.contractorapi.findContractorByContractorId()
        if len(contractor_list) == 0:
            print("Contractor not found!")
            contractor_id = None
        else:
            for contractor in contractor_list:
                print(contractor)

        