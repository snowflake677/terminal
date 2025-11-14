import runpy,sys,os,cmds.homebrew.config as conf,cmds.text as t,cmds.cls as cls,time
from colorama import just_fix_windows_console
sys.path.append("/")
just_fix_windows_console()
try:
    os.mkdir("cmds\\homebrew\\applications")
except FileExistsError:
    pass
def installer():
    import requests
    cls.cls()
    t.print_with_color(conf.logo, color=t.Back.CYAN)
    t.print_with_color(conf.logo3, color=t.Back.BLUE)
    def get(file):
        try:
            os.mkdir("cmds\\"+file)
        except FileExistsError:
            print("package alredy installed\nupdating instad")
        r = requests.get(conf.mirror+file+"/"+file+".py", allow_redirects=True)
        open("cmds\\"+file+"\\"+file+".py", 'wb').write(r.content)
        r = requests.get(conf.mirror+file+"/config.py", allow_redirects=True)
        open("cmds\\"+file+"\\config.py", 'wb').write(r.content)
        r = requests.get(conf.mirror+file+"/cmd", allow_redirects=True)
        open("commands\\"+file, 'wb').write(r.content)
        r = requests.get(conf.mirror+file+"/__init__.py", allow_redirects=True)
        open("cmds\\"+file+"\\__init__.py", 'wb').write(r.content)
    choice = input("Select an option: ")

def launcher():
    homebrew_apps = os.listdir("cmds\\homebrew\\applications")
    cls.cls()
    t.print_with_color(conf.logo, color=t.Back.CYAN)
    t.print_with_color(conf.logo2, color=t.Back.BLUE)
    print("---------------------")
    for idx, option in enumerate(homebrew_apps, start=1):
        print(f"{idx}. {option}\nexit")
    print("---------------------")
    choice = input("Select an option: ")
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

def launch_homebrew(app_name):
    print(f"Launching {app_name}...")
    # Simulate loading and running the homebrew application
    time.sleep(2)
    print(f"{app_name} has been launched!")

def main():
    cls.cls()
    t.print_with_color(conf.logo, color=t.Back.CYAN)    
    option = input("Select an option: ")
    if option.lower() == "exit":
        print("Exiting...")
    elif option.lower() == "launcher":
        launcher()
    elif option.lower() == "installer":
        installer()
    else:
        print("Invalid choice. Please select a valid option.\nExiting...")

def hb(arg=""):
    if arg == "-h":
        print("starts the homebrew app\nhomebrew")
    else:
        main()
