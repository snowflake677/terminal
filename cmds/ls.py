import sys,os
sys.path.append("/")
def ls(arg=""):
    if arg == "-h":
        print("lists the contains of a folder\nls <path>")
    else:
        print(os.listdir(arg))