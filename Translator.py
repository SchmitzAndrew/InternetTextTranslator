import random

def printspaces(num):
    s = " "
    return s * num

def shiftText(str):
    lines = int(input("How many lines: "))
    length = len(str)
    if length <= 2:
        print("Input needs to be longer")
    else:
        spaces = int(length / 2)
        linecount = 0
        for i in range(int(lines / spaces)):
            for s in range(spaces):
                if linecount >= lines:
                    break
                print(printspaces(s % spaces) + str)
                linecount += 1
            for s in range(spaces):
                if linecount >= lines:
                    break
                print(printspaces(spaces - s % spaces) + str)
                linecount += 1

def wackyText(str):
    phrase = str
    length = len(str)
    for c in range(length):
        if random.random() < .2:
            print("make each char upper")
        elif random.random() > .7:
            phrase.replace(phrase[c], phrase[c].lower())
    print(phrase)












