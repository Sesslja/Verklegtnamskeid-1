from Constants import MENU_OPTIONS_DICT

class MenuAPI:
    def __init__(self):
        self.menu_options = MENU_OPTIONS_DICT

    def print_menu(self):
        print ("[M] Menu")
        for key, value in MENU_OPTIONS_DICT.items():
            print(f"[{key}] {value:>6}")

    def get_user_input(self):
        user_input = input(": ").upper()

        if user_input == "P":
            pass
        elif user_input == "R":
            pass
        elif user_input == "C":
            pass
        elif user_input == "E":
            pass
        elif user_input == "M":
            pass
        else:
            print("Invalid Input ")

m = MenuAPI()

m.print_menu()
m.get_user_input()

    
        
        