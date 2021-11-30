from ui.BaseMenu import BaseMenu

class ContractorsMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = {
            "A": {
                "title": "Search contractors",
                "access": "Manager",
                "Function": self.searchContractors
            },                    
            "B": {
                "title": "Contractors overview",
                "access": "",
                "aunction": self.contractorsOverview
            },                
            "X": {
                "title": "Return to previous page",
                "access": "",
                "special": "back"
                #Fara á fyrri síðu
            },
            "M": {
                "title": "Return to main menu",
                "special": "main"
            }
        }

    def searchContractors(self):
        print('serach me contractors')

    def contractorsOverview(self):
        print('overview me contractors')