from constants import CONTRACTORS_OPTIONS_DICT

from MainMenu import MainMenu

class ContractorsMenu :

    def __init__(self) :
        self.menu_options = CONTRACTORS_OPTIONS_DICT
    
    def print_options(self) :
        for key in  self.menu_options :
            print(f"{key} {self.menu_options[key]}")
        self.get_user_input()
    
    def get_user_input(self) :

        while True :

            user_input = input("").upper()

            if user_input == "A" : #Search contractor
                print("Search contractor")
                #a_menu = SearchContractor()
                #a_menu.get_user_input()
                pass
            elif user_input == "B" : #Contractors overview
                print("List contractors overview")
                #b_menu = ContractorsOverview()
                #b_menu.get_user_input()
                pass
            elif user_input == "X" : #Return to previous page
                previous_menu = MainMenu()
                previous_menu.print_options()
            else :
                print("Invalid input")