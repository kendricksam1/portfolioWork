lower = 0
upper = 0


def caseCheck(string):
    for i in string:
        if (i.islower()):
            lower += 1
        else:
            upper += 1
    return upper, lower


print("The number of upper case letters is ", upper, " and the number of lower case letters is", lower)
