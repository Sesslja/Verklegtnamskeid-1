from MenuConstants import PROPERTIES_OPTIONS_DICT
from ui.BaseMenu import BaseMenu

class PropertiesMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = PROPERTIES_OPTIONS_DICT