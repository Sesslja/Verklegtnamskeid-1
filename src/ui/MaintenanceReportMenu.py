from ui.BaseMenu import BaseMenu
from logic.MaintReportLogic import MaintReportAPI

class MaintenanceReportMenu(BaseMenu):
    '''Gives maintenace report optins'''
    def __init__(self):
        super().__init__()

        self.menu_title = "Maintenance Report Menu"
        self.maintreportAPI = MaintReportAPI

        self.menu_options = {
            
            "1": {
                "title": "Find all reports",
                "access": "",
                "function": "find_all_reports"
            },                        
            "2": {
                "title": "Find report by maintenance ID",
                "access": "",
                "function": "find_by_maintenance_id"
            },
            "3": {
                "title": "Find report by employee",
                "access": "",
                "function": "find_by_employee"
            },
            "4": {
                "title": "Find report by property",
                "access": "",
                "function": "find_by_property"
            },
            "5": {
                "title": "Find report by date",
                "access": "",
                "function": "find_by_date"
            }, 
            "X": {
                "title": "Return to previous page",
                "Access": "",
                "special": "back"
            },
            "M": {
                "title": "Return to main menu",
                "special": "main"
            }
        }

    def find_all_reports(self):
        report_list = self.maintreportAPI.findReport()
        show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
        print(self.createTable(show_keys, report_list))
        self.waitForKeyPress()

    def find_by_maintenance_id(self):
        '''Gives option to find maintenace report given the id of request'''
        maintenence_id = None
        while maintenence_id == None:
            maintenence_id = input("Enter maintenance ID: ")
            try:
                int(maintenence_id)
                report_list = self.maintreportAPI.findReportByMaintenanceId(maintenence_id)
                if len(report_list) == 0:
                    print ("No items to show")
                    report_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                    print(self.createTable(show_keys, report_list))
                    self.waitForKeyPress()
            except ValueError:
                print("Please enter a valid ID")
                maintenence_id = None


    def find_by_employee(self):
        '''Gives option to find maintenace report given the id of employee'''
        employee_id = None
        while employee_id == None:
            employee_id = input("Enter employee ID: ")
            try:
                int(employee_id)
                report_list = self.maintreportAPI.findReportByEmployee(employee_id)
                if len(report_list) == 0:
                    print ("No items to show")
                    report_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                    print(self.createTable(show_keys, report_list))
                    self.waitForKeyPress()
            except ValueError:
                print("Please enter a valid ID")
                employee_id = None

    def find_by_property(self):
        '''Gives option to find maintenace report given the id of property'''
        property_id = None
        while property_id == None:
            property_id = input("Enter property ID: ")
            try:
                int(property_id)
                report_list = self.maintreportAPI.findReportByProperty(property_id)
                if len(report_list) == 0:
                    print ("No items to show")
                    report_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                    print(self.createTable(show_keys, report_list))
                    self.waitForKeyPress()
            except ValueError:
                print("Please enter a valid ID")
                property_id = None

    def find_by_date(self):
        '''Gives option to find maintenace report given the date of report'''
        start_date = None
        end_date = None
        while start_date == None or end_date == None:
            start_date = input("Enter start date: ")
            end_date = input("Enter start date: ")
            if start_date == "" or  end_date == "":
                start_date == None
                end_date == None
            else:
                report_list = self.maintreportAPI.findReportByDate(start_date, end_date)
                if len(report_list) == 0:
                    print ("No items to show")
                    report_list == None
                    self.waitForKeyPress()
                else:
                    show_keys = ["propertyId",'maintenance', 'contractorId', 'salary', 'contractorsfee']
                    print(self.createTable(show_keys, report_list))
                    self.waitForKeyPress()