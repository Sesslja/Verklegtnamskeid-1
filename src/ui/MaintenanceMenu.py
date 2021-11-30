from MenuConstants import MAINTENANCE_REQUESTS_OPTIONS_DICT
from ui.BaseMenu import BaseMenu

class MaintenanceMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = MAINTENANCE_REQUESTS_OPTIONS_DICT