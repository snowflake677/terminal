import sys,requests,os
sys.path.append("/")
def get(file):
    os.mkdir(sys.path[0]+"\\opt\\"+file)
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file+"/"+file+".py", allow_redirects=True)
    open(sys.path[0]+"\\opt\\"+file+"\\"+file+".py", 'wb').write(r.content)
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file+"/config.py", allow_redirects=True)
    open(sys.path[0]+"\\opt\\"+file+"\\config.py", 'wb').write(r.content)
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file+"/cmd", allow_redirects=True)
    open(sys.path[0]+"\\commands\\"+file, 'wb').write(r.content)
def tap(arg):
    if arg == "-h":
        print("gets packages one at a time\ntap [package name]")
    else:
        get(arg)