from parseInput import *
from saveOutput import *

if __name__ == "__main__":
    
    all_tests = parseTestMd("TestReport.md")
   
    for one in all_tests:
        one.parseCode();
    
    saveTestToTextCpp("codigoCpp.txt",all_tests)
    #Test 31 le falta un ;