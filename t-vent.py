# this is going to be an attempt at a text adventure

import ConfigParser

config_parser = ConfigParser.RawConfigParser()
config_parser.read("text.ini")

section = "start"
blockx = 0
blocky = 0

def GetText():
    parsed = False
    blockx, blocky = 0, 0
    while parsed != True:
        direction = raw_input("N, S, E, or W?")
        if direction.upper() == "N":
            blockx = 0
            blocky = 1
            parsed = True
        elif direction.upper() == "S":
            blockx = 0
            blocky = -1
            parsed = True
        elif direction.upper() == "E":
            blockx = 1
            blocky = 0
            parsed = True
        elif direction.upper() == "W":
            blockx = -1
            blocky = 0
            parsed = True
        else:
            print("Try again...")
    return [blockx,blocky]

print(config_parser.get("start","0,0"))
while True:
    block = GetText()
    blockx += block[0]
    blocky += block[1]
    blockz = (str(blockx)+","+str(blocky))
    try:
        current_text = config_parser.get(section,blockz)
        print current_text
    except:
        blockx -= block[0]
        blocky -= block[1]
        blockz = (str(blockx)+","+str(blocky))
        current_text = config_parser.get(section,blockz)
        print ("Try again...")

 
