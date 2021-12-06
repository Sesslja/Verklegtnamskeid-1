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
                "title": "See all contractors",
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
            "6": {
                "title": "Delete contractor from our system",
                "access": "Manager",
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

        contractors_name = (input("Enter employee name: ")).upper()
        contractors_list = []
        for item in contractors_list:
            if contractors_name == contractors_name:
                print (item)
        self.waitForKeyPress()


    def find_contractor(self):
        try:
            contractor_list = self.contractorapi.findContractor()
            if len(contractor_list) == 0:
                print("No contractor to show :(")
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractor_list))
        except ValueError:
            print("No contractors found")
        self.waitForKeyPress()

    def delete_contractor(self):
        contractor_id = input("Enter contractors ID: ")
        if self.contractorapi.deleteContractor(contractor_id) == True:
            print("Contractor deleted")
        else: 
            print("Contractor not found")
        self.waitForKeyPress()

    def find_contractor_by_profession(self):
        contractors_profession = None
        while contractors_profession == None:
            try:
                contractors_profession = input("Enter profession: ")
            except ValueError:
                print("Please enter a valid profession")
        
        try:
            contractors_prof_list = self.contractorapi.findContractorByProfession()
            if len(contractors_prof_list) == 0:
                print("Profession not found!")
                contractors_profession = None
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractors_prof_list))
        except ValueError:
            print ("No contractors found")
        self.waitForKeyPress()

    def find_new_contractors(self): # Numer 2 á eftir að græja fallið
        print('serach me contractors')

    def all_contractors_overview(self):
        try:
            contractor_list = self.contractorapi.findContractor()
            if len(contractor_list) == 0:
                print("No contractors to show")
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractor_list))
                self.waitForKeyPress()
        except ValueError:
            print("No contractors found")
        self.waitForKeyPress()


    def search_contractor_by_id(self):
        contractor_id = None
        while contractor_id == None:
            try:
                contractor_id = int(input("Enter contractors ID: "))
            except ValueError:
                print("Please enter a valid ID")
        try:
            contractor_list = self.contractorapi.findContractorByContractorId()
            if len(contractor_list) == 0:
                print("Contractor not found!")
                contractor_id = None
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractor_list))
                self.waitForKeyPress()
        except ValueError:
            print("No contractors found")
        self.waitForKeyPress()

        