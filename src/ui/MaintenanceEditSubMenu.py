from ui.BaseMenu import BaseMenu
from data.DBError import RecordNotFoundError
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from logic.MaintReportLogic import MaintReportAPI
#from MaintenanceReportMenu import MaintReportAPI
#from MaintenanceRequestMenu import MaintenanceRequestAPI
try:
    from rich.prompt import Confirm, Prompt, FloatPrompt
    from rich.text import text
except ModuleNotFoundError:
    pass

class MaintenanceEditSubMenu(BaseMenu):
    ''' Gives menu options to edit reports'''
    def __init__(self):
        super().__init__(logged_in_user=None):
        self.maintreportAPI = MaintReportAPI()
        self.maintrequestAPI = MaintenanceRequestAPI()
        self.maintenanceId = self.maintenanceIdInput()
        if self.maintenanceId is 'q':
            self.failed = True

        self.menu.title = f'Edit report nr. {self.maintenanceId}'

        self.menu_options = {
            "1": {
                "title": "Edit maintenance report",
                "access": "manager",
                "function": "editReport"
            },
            "2": {
                "title": "Add new room",
                "access": "manager",
                "function": "addRoom"
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

    def maintenanceIdInput(self, retry: bool= False):
        ''' Is called when the user opens the menu, ask for the maintenance ID'''
        self.clear()
        print('No maintenance ID found please input a correct one') if retry else None
        maintId = input('Please input ID of property ([Q] to Quit): ')
        if maintId.lower() == "q":
            return "q"

        try:
            foundMaint = self.maintrequestAPI.findMRequestByVerificationId(maintId)
        except RecordNotFoundError:
            return self.mantenanceIdInput(True)

        return foundMaint.maintenanceId

    def 
    


    # def openClosedMReport(self):
    #         ''' Update report '''
    #         found_report = self.maintenanceRequestAPI.findMRequestByVerificationId()