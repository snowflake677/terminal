import sys,requests
sys.path.append("/")
def wget(arg1,arg2):
    if arg1 == "-h":
        print("copys the source of a url to a file\nwget [url] [file]")
    else:
        r = requests.get(arg1, allow_redirects=True)
        open(arg2, 'wb').write(r.content)