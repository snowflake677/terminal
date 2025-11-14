import sys
sys.path.append("/")
def toutch(arg):
    if arg == "-h":
        print("creats a file\ntoutch [file name]")
    else:
        open(arg,"w+").close
