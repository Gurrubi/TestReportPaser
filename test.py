class test:
    RSRVED_WORDS = [
        "Profile ",
        "Kmer ",
        "KmerFreq ",
        "char* ",
        "char ",
        "string ",
        "int "
        ]
    
    #CONSTRUCTOR
    
    def __init__(self, id, name, code, result, exception):
        self.__id = id
        self.__name = name
        self.__code = code
        self.__result = result
        self.__exception = exception

        self.__parseResult()

    #PRIVATE METHODS

    def __insert(self, line, toInsert, pos):
        return line[:pos] + toInsert + line[pos:]

    def __findVarAssingId(self, line, var):
        i = 0
        k = 0

        while i < (len(line) - len(var) + 1):
            is_in = False
            common_chars = ""
            
            while k < len(var):
                if line[i+k] == var[k]:
                    common_chars += var[k]
                k+=1


            if (i + len(var)) < len(line):
                next_c = line[i+len(var)]
                if common_chars == var and (next_c == '.' or next_c == '(' or next_c == ')' or next_c == ' ' or next_c == ',' or next_c == '+' or next_c == '='):
                    is_in = True
                    #print("---------------------")
                    #print(f"Linea {i}: {line}")
                    #print(f"La variable identificada en esta linea es: {common_chars}")
            elif common_chars == var:
                is_in = True
                #print("---------------------")
                #print(f"Linea {i}: {line}")
                #print(f"La variable identificada en esta linea es: {common_chars}")

            if is_in:
                id = "_" + str(self.__id)
                line = self.__insert(line, id, i+len(var))
                i += len(id) + len(var)
                #print(f"Nueva linea: {line}, i:{i+1}")
            
            k=0
            i+=1

        return line;

    def __parseResult(self):
        boolData = ["true", "false"]
        PROFILE = "unknown"

        if not self.__isDigit(self.__result) and self.__result != boolData[0] and self.__result != boolData[1]:
            if PROFILE in self.__result and len(self.__result) != len(PROFILE):
                prf = self.__result.split(' ')
                newstr = prf[0] + '\\n' + prf[1] + '\\n'
                prf = prf[2:-1]

                for i in range(0,len(prf)):
                    if i % 2 == 0:
                        newstr += prf[i] + ' '
                    else:
                        newstr += prf[i] + '\\n'
                
                self.__result = '"' + newstr + '"'

            elif len(self.__result) > 1 or self.__result == "_":
                self.__result = '"' + self.__result + '"'
            else:
                self.__result = "'" + self.__result + "'"

    
    def __isDigit(self, string):
        FIRST_CHAR = '-'
        FLOAT = '.'
        comma = False
        is_number = True
        i = 0

        is_number = string[i].isdigit() or string[i] == FIRST_CHAR
        i+=1


        while i < len(string) and is_number:
            if not comma:
                if string[i] == FLOAT:
                    comma = True
                else:
                    is_number = string[i].isdigit()
            else:
                is_number = string[i].isdigit()
            
            i+=1

        return is_number
    
    def __isVariable(self, c):
        return c != ' ' and c != ';' and c != ')' and c != '(' and c != '='
    
    def __getVarIn(self, line, word):
        k = line.find(word) + len(word)
        var = ""
        ended = False

        while not ended and k < len(line):
            if self.__isVariable(line[k]):
                var += line[k]
                k+=1
            else:
                ended = True
        
        return var


    #PUBLIC METHODS

    def parseCode (self):
        self.__code = (self.__code, self.__code.replace("inspectT","toString"))[self.__code.find("inspectT") != -1]
        self.__code = (self.__code, self.__code.replace("._size",".getSize()"))[self.__code.find("._size") != -1]
        self.__code = (self.__code, self.__code.replace("._profileId", ".getProfileId()"))[self.__code.find("._profileId") != -1]
        
        instructions = self.__code.split(';')
        instructions = (instructions, instructions[:-1])[instructions[len(instructions)-1] == '']
        instructions = [f"cout << \"Test {self.__id}: \""] + instructions

        vars = []
        for i in range(0,len(instructions)):
            line = instructions[i]

            for word in self.RSRVED_WORDS:
                if line.find(word) != -1:
                    var = self.__getVarIn(line, word)
                    vars.append(var)

            for var in vars:
                line = self.__findVarAssingId(line,var)

            instructions[i] = line

        if not self.__exception:
            last = len(instructions)-1
            #outputMessage = f"cout << \"EXPECTED: \" << {self.__result} << \" | RESULT: \" << {instructions[last]} << ({self.__result} == {instructions[last]} ? \" PASSED\" : \" FAILED\") << endl;"

            if instructions[last].find('}') == -1:
                instructions[last] = f"cout << ({self.__result} == {instructions[last]} ? \" PASSED\" : \" FAILED\") << endl;"
            else:
                pos = instructions[last].find('}') + 1
                instructions[last] = instructions[last][:pos] + f"cout << ({self.__result} == {instructions[last][pos:]} ? \" PASSED\" : \" FAILED\") << endl;"

        #else:
            #instructions[len(instructions)-1] += ';'

        self.__code = ';'.join(instructions)
        #print(instructions)
        #print(self.__code)

    def print(self):
        return str(self.__id) + " " + self.__name + " " + self.__code + " " + self.__result + " " + str(self.__exception)

    def printCode(self):
        return str(self.__id) + " | " + self.__code
    
    def printCpp(self):
        cpp = ""

        cpp += "\t// Test: " + str(self.__id) + " SHOULD GIVE: " + self.__result + "\n"
        comment = ("", "//")[self.__exception]
        cpp += "\t" + comment + self.__code + "\n\n"

        return cpp