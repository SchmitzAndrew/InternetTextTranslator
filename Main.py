#main.py
from Translator import *

print("Welcome to Internet Text Translator!")
print("1 - Shifting Text")
print("2 - wAckY teXt")
print("3 - Whiny Text")
print("4 - Text Spacer")
print("5 - Text Reducer")
print("6 - Text Repeater")

selection = int(input("Enter your desired translation here: "))
phrase = input("Enter the phrase you would like to translate: ")
if selection == 1:
    shiftText(phrase)
elif selection == 2:
    wackyText(phrase)
else:
    print("Not a valid selection.")

