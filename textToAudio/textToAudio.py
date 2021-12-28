from gtts import gTTS
import os

#read text string from file - first option for input
# fileHandle = open("test.txt","r")
# textInput = fileHandle.read().replace("\n"," ")

#user input can be converted to audio - second option for input
textInput=input("Enter text to read")

#specify language for audio
language = 'en'

#generate output using gtts
output = gTTS(text=textInput,lang=language,slow=False)

output.save("output.mp3")
# fileHandle.close()

os.system("mpg123 output.mp3")