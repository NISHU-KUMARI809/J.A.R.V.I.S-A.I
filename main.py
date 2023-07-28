import os
import time
from time import sleep
import webbrowser
from playsound import playsound
import pyautogui
import speech_recognition as sr
import win32com.client
import openai
import datetime
from playsound import playsound
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
        if 'hi Jarvis' in query:
            say("Hello sir ! how are you ?")
            s = takeCommand()
            say("Nice to hear that sir!!")
            listenn = takeCommand()
            say("I am fine sir!!")
            listen1 = takeCommand()
            say("Thank you sir ! its my pleasure you ask about me!")
            break
            # todo: Add a feature to play a specific song

        if "play song" in query:
            say("sir what song you want")
            song= takeCommand()
            webbrowser.open(f"https://open.spotify.com/search/{song}")
            sleep(7)
            pyautogui.click()
            say('playing'+ song)
            break
        if "send WhatsApp message for me" in query:
            say("Tell me the number sir")
            num =takeCommand()
            pnum = f"+91{num}"
            say("What message you want me to deliver sir")
            typemsg = takeCommand()
            say("Sure sir, I will send but first Tell me the timing sir...")
            say("On which hour should I send the message sir")

            hour = int(input("Enter Hour"))
            say("Tell me the minutes sir")
            mins = int(input("Enter Minutes"))
            pwt.sendwhatmsg(pnum, typemsg,hour,mins)
            say("Message send successfully")
            break
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

        if "open Browser".lower() in query.lower():
            say("Sure Sir, first tell me the website")
            initial1="www."
            initial2=takeCommand()
            initial3=".com"
            web=initial1+initial2+initial3
            # web=input("Enter website sir: ")
            os.system(f"start chrome {web}")
            break

        if "open camera" in query:
            os.system(f"start microsoft.windows.camera:")
            sleep(7)
            pyautogui.click()
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
        if "could you please take a screenshot" in query:
            say("Sir,please tell me the name for the screenshot file")
            name=takeCommand()
            say("Please sir hold a second.I am taking a screenshot")
            time.sleep(7)
            img=pyautogui.screenshot()
            img.save(f'{name}.png')
            say("Done sir.")
            break
        # if "alarm" in query:
        #     say("Enter the time:")
        #     time=input(":Enter the time:")
        #     while True:


        if "stop" in query:
            exit()




















    
