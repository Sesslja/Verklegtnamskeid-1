from Constants import MAINTENANCE_REQUESTS_OPTIONS_DICT

from MainMenu import MainMenu

class MaintenanceMenu :

    def __init__(self) :
        self.menu_options = MAINTENANCE_REQUESTS_OPTIONS_DICT
    
    def print_options(self) :
        for key in  self.menu_options :
            print(f"{key} {self.menu_options[key]}")
        self.get_user_input()
    
    def get_user_input(self) :

        user_input = input("").upper() #User input A/B/C/D/E/X
        if user_input == "A" : #Opened maintenance request
            print("List opened maintenance request")
            #a_menu = OpenedMaintenanceRequestClass()
            #a_menu.print_options()
            pass
        elif user_input == "B" : #Closed maintennance request
            print("List closed maintennance request")
            #b_menu = ClosedMaintennanceRequestClass()
            #b_menu.print_options()
            pass
        elif user_input == "C" : #Upcoming maintenance
            print("List upcoming maintenance")
            #c_menu = UpcomingMaintenanceClass()
            #c_menu.print_options()
            pass
        elif user_input == "D" : #Create maintenance request
            print("Create maintenance request")
            #d_menu = CreateMaintennanceRequestClass
            #d_menu.print_options()
            pass
        elif user_input == "E" : #Outstanding maintennance request
            print("List outstanding maintennance request")
            #e_menu = OutstandingMaintennanceRequestClass
            #e_menu.print_options()
            pass
        elif user_input == "X" : #Return to previous page
            previous_menu = MainMenu()
            previous_menu.print_options()
        else :
            print('Invalid input')