#Function to Add_Employee
 
def Add_Employ():
    ssn = input("Enter Employee social security number : ")
 
    #Checking if Employee is aldready in the system or not
    if(check_employee(Id) == True):
        print("Employee aready exists - Try Again\n")
        menu()
     
    else:
        name = input("Enter employee name: ")
        ssn = input("Enter emplpyee social security number: ")
        homephone = input("Enter employee homephone: ")
        cellphone = input("Enter employee cellphone: ")
        address = input("Enter eomployee address: ")
        email = input("Enter employee email: ")
        destination = input("Enter employee destination: ")
        employee = Employee(name, ssn, homephone, cellphone, address, email, destination)
        self.llapi.make_employee(employee)

 
 
        
        ## Vantar fall inní data 
        print("Employee Added Successfully ")
        menu()





#Models 
import string

class Employee:
    def __init__(self, name =string , ssn = string, homephone = string, cellphone = string , address = string, email =string , destination):
        self.name = name
        self.ssn = ssn
        self.homephone = homephone
        self.cellphone = cellphone
        self.address = address
        self.email = email
        self.destination = destination

    def __str__(self):
        return f"name: {self.name}, social security nr: {self.ssn}, homephone: {self.homephone}, cellphone: {self.cellphone}, address: {self.addess}, email: {self.email}, destination: {self.destination}"

class Property: 
    def __init__(self, address, renum = string, amenities = list, staff = list):
        self.address = address
        self.renum = renum
        self.amenitites = amenities
        self.staff = staff
    
    def __str__(self):
        return f"address: {self.address}, real estate number: {self.renum}, amenitites: {self.amenitites}, staff: {self.staff}"

class Contractor:
    def __init__(self, companyname = string, name = string, ssn =string, profession = string, phone = string, openinghrs = string, address = string):
        self.companyname = companyname
        self.name = name
        self.ssn = ssn
        self.profession = profession
        self.phone = phone
        self.openinghrs = openinghrs
        self.address = address

    def __str__(self):
    return f"company name: {self.companyname}, name: {self.name}, ssn: {self.ssn}, profession: {self.profession}, phone: {self.phone}, openinghrs: {self.openinghrs}, address: {self.address})"
    


#Menu = UI // Contractor 
class ContractorMenu:
    def __init__(self, llapi ):
        self.llapi = llapi
        self.options = "l - List of all listed contractors\nn - List of all unlisted contractors\nc - Create contractor\nr - return to menu"

    def contractor_command_input(self):
        print(self.options)
        while True:
            command = input("Enter your input: ")
            if command == "l":
                all_contractors = self.llcont.all_contractors()
                for contractors in all_contractors:
                    print(contractors)
            elif command == "n":
                new_contractors = self.llcont.new_contractors()
                for contractors in new_contractors:
                    print(contractors)
            elif command == "c":
                self.create_contractor()
            elif command == "r":
                return "r"
            else:
                print("Not invalid option - Try again!")
            print(self.options)

    def create_contractor(self):
        companyname = input("Enter the company name: ")
        name = input("Enter contractor's name: ")
        ssn = input("Enter contractor's social security number: ")
        profession = input("Enter contractor's profession: ")
        phone = input("Enter contractor's phone: ")
        openinghrs = input("Enter company's opening hours: ")
        address = input("Enter company's address: ")
        contractor = Contractor(companyname, name, ssn, profession, phone, openinghrs, address)
        self.llman.make_contractor(contractor)



#Menu = UI // Employee
class EmployeeMenu:
    def __init__(self, llapi ):
        self.llapi = llapi
        self.options = self.options = "l - List of all employees\nc - Create employee\nr - return to menu"

    def command_input(self):
        print(self.options)
        while True:
            command = input("Enter your input: ")
            if command == "l":
                all_employees = self.llempl.all_employees()
                for employees in all_employees:
                    print(employees)
            elif command == "c":
                self.create_employee()
            elif command == "r":
                return "r"
            else:
                print("Not invalid option - Try again!")*
            print(self.options)

    def create_employee(self):
        name = input("Enter employee name: ")
        ssn = input("Enter emplpyee social security number: ")
        homephone = input("Enter employee homephone: ")
        cellphone = input("Enter employee cellphone: ")
        address = input("Enter eomployee address: ")
        email = input("Enter employee email: ")
        destination = input("Enter employee destination: ")
        employee = Employee(name, ssn, homephone, cellphone, address, email, destination)
        self.llapi.make_employee(employee)



#Menu = UI // Property
class PropertyMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = "l - List of all properties\nc - Created property\nr - return to menu"

    def porp_command_input(self):
        print(self.options)
        while True:
            command = input("Enter your input: ")
            if command == "l":
                all_properties = self.llprop.all_properties()
                for properties in all_properties:
                    print(properties)
            elif command == "c":
                self.create_property()
            elif command == "r":
                return "r"
            else:
                print("Not invalid option - Try again!")
            print(self.options)

    def create_property(self):
        address = input("Enter the addreess for the propery: ")
        renum = input("Enter the real estate number for the property: ")
        amenities = list(input("Enter employee name: "))
        staff = list(input("Enter staff: "))
        properties = Property(address, renum, amenities, staff)
        self.llapi.make_properties(properties)


##llapi
# 
# def make_properties():

# def make_employee():

# def make_contractor():




