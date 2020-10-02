import pyttsx3

engine = pyttsx3.init()
print("!!!To exit the program enter exit!!!")
while(True):
    text = input('Enter text:')
    if(text in ('exit','Exit')):
        break
    else:
        engine.say(text)
        engine.runAndWait()
