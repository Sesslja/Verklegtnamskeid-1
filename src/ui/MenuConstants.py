from ui.ContractorsMenu import ContractorsMenu
from ui.EmployeesMenu import EmployeesMenu
from ui.MaintenanceMenu import MaintenanceMenu
from ui.PropertiesMenu import PropertiesMenu

MENU_OPTIONS_DICT = { 
    "P": {
        "Title": "Properties",
        "Access": "",
        "Class": PropertiesMenu
    },  
    "R": {
        "Title": "Maintenance Requests",
        "Access": "",
        "Class": MaintenanceMenu
    },     
    "C": {
        "Title": "Contractors",
        "Access": "",
        "Class": ContractorsMenu
    },
    "E": {
        "Title": "Employees",
        "Access": "Manager",
        "Class": EmployeesMenu
    },                  
    "X": {
        "Title": "Return to previous page",
        "special": "back"
        #Fara á fyrri síðu
    },
    "M": {
        "title": "Return to main menu",
        "special": "main"
    }
}

PROPERTIES_OPTIONS_DICT = {
    "A": {
        "Title": "Record property",
        "Access": "Manager",
        "Function": PropertiesMenu.createProperty()
    },                   
    "B":  {
        "Title": "Properties overview",
        "Access": "",
        "Function": PropertiesMenu.propertiesOverview()
    },                
    "X": {
        "Title": "Return to previous page",
        "Access": ""
        #Fara á fyrri síðu
    },
    "M": {
        "title": "Return to main menu",
        "special": "main"
    }
}

MAINTENANCE_REQUESTS_OPTIONS_DICT = {
    "A": {
        "Title": "Opened maintenance request",
        "Access": "Manager",
        "Function": MaintenanceMenu.openedMRequest()
    },
    "B": {
        "Title": "Closed maintenance requests",
        "Acess": "",
        "Function": MaintenanceMenu.closedMRequest()
    },        
    "C": {
        "Title": "Upcoming maintenance",
        "Access": "",
        "Function": MaintenanceMenu.upcomingMaintenance()
    },                
    "D": {
        "Title": "Create maintenance requests",  
        "Access": "",
        "Function": MaintenanceMenu.createMRequest
    },       
    "E": {
        "Title": "Outstanding maintenance requests",
        "Access": "Manager",
        "Function": MaintenanceMenu.outstandingMRequest
    },    
    "X": {
        "Title": "Return to previous page",
        "Access": ""
    },
    "M": {
        "title": "Return to main menu",
        "special": "main"
    }
}

CONTRACTORS_OPTIONS_DICT = {
    "A": {
        "Title": "Search contractors",
        "Access": "Manager",
        "Function": ContractorsMenu.searchContractors()
    },                    
    "B": {
        "Title": "Contractors overview",
        "Access": "",
        "Function": ContractorsMenu.contractorsOverview()
    },                
    "X": {
        "Title": "Return to previous page",
        "Access": ""
        #Fara á fyrri síðu
    },
    "M": {
        "title": "Return to main menu",
        "special": "main"
    }
}

EMPLOYEE_OPTIONS_DICT = {
    "A": {
        "Title": "Create employee",
        "Functino": EmployeesMenu.createEmployee()
    },                     
    "B": {
        "Title": "Employees overview",
        "Function": EmployeesMenu.employeesOverview()
    },                  
    "X": {
        "Title": "Return to previous page"
        #Fara á fyrri síðu
    },
    "M": {
        "title": "Return to main menu",
        "special": "main"
    }
}