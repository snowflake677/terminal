import sys,requests,cmds.homebrewconfig as conf,cmds.text as t
sys.path.append("/")

def get(file):
    r = requests.get(conf.source+file, allow_redirects=True)
    open(sys.path[0]+"\\commands\\"+file, 'wb').write(r.content)
def hb(arg):
    if arg == "-h":
        print("homebrew\nhomebrew [package name]")
    else:
	t.print_with_color(conf.logo, color=Back.CYAN)
	get(arg)
