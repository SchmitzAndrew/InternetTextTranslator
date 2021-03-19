import random

#text shifter

def printSpaces(num):
    s = " "
    return s * num


def shiftText(str):
    shifter_lines = int(input("How many lines: "))
    length = len(str)
    if length <= 2:
        print("Input needs to be longer")
    else:
        spaces = int(length / 2)
        linecount = 0
        for i in range(int(shifter_lines / spaces)):
            for s in range(spaces):
                if linecount >= shifter_lines:
                    break
                print(printSpaces(s % spaces) + str)
                linecount += 1
            for s in range(spaces):
                if linecount >= shifter_lines:
                    break
                print(printSpaces(spaces - s % spaces) + str)
                linecount += 1


#Wacky Switch
def wackySwitch(t):
    if random.random() < .3:
        t = t.swapcase()
    return t

def wackyText(input):  # cant use str
    phrase = list(input)
    wacky_phrase = [wackySwitch(t) for t in phrase]
    result = ''.join([str(x) for x in wacky_phrase])
    print(result)


#Text Spacer
def textSpacer(input):
    char_length = len(input) - input.count(' ')
    list_phrase = list(input)
    list_phrase = [t.strip(' ') for t in list_phrase]
    list_phrase = [t for t in list_phrase if t]  # removes empty strings
    line_length = 10
    chars_per_lines = 3
    global temp_list
    temp_list = []
    for i in range(line_length):
        temp_list.append(" ")


def textReducer(phrase):
    for i in range(len(phrase)):
        print(phrase[0:len(phrase)- i])


def textRepeater(phrase):
    lines = int(input("How many lines: "))
    if lines < 10:
        for i in range(lines):
            print(phrase)
    elif lines > 100: #change this
        print("Woah there kiddo.")
    else:
        f = open("output.txt", "w")
        for i in range(lines):
            f.write(phrase + "\n")

