import datetime,sys
sys.path.append("/")
def time(arg=""):
    if arg == "-h":
        print("displays the curent time\ntime")
    else:
        time=datetime.datetime.now()
        time=time.strftime("%H:%M:%S")
        print(time)