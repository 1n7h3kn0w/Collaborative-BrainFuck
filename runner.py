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
        self.tape[self.pointer] += 1
        self.tape[self.pointer] &= 0xff
        return 0
    
    def sub(self):
        self.tape[self.pointer] -= 1
        self.tape[self.pointer] &= 0xff
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
    
    # TODO fix loop code
    
    # This section defines all required variables for loops
    LoopStack = []
    LoopDepth = 0
    LoopSkip = False
    
    while(CodePointer < CodeLen):
        char = code[CodePointer]
        match char:
            case "+":
                machine.add()
                CodePointer += 1
            case "-":
                machine.sub()
                CodePointer += 1
            case ">":
                machine.MoveLeft()
                CodePointer += 1
            case "<":
                machine.MoveRight()
                CodePointer += 1
            case ",":
                machine.inp()
                CodePointer += 1
            case ".":
                machine.out()
                CodePointer += 1
            case "[":
                if(machine.tape[machine.pointer] == 0):
                    LoopSkip = True
                    LoopDepth = 1
                    while(LoopSkip):
                        CodePointer +=1
                        char = code[CodePointer]
                        match char:
                            case "[":
                                LoopDepth += 1
                            case "]":
                                LoopDepth -= 1
                        if(LoopDepth == 0):
                            LoopSkip = False
                if(machine.tape[machine.pointer] != 0):
                    LoopStack.append(CodePointer)
                    CodePointer += 1
            case "]":
                if(LoopStack != []):
                    CodePointer = LoopStack.pop()
                else:
                    CodePointer += 1
    
    return 0

# TODO remove this test for "prod"
# This is just test code for my interpreter

interpreter = BrainFuck(100)

BFcode = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

RunInterpreter(interpreter, BFcode)