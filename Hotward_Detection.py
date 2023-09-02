import os
import speech_recognition as sr
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 900
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            print(query)
            return query
        except Exception as e:
            return "Some Error Occurred, Please Speak Again Sir.."
while True:
    wake_up=takeCommand()
    if "wake up" in wake_up:
        os.startfile('F:\\PycharmProjects\\jarvis_ai\\main.py')
    else:
        print('nothing....')

        # I Love you






