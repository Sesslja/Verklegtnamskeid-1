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

