import sys,os
sys.path.append("/")
def rename(arg1,arg2):
    if arg1 == "-h":
        print("renames a file\nrename [target] [new name]")
    else:
        os.rename(arg1,arg2)