from io import FileIO
import sys

from sqlalchemy import null

def printErrorExit(err):
    print("Error: " + err)
    sys.exit(84)

class Map:
    def __init__(self, sX, sY):
        self.x = sX
        self.y = sY

class Vacuum:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
    
    def letfRotate(self):
        if (self.dir == 'N'):
            self.dir = 'W'
        elif (self.dir == 'W'):
            self.dir = 'S'
        elif (self.dir == 'S'):
            self.dir = 'E'
        elif (self.dir == 'E'):
            self.dir = 'N'
    
    def rightRotate(self):
        if (self.dir == 'N'):
            self.dir = 'E'
        elif (self.dir == 'E'):
            self.dir = 'S'
        elif (self.dir == 'S'):
            self.dir = 'W'
        elif (self.dir == 'W'):
            self.dir = 'N'
    
    def advance(self, map: Map):
        if (self.dir == 'N'):
            if (self.y + 1 < map.y):
                self.y += 1
            else:
                printErrorExit("Out of map")
        elif (self.dir == 'E'):
            if (self.x + 1 < map.x):
                self.x += 1
            else:
                printErrorExit("Out of map")
        elif (self.dir == 'S'):
            if (self.y - 1 > 0):
                self.y -= 1
            else:
                printErrorExit("Out of map")
        elif (self.dir == 'W'):
            if (self.x - 1 > 0):
                self.x -= 1
            else:
                printErrorExit("Out of map")

def getMap(file:FileIO) -> Map:
    arr = file.readline().split()
    try:
        map = Map(int(arr[0]), int(arr[1]))
    except:
        printErrorExit("Invalid map size")
    return map

def getVacuum(file:FileIO, map:Map) -> Vacuum:
    arr = file.readline().split()
    if (len(arr) != 3):
        printErrorExit("Not enough arguments for vacuum")
    if (arr[2] != 'N' and arr[2] != 'E' and arr[2] != 'S' and arr[2] != 'W'):
        printErrorExit("Invalid direction")
    try:
        vacuum = Vacuum(int(arr[0]), int(arr[1]), arr[2])
    except:
        printErrorExit("Invalid vacuum position")
    if (vacuum.x < 0 or vacuum.x >= map.x):
        printErrorExit("Invalid vacuum position X")
    if (vacuum.y < 0 or vacuum.y >= map.y):
        printErrorExit("Invalid vacuum position Y")
    return vacuum

def exec(file:FileIO, vacuum: Vacuum, map: Map):
    buff = str(file.readline().strip())
    for i in buff:
        if (i != 'G' and i != 'A' and i != 'D'):
            printErrorExit("Invalid instruction")
        if (i == 'G'):
            vacuum.letfRotate()
        elif (i == 'A'):
            vacuum.advance(map)
        elif (i == 'D'):
            vacuum.rightRotate()

def main():
    f = null
    if (sys.argv.__len__() >= 2):
        try:
            f = open(sys.argv[1], 'r')
        except:
            print("Error: can't open file in argument, opening default file.")
            f = open("test.txt", "r")
    else:
            f = open("test.txt", "r")
    map = getMap(f)
    vacuum = getVacuum(f, map)
    exec(f, vacuum, map)
    print(vacuum.x, vacuum.y, vacuum.dir)
    f.close()

if __name__ == "__main__":
    main()