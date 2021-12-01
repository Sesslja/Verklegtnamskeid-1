from ui.BaseMenu import BaseMenu

class ContractorsMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = {
            "A": {
                "title": "Search contractors",
                "access": "Manager",
                "function": self.searchContractors()
            },                    
            "B": {
                "title": "Contractors overview",
                "access": "",
                "function": self.contractorsOverview()
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

    def searchContractors(self):
        print('serach me contractors')

    def contractorsOverview(self):
        print('overview me contractors')