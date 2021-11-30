from ContractorsMenu import ContractorsMenu
from EmployeesMenu import EmployeesMenu
from MaintenanceMenu import MaintenanceMenu
from MaintenanceMenu import MaintenanceMenu
from PropertiesMenu import PropertiesMenu


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
        "function": PropertiesMenu.createProperty()
    },                   
    "B":  {
        "Title": "Properties overview",
        "Access": ""
    },                
    "X": {
        "Title": "Return to previous page",
        "Access": ""
        #Fara á fyrri síðu
    }
}

MAINTENANCE_REQUESTS_OPTIONS_DICT = {
    "A": {
        "Title": "Opened maintenance request",
        "Access": "Manager"
    },
    "B": {
        "Title": "Closed maintenance requests",
        "Acess": ""
    },        
    "C": {
        "Title": "Upcoming maintenance",
        "Access": ""
    },                
    "D": {
        "Title": "Create maintenance requests",  
        "Access": ""
    },       
    "E": {
        "Title": "Outstanding maintenance requests",
        "Access": "Manager"
    },    
    "X": {
        "Title": "Return to previous page",
        "Access": ""
        #Fara á fyrri síðu
}

CONTRACTORS_OPTIONS_DICT = {
    "A": {
        "Title": "Search contractors",
        "Access": "Manager"
    },                    
    "B": {
        "Title": "Contractors overview",
        "Access": ""
    },                
    "X": {
        "Title": "Return to previous page",
        "Access": ""
        #Fara á fyrri síðu
    }
}

EMPLOYEE_OPTIONS_DICT = {
    "A": {
        "Title": "Create employee"
    },                     
    "B": {
        "Title": "Employees overview"
    },                  
    "X": {
        "Title": "Return to previous page"
        #Fara á fyrri síðu
    }
}