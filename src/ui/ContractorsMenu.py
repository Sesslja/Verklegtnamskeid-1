from ui.BaseMenu import BaseMenu

class ContractorsMenu(BaseMenu):
    def __init__(self):
        super().__init__()

        self.menu_title = "Menu\nContractors Menu"

        self.menu_options = {
            "1": {
                "title": "Search our contractors",
                "access": "Manager",
                "function": "search_contractors"
            },
            "2": {
                "title": "Find new contractors",
                "access": "Manager",
                "function": "find_new_contractors"
            },                             
            "3": {
                "title": "Contractors overview",
                "access": "",
                "function": "contractorsOverview"
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

    def search_contractors():
        print('serach me contractors')


    def find_new_contractors():
        print('serach me contractors')


    def contractorsOverview():
        print('overview me contractors')