from MenuConstants import EMPLOYEE_OPTIONS_DICT
from ui.BaseMenu import BaseMenu

class EmployeesMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        self.menu_options = EMPLOYEE_OPTIONS_DICT