from test import *

def saveTestToTextCpp(localitation, tests):
    file = open(localitation, "w")

    for one in tests:
        file.write(one.printCpp())

    file.close()