import sys
sys.path.append("/")
def toutch(arg):
    if arg == "-h":
        print("creats a file\ntouch [file name]")
    else:
        open(arg,"w+").close
