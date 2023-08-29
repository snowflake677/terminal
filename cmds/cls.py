import sys,os
sys.path.append("/")
def cls(arg=""):
    if arg == "-h":
        print("clears the terminal\ncls")
    else:
        os.system("cls")