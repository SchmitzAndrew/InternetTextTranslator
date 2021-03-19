#main.py
from Translator import *

print("Welcome to Internet Text Translator!")
print("1 - Shifting Text")
print("2 - wAckY teXt")
print("3 - Text Reducer")
print("4 - Text Repeater")

selection = int(input("Enter your desired translation here: "))
phrase = input("Enter the phrase you would like to translate: ")

if selection == 1:
    shiftText(phrase)
elif selection == 2:
    wackyText(phrase)
elif selection ==3:
    textReducer(phrase)
elif selection == 4:
    textRepeater(phrase)
else:
    print("Not a valid selection.")

