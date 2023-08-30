import runpy,sys,os,cmds.homebrew.config as conf,cmds.text as t,time,cmds.cls as cls
from colorama import just_fix_windows_console
sys.path.append("/")
just_fix_windows_console()
try:
    os.mkdir("cmds\\homebrew\\applications")
except FileExistsError:
    print("")
def display_menu(options):
    cls.cls()
    t.print_with_color(conf.logo, color=t.Back.CYAN)
    t.print_with_color(conf.logo2, color=t.Back.BLUE)
    print("---------------------")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    print("---------------------")

def launch_homebrew(app_name):
    print(f"Launching {app_name}...")
    # Simulate loading and running the homebrew application
    time.sleep(2)
    print(f"{app_name} has been launched!")

def main():
    homebrew_apps = os.listdir("cmds\\homebrew\\applications")

    display_menu(homebrew_apps)
    choice = input("Select an option: ")

    if choice.lower() == "exit":
        print("Exiting...")
    else:
        try:
            choice = int(choice)
            if 1 <= choice <= len(homebrew_apps):
                selected_app = homebrew_apps[choice - 1]
                launch_homebrew(selected_app)
                runpy.run_path("commands\\homebrew")
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def hb(arg=""):
    if arg == "-h":
        print("homebrew\nhomebrew <arg>")
    else:
        main()
