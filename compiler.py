import json

def GetFile(FileToRead):
    try:
        file = open(FileToRead)
        data = file.read()
        return data
    except FileExistsError as e:
        print("That file cannot be found, please try again\n", e)
        return GetFile()
    except Exception as e:
        print("There was an error.\n", e)
        return GetFile()

code = GetFile(input("What file should be read?\n"))

