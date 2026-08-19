# This function is designed to open and read a file, then return the file data as one string
# On exception the function explains that it failed and re-runs itself
def GetFile(FileToRead: str) -> str:
    try:
        file = open(FileToRead)
        data = file.read()
        file.close()
        return data
    except FileExistsError as e:
        print("That file cannot be found, please try again\n", e)
        file.close()
        return GetFile(input("Please select another file to read.\n"))
    except Exception as e:
        print("There was an error.\n", e)
        exit(1)

# This function cleans any and all comments out of code to make it more workable
def CodeCleaner(code: str) -> str:
    CleanCode = ""
    for char in code:
        if( (char=="+") or (char=="-") or (char==">") or (char=="<") or (char=="[") or (char=="]") or (char==".") or (char==",") ):
            CleanCode += char
    return CleanCode

# This function returns a dict the index is the start and the value is the end of loops
def MakeLoopTable(code: str) -> list:
    OpenStack = []
    LookupTable = {}
    try:
        for index, char in enumerate(code):
            if(char=="["):
                OpenStack.append(index)
            elif(char=="]"):
                LookupTable[OpenStack.pop(0)] = index
    except IndexError:
        print("Could not parse file, unmatched [ found, exiting")
        exit(1)
    return LookupTable

# This function returns a list of tuples, the tuples are formated (INSTRUCTION, DATA), for most instructions +-<>,. the DATA is the count, but, for some [] it is the connected bracket using the loop table
def CountInstances(code: str, LoopTable: dict) -> list:
    count = 0
    CurrentInstruction = ""
    LoopStack = []
    FinalCode = []
    for index, data in enumerate(code):
        if(CurrentInstruction != data and count != 0):
            FinalCode.append( (CurrentInstruction, count) )
            count = 1
            CurrentInstruction = data
        
        if(data == "["):
            LoopStack.append(index)
            FinalCode.append( (data, LoopTable.get(index, -1)) )
            continue
        elif(data == "]"):
            FinalCode.append( (data, LoopStack.pop(0)) )
            continue
        
        if(CurrentInstruction == data or count==0):
            count+=1
            CurrentInstruction = data
        
    return FinalCode


# This nested function call is to auto-clean the data read from the file
code = CodeCleaner(GetFile(input("What file should be read?\n")))

LoopTable = MakeLoopTable(code)

FinalCode = CountInstances(code, LoopTable)

import pickle

with open(input("What file should be written to?\n"), 'wb') as OutFile:
    pickle.dump(FinalCode, OutFile)