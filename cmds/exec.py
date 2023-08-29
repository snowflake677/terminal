import sys,runpy
sys.path.append("/")
def exec(arg):
    if arg == "-h":
        print("executes a file\nexec [file]")
    else:
        runpy.run_path(arg)