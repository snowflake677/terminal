import sys,os
sys.path.append("/")
def mkdir(arg):
    if arg == "-h":
        print("creats a directory\nmkdir [folder name]")
    else:
        os.mkdir(arg)