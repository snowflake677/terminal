import sys
sys.path.append("/")
def cat(arg):
    if arg == "-h":
        print("concatenate\ncat [file]")
    else:
        with open(arg, 'r') as fin:
            print(fin.read())