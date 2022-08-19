import colorama
colorama.init(True)


def ShowBanner():
    print(colorama.Back.BLACK)
    print(colorama.Fore.LIGHTCYAN_EX)
    print("""

███████╗███████╗██╗  ██╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗██████╗ 
██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
███████╗███████╗███████║    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗  ██████╔╝
╚════██║╚════██║██╔══██║    ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  ██╔══██╗
███████║███████║██║  ██║    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
    """)
    print(colorama.Fore.LIGHTBLACK_EX + "_________________________________________________________________________________")
    print(colorama.Fore.WHITE)

def AddOptions(text, numero):
    print(f"{colorama.Fore.LIGHTRED_EX} [ {colorama.Fore.WHITE} {numero} {colorama.Fore.LIGHTRED_EX} ] {colorama.Fore.WHITE}{text}")

def ShowMenu(menu : list):
    for x in range(len(menu)):
        AddOptions(menu[x],x+1)
    return int(input(""))
