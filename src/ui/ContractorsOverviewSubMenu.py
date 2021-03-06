from typing import Container
from ui.BaseMenu import BaseMenu
from logic.ContractorLogic import ContractorAPI
from data.DBError import RecordNotFoundError

class ContractorsOverviewSubMenu(BaseMenu):
    '''Shows sub-menu to contractor options'''
    def __init__(self, logged_in_user=None):
        super().__init__(logged_in_user)
        self.contractorapi = ContractorAPI()

        self.menu_title = "ContractorsMenu\nContractors Overview"

        self.menu_options = {
            "1": {
                "title": "See all contractors",
                "access": "",
                "function": "all_contractors_overview"
            },                             
            "2": {
                "title": "Search contractors by id",
                "access": "",
                "function": "find_contractors_by_id"
            },  
            "3": {
                "title": "Find contractor by profession",
                "access": "",
                "function": "find_contractor_by_profession"
            },  
            "4": {
                "title": "Search contractor by name",
                "function": "find_contractor_by_name"
            },     
            "5": {
                "title": "Delete contractor from our system",
                "access": "manager",
                "function": "delete_contractor"
            },
            "6": {
                "title": "See contractors history",
                "access": "manager",
                "function": "see_contractor_history"
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
    
    
    def see_contractor_history(self):
        '''promts user to see all previos or current MRequests assigned to contractor'''
        contractor_ssn = input("Enter contractor SSN: ")
        try:    
            contractorID = self.contractorapi.findContractorByContractorId(contractor_ssn)
            requests = self.contractorapi.find_requests_by_contractorID(contractorID._id)
            
            show_keys = ['status', 'to_do', 'priority']
            print(self.createTable(show_keys, requests))
        except RecordNotFoundError:
            print('Nothing found ')
        self.waitForKeyPress()


    def find_contractors_by_id(self): #1
        '''Prompts user to find contractor by contractor ID'''
        contractor_id = None
        while contractor_id == None:
            try:
                contractor_id = input("Enter contractors ID: ")
            except ValueError:
                print("Please enter a valid ID")
                contractor_id = None
        try:
            contractor_list = self.contractorapi.findContractorByContractorId(contractor_id)
            if len(contractor_list) == 0:
                print("Contractor not found!")
                contractor_id = None
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractor_list))

        except RecordNotFoundError:
            print("No contractors found")
        self.waitForKeyPress()
    

    def find_contractor_by_name(self):
        '''Prompts user to find contractor by contractor name'''
        contractors_name = input("Enter name: ")   
        try:
            contractors_name_list = self.contractorapi.findContractorByName(contractors_name)
            if len(contractors_name_list) == 0:
                print("Contractor not found!")
                contractors_name = None
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractors_name_list))
        except RecordNotFoundError:
            print ("No contractors found")
        self.waitForKeyPress()


    def find_contractor_by_profession(self):
        '''option to search for contractor \ngiven contractor proffesion'''
        contractors_profession = None
        while contractors_profession == None:
            try:
                contractors_profession = input("Enter profession: ")
            except RecordNotFoundError:
                print("Please enter a valid profession")
        
        try:
            contractors_prof_list = self.contractorapi.findContractorByProfession(contractors_profession)
            if len(contractors_prof_list) == 0:
                print("Profession not found!")
                contractors_profession = None
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractors_prof_list))
        except RecordNotFoundError:
            print ("No contractors found")
        self.waitForKeyPress()


    def all_contractors_overview(self):
        '''Shows all contractors working for NAN'''
        try:
            contractor_list = self.contractorapi.findContractor()
            if len(contractor_list) == 0:
                print("No contractors to show")
            else:
                show_keys = ['name', 'email', 'ssn']
                print(self.createTable(show_keys, contractor_list))

        except ValueError:
            print("No contractors found")
        self.waitForKeyPress()


    def delete_contractor(self):
        '''Prompts user to delete contractor by contractor ID'''
        contractor_id = input("Enter contractors ID: ")
        if self.contractorapi.deleteContractor(contractor_id) == True:
            print("Contractor deleted")
        else: 
            print("Contractor not found")
        self.waitForKeyPress()
