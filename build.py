import os

embedStr = "local EmbeddedModules = {\n"
files = os.listdir("modules")

def readfile(path):
    file = open(path,"r")
    str = file.read()
    file.close()
    return str

def addModuleFile(path):
    global embedStr

    moduleName = os.path.splitext(os.path.basename(path))[0]
    moduleSource = readfile(path)

    embedStr = embedStr + '["' + moduleName + '"] = function()\n' + moduleSource + '\nend,\n'

for filename in files:
    addModuleFile("modules/" + filename)

embedStr = embedStr + "}"
embedStr = embedStr + "\n" + readfile("main.lua")

file = open("out.lua","w")
file.write(embedStr)
file.close()