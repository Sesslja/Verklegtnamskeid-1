# Initar alla layerana
from model.RoomType import RoomType
from logic.PropertyLogic import PropertyAPI
from ui.MainMenu import MainMenu
from logic.MaintenanceRequestLogic import MaintenanceRequestAPI
from model.AddressType import Address


def main():
    menu = MainMenu()
    menu.print_options()

if __name__ == "__main__" :
    main()
    pass

#propApi = PropertyAPI()
#
#room = RoomType(11502, 'PR7991')
#room2 = RoomType(8902, 'PR7992')

#print(propApi.createProperty('husstadur', 'PP7990', ['klost','bad','eldhus'], [room, room2]))

# mReq = MaintenanceRequestAPI()
# 
# addr = Address('Iceland', 'Reykjavik', '101', 'Bankastræti 5')
# mReq.createMaintenanceRequest(addr, ['Borða mat', 'slá vegg', 'kaupa bíl'], 'ha', 'HIGH', 'now', '37a229db-6157-4bbe-b898-9d2abafb464d', 'VB00001')
# 
# mReq.createVerificationNumber()