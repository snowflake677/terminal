import os,runpy,sys
os.system('title terminal')
os.system('@mode con cols=150 lines=60')
dir=sys.path[0]
perms="#"
os.system(":terminal")
on=True
while on:
    command = input(dir+perms)
    
    if command.startswith("exit"):
        if args[0] =="-h":
            print("quits the terminal\nexit")
        else:
            on=False
    
    elif command.startswith("cd"):
        parts = command.split()
        command = parts[0]
        args = parts[1:]
        if args[0] =="..":
            dir=os.path.split(dir)[0]
        elif args[0] =="-h":
            print("changes the curent directory\ncd [path]")
        else:
            dir=dir+"\\"+args[0]
    else:
        if command != "":
            try:
                if " " in command:
                    parts = command.split()
                    command = parts[0]
                    args = parts[1:]
                runpy.run_path("commands\\"+command)
            except:
                print("no command found try help")