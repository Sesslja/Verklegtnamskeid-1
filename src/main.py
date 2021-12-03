# Initar alla layerana
from ui.MainMenu import MainMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from model.AddressType import Address

def main():
    menu = MainMenu()
    ret = False
    menu.print_options()

if __name__ == "__main__" :
    main()
    pass

# mReq = MaintenanceRequestAPI()
# 
# addr = Address('Iceland', 'Reykjavik', '101', 'Prikahús 2')
# mReq.createMaintenanceRequest(addr, ['Borða mat', 'kaupa tölvu', 'selja hjól'], 'ha', 'HIGH', 'now', '37a229db-6157-4bbe-b898-9d2abafb464d')

#print(mReq.createVerificationNumber())