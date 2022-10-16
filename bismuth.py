
import sys,logging
import io
import modules

if len(sys.argv) >= 2:
    f = io.open(sys.argv[1], mode="r", encoding="utf-8")
else:
    f = io.open("test.b", mode="r", encoding="utf-8")
run = f.read()
chunks = run.split("\n@#\n",1)
assert len(chunks) >= 2 
if "$dev" in chunks[0]:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.ERROR)

lines = chunks[1].split("\n")

#define global table
gT = {}


def handle(line):
    global gT
    ret = line.split("|")
    print(ret)
    args =ret[1].split(",")
    f = ret[0]
    if f == "print":
        print(parseArg(args[0]))
    elif f == "✎":
        args =ret[1].split(",",1)
        gT[args[0]] = parseArg(args[1])
    elif f == "⎎":
        gT[args[0]] = modules.pkgs[args[0]]


    

def parseArg(arg):
    if arg[0] == "𝚫":
        return int(arg[1:len(arg)])
    elif arg[0] == "⎌":
        argc = arg[1:len(arg)].split(".")
        if len(argc) == 1:
            return gT[argc[0]]
        else:
           return gT[argc[0]][argc[1]] 
    elif arg[0] == "⎆":
        return handle(arg[1:len(arg)])
    else:
        return arg



for line in lines:
    handle(line)
