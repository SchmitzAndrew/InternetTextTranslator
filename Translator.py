import random


def printSpaces(num):
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
                print(printSpaces(s % spaces) + str)
                linecount += 1
            for s in range(spaces):
                if linecount >= lines:
                    break
                print(printSpaces(spaces - s % spaces) + str)
                linecount += 1


def wackySwitch(t):
    if random.random() < .3:
        t = t.swapcase()
    return t

def wackyText(input):  # cant use str
    phrase = list(input)
    wacky_phrase = [wackySwitch(t) for t in phrase]
    result = ''.join([str(x) for x in wacky_phrase])
    print(result)
