# Initar alla layerana
from ui.MainMenu import MainMenu

def main():
    menu = MainMenu()
    ret = False
    while ret is False:
        ret = menu.print_options()