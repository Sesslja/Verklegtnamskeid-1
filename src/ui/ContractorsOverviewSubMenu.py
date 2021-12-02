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
            "4": {
                "title": "Find contractor by profession",
                "access": "",
                "function": "find_contractor_by_profession"
            },  
            "5": {
                "title": "Search contractor by name",
                "function": "search_contractor_by_name"
            },     
            "4": {
                "title": "Delete contractor from our system",
                "access": "manager",
                "function": "delete_contractor"
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


    def search_contractor_by_name(self):
        contractors = self.contractorapi.findContractor()
        list_contractor_name = []
        list_contractor_ids = []
        for contractor in contractors:
            list_contractor_name.append(contractor.name)
            list_contractor_ids.append(contractor._id)

        contractor_name = self.autocomplete_input(list_contractor_name)
        contractor_id = list_contractor_ids[list_contractor_name.index(contractor_name)]

        found_contractor = self.contractorapi.findOneContractor(contractor_id)
        print(found_contractor)

    def find_contractor(self):
        pass

    def delete_contractor(self):
        contractor_id = None
        self.contractorapi.deleteContractor(contractor_id)

    def find_contractor_by_profession(self):
        contractors_profession = None
        while contractors_profession == None:
            try:
                contractors_profession = input("Enter profession: ")
            except ValueError:
                print("Please enter a valid profession")
        
        contractors_prof_list = self.contractorapi.findContractorByProfession()
        if len(contractors_prof_list) == 0:
            print("Profession not found!")
            contractors_profession = None
        else:
            for contractor in contractors_prof_list:
                print(contractor)

    def find_new_contractors(self): # Numer 2 á eftir að græja fallið
        print('serach me contractors')

    def all_contractors_overview(self):
        contractor_list = self.contractorapi.findContractor()
        if len(contractor_list) == 0:
            print("No contractors to show")
        else:
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

        