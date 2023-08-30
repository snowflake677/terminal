import sys,requests,opt.homebrew.config as conf,cmds.text as t
sys.path.append("/")

def get(file):
    r = requests.get(conf.source+file, allow_redirects=True)
    open(sys.path[0]+"\\commands\\"+file, 'wb').write(r.content)
  
if terminal.args[0] == "-h":
    print("homebrew\nhomebrew [package name]")
else:
		t.print_with_color(conf.logo, color=Back.CYAN)
