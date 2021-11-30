from MenuConstants import CONTRACTORS_OPTIONS_DICT
from ui.BaseMenu import BaseMenu

class ContractorsMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = CONTRACTORS_OPTIONS_DICT