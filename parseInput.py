from test import *

STARTING_LINE_FILE = 4
ID_FINAL_TEST = 80

def parseTestMd(localitation):
    tests = []
    file = open(localitation)

    lines = [line.strip() for line in file if line.strip() != '']

    lines = lines[STARTING_LINE_FILE:]

    id = 0
    aux = []
    i = 0

    for line in lines:
        if id <= ID_FINAL_TEST:
            if i % 2 == 0:
                aux = [x for x in line.split('|') if x != '']
                
                for i in range(0,3):
                    aux[i] = aux[i].replace(' ', '')
                
                id = int(aux[0])

                aux[3] = aux[3].replace('```','')

            else:
                cleaned = line[8:-1]
                exception = False

                if cleaned.find("exception") == -1:
                    cleaned = cleaned.split('```')[1]

                    if cleaned[0] == '\"':
                        cleaned = cleaned.replace('\"','')

                else:
                    exception = True
                    cleaned = cleaned.split("exception")[1][1:]
                
                tests.append(test(int(aux[0]),aux[1],aux[3],cleaned,exception))
 
        i+=1

    file.close()

    return tests