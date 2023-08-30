import sys,requests,os
sys.path.append("/")
def get(file):
    try:
        os.mkdir("cmds\\"+file)
    except FileExistsError:
        print("package alredy installed\nupdating instad")
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file+"/"+file+".py", allow_redirects=True)
    open("cmds\\"+file+"\\"+file+".py", 'wb').write(r.content)
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file+"/config.py", allow_redirects=True)
    open("cmds\\"+file+"\\config.py", 'wb').write(r.content)
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file+"/cmd", allow_redirects=True)
    open("commands\\"+file, 'wb').write(r.content)
    r = requests.get("https://raw.githubusercontent.com/snowflake677/terminal/packages/"+file+"/__init__.py", allow_redirects=True)
    open("cmds\\"+file+"\\__init__.py", 'wb').write(r.content)
def tap(arg):
    if arg == "-h":
        print("gets packages one at a time\ntap [package name]")
    else:
        get(arg)