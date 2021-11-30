from Constants import EMPLOYEE_OPTIONS_DICT

from MainMenu import MainMenu

class EmployeesMenu :

    def __init__(self) :
        self.menu_options = EMPLOYEE_OPTIONS_DICT
    
    def print_options(self) :
        for key in  self.menu_options :
            print(f"{key} {self.menu_options[key]}")
        self.get_user_input()
    
    def get_user_input(self) :

        user_input = input("").upper() #User input A/B/X
        if user_input == "A" : #Create Employee
            print("Create employee")
            #a_menu = CreateEmployee()
            #a_menu.print_options()
            pass
        elif user_input == "B" : #Employees overview
            print("List employees overview")
            #b_menu = EmployeesOverview()
            #b_menu.print_options()
            pass
        elif user_input == "X" : #Return to previous page
            previous_menu = MainMenu()
            previous_menu.print_options()
        else :
            print('Invalid input')