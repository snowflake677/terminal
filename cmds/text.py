from colorama import just_fix_windows_console, Fore, Back, Style

# essential for Windows environment
just_fix_windows_console()
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

def print_with_color(s, color=Fore.BLUE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)
bootimg="""
  ________________  __  ________   _____    __ 
 /_  __/ ____/ __ \/  |/  /  _/ | / /   |  / / 
  / / / __/ / /_/ / /|_/ // //  |/ / /| | / /  
 / / / /___/ _, _/ /  / // // /|  / ___ |/ /___
/_/ /_____/_/ |_/_/  /_/___/_/ |_/_/  |_/_____/
                                               

"""
