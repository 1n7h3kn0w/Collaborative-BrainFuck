# This is just the class for holding the tape, instruction pointer, and methods for handling moving the pointer and altering values while handling wraping to 8-bit automatically

class BrainFuck():
    
    def __init__(self, TAPE_SIZE: int):
        self.tape = [0 for _ in range(0, TAPE_SIZE)]
        self.pointer = 0
    
    def MoveLeft(self):
        if(self.pointer == 0):
            self.pointer = (len(self.tape) - 1)
            return 0
        self.pointer -= 1
        return 0
    
    def MoveRight(self):
        if(self.pointer == (len(self.tape) - 1)):
            self.pointer = 0
            return 0
        self.pointer += 1
        return 0
    
    def add(self):
        if(self.tape[self.pointer] == 255):
            self.tape[self.pointer] = 0
            return 0
        self.tape[self.pointer] += 1
        return 0
    
    def sub(self):
        if(self.tape[self.pointer] == 0):
            self.tape[self.pointer] == 255
            return 0
        self.tape[self.pointer] -= 1
        return 0
    
    def out(self):
        print(chr(self.tape[self.pointer]), end="")
        return 0
    
    def inp(self):
        uin = input()
        if(len(uin) == 0):
            self.tape[self.pointer] = 0
        elif(len(uin) > 1):
            self.tape[self.pointer] = ord(uin[0])
        elif(len(uin) == 1):
            self.tape[self.pointer] = ord(uin)
        return 0


def RunInterpreter(machine: BrainFuck, SourceCode: str):
    
    def CodeCleaner(SourceCode: str):
        ValidCommands = ['+', '-', '<', '>', '[', ']', '.', ',']
        CleanCode = ""
        for char in SourceCode:
            if(char in ValidCommands):
                CleanCode += char
        return CleanCode
    
    code = CodeCleaner(SourceCode)
    CodeLen = len(code)
    CodePointer = 0
    
    # TODO finish interpreter code
    
    return 0