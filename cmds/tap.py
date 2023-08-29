import sys,requests,terminal
sys.path.append("/")
def get(file):
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file, allow_redirects=True)
    open(sys.path[0]+"\\commands\\"+file, 'wb').write(r.content)
def tap(arg):
    if arg == "-h":
        print("gets packages one at a time\ntap [package name]")
    else:
        get(arg)