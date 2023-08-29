import sys,os
sys.path.append("/")
def clear(arg=""):
    if arg == "-h":
        print("clears the terminal\nclear")
    else:
        os.system("cls")