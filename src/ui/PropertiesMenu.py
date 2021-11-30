from constants import PROPERTIES_OPTIONS_DICT

from MainMenu import MainMenu

class PropertiesMenu :

    def __init__(self) :
        self.menu_options = PROPERTIES_OPTIONS_DICT
    
    def print_options(self) :
        for key in  self.menu_options :
            print(f"{key} {self.menu_options[key]}")
        self.get_user_input()
    
    def get_user_input(self) :
        while True :
            user_input = input("").upper() #User input A/B/X
            if user_input == "A" : #Record property
                print('Record new property')
                #a_menu = RecordProperty()
                #a_menu.print_options()
                pass
            elif user_input == "B" : #Properties overview
                print("List properties overview")
                #b_menu = PropertiesOverview()
                #b_menu.print_options()
                pass
            elif user_input == "X" : #Return to previous page
                previous_menu = MainMenu()
                previous_menu.print_options()
            else :
                print('Invalid input')