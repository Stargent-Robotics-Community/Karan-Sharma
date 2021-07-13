import pyttsx3
import speech_recognition as sr

a=pyttsx3.init()
a.say('Hello Sir ! How can i help you')
a.runAndWait()
a.setProperty('rate',150)

try:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        print('Speak Now')
        audio=r.listen(source)

    text=r.recognize_google(audio)
    print(text)

    if text=='hello':
        a.say('Hello how can i help you?')
        a.runAndWait()
    elif text=='what is your name':
        a.say('My name is Jarvis and i am your creation')
        a.runAndWait()
    elif text=='good morning Jarvis':
        a.say('A very Good morning sir')
        a.runAndWait()
    elif text=="what else can you do":
        a.say('I am a first trial version created by Karan , and he is working on me right now, and i hope after some times he will make me fully working like Iron man')   
        a.runAndWait()

except:
    print("Run this Program again plz")