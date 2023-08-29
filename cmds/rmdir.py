import sys,os
sys.path.append("/")
def rmdir(arg):
    if arg == "-h":
        print("removes a directory\nrmdir [target]")
    else:
        os.rmdir(arg)