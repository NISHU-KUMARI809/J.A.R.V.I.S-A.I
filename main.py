import os
import webbrowser
import speech_recognition as sr
import win32com.client
import openai
import datetime
import pywhatkit as pwt

def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    while 1:
        speaker.Speak(text)
        break
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 800
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred, Please Speak Again Sir.."

#--------------------------Main Function------------------
if __name__ == '__main__':
    # print("pycharm")
    say("Hi, I am Jarvis")
    while True:
        print("Listening....")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
            # todo: Add a feature to play a specific song

            if "open music" in query:
                musicPath = "F:\PycharmProjects\jarvis_ai\downfall-21371.mp3"
                os.system(f"open{musicPath}")
            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is{strfTime}")
                break
            if "open Excel".lower() in query.lower():
                os.system(f"start excel")
                break
            if "open Word".lower() in query.lower():
                os.system(f"start winword")
            if "open PowerPoint".lower() in query.lower():
                os.system(f"start powerpnt")
                break

            if "open camera" in query:
                os.system(f"start microsoft.windows.camera:")
                break

            if "open Notepad" in query:
                os.system(f"start notepad")
                break

            if "play video" in query:
                say("Which video you want to play Sir")
                text = takeCommand()
                pwt.playonyt(text)

            if "search for me Jarvis" in query:
                say("What do you want me to search Sir")
                text = takeCommand()
                pwt.search(text)
                break

            #This is Jarvis, 



















    
