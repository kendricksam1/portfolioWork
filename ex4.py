string =input("Enter string")
string = str(string)


def removeLastChar(string):
    if len(string) > 1:
        print(string[:-1])
    else:
        print(string)

removeLastChar(string)