import sys,os
sys.path.append("/")
def remove(arg):
    if arg == "-h":
        print("help msg")
    else:
        os.remove(arg)