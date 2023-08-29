import sys,shutil
sys.path.append("/")
def copy(arg1,arg2):
    if arg1 == "-h":
        print("copys a file\ncopy [source] [target]")
    else:
        shutil.copy2(arg1,arg2)