import os #to intreact with operating system
import requests #  to send HTTP requests, handle responses, and perform other related tasks in their Python programs.
from bs4 import BeautifulSoup #easily to scrap information from web pages ,
from win10toast import ToastNotifier #to show pop up Desktop notifications (Alert Messages)
import pywhatkit # It offers functionalities such as playing YouTube videos, searching for information on Wikipedia,
# converting text to handwriting, and sending WhatsApp messages programmatically.
from googletrans import Translator
import time
from time import sleep
import webbrowser
import pyautogui # used for automating gui interactions
import speech_recognition as sr
import win32com.client #access to many Windows-specific features and functionalities.
import openai #provides access to natural language processing (NLP) models such as
# GPT (Generative Pre-trained Transformer) through its API and Python library.
import datetime
from playsound import playsound
import pywhatkit as pwt # performing various functions like sending whtspp mesg ,
# performing google search , converting text to handwriting and more
import gtts   #to convert text to speech and save it aas an audio file or play it directly
from gtts import gTTS
from tkinter import * # provide fast and easy way to create gui application
import tkinter as tk
import googletrans
import pyttsx3 # used for text-to-speech conversion
import pypdf # to read ,write and to manipulate pdf file in python code

def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    while 1:
        speaker.Speak(text)
        break
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 900
        r.pause_threshold = 0.9
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred, Please Speak Again Sir.."


def Reader():
    say("Tell me the name of the Book!")
    name=takeCommand()
    if "India" in name:
        os.startfile('F:\\PycharmProjects\\jarvis_ai\\history.pdf')
        book=open('F:\\PycharmProjects\\jarvis_ai\\history.pdf','rb')
        pdfreader=pypdf.PdfReader(book)
        # pages=pdfreader.getNumPages()
        pages=len(pdfreader.pages)
        say(f"Number of pages in this book are {pages}")
        say("From Which page I Have to start Reading ?")
        numPage=input("Enter the page number:")
        numpage1=int(numPage)

        page=pdfreader.pages[numpage1]
        text=page.extract_text()
        say("In which Language you wana listen sir?")
        lang=takeCommand()
        if "Hindi" in lang:
            trans1=Translator()
            textHin=trans1.translate(text,"hi")
            textm=textHin.text
            speech=gTTS(text=textm)
            try:
                speech.save("book.mp3")
                playsound("book.mp3")
            except:
                playsound("book.mp3")
        else:
            say(text)
    if "Europe" in name:
        os.startfile("C:/Users/HP/Downloads/NCERT-Class-10-History.pdf")
        book = open("C:/Users/HP/Downloads/NCERT-Class-10-History.pdf", "rb")
        pdfreader = pypdf.PdfReader(book)
        pages = len(pdfreader.pages)
        say(f"Number of pages in this book are {pages}")
        say("From Which page I Have to start Reading ?")
        numPage=input("Enter the page number:")
        numpage1=int(numPage)

        page=pdfreader.pages[numpage1]
        text=page.extract_text()
        say("In which Language, I have to read?")
        lang = takeCommand()
        if "hindi" in lang:
            trans1 = Translator()
            textHin = trans1.translate(text, "hi")
            textm = textHin.text
            speech = gTTS(text=textm)
            try:
                speech.save("book.mp3")
                playsound("book.mp3")
            except:
                playsound("book.mp3")
        else:
            say(text)
def temperature():
    root=tk.Tk()
    root.geometry("350x350")
    root.title("Temperature")
    root.configure(bg="black")
    y = tk.StringVar()
    e1 = tk.Entry(root, textvariable=y)
    l1 = tk.Label(root, text="Enter city:")
    l1.place(x=10, y=5)
    e1.place(x=10, y=50, height=35, width=180)

    def check():
        city = y.get()
        search = "Weather in {}".format(city)
        url = f"https://www.google.com/search?&q={search}"
        req = requests.get(url)
        sor = BeautifulSoup(req.text, "html.parser")
        temp = sor.find("div", class_="BNeawe").text
        l2 = tk.Label(root, text="", bg="black", fg="yellow")
        l2.place(x=10, y=140)
        g = f"Temperature in {city} is", temp
        l2.configure(text=g)
        say("Temperature of" + city+"is"+temp)

    b=tk.Button(root,text="Check",command=check)
    b.place(x=10,y=100)

    root.mainloop()



def ChooseLang():
    root = Tk()
    root.title("Languages")
    root.configure(bg="black")
    lang = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque',
            'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa',
            'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish',
            'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian',
            'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian',
            'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish',
            'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)',
            'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy',
            'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali',
            'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian',
            'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak',
            'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu',
            'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa',
            'yiddish', 'yoruba', 'zulu']
    root.geometry("400x400")
    options = StringVar(root)
    options.set("Choose")
    dropdown = OptionMenu(root, options, *lang).pack(pady=50)

    def close():
        root.destroy()

    buttons = Button(root, command=close, text='Press Okay to Confirm!').pack(pady=100)
    root.mainloop()

    your_value = options.get()
    kys = googletrans.LANGUAGES
    for my_key, my_value in kys.items():
        if my_value == your_value:
            l = my_key
    trans2 = trans1.translate(text, dest=l)
    Text = trans2.text
    convertAudio = gtts.gTTS(trans2.text, lang=l)
    convertAudio.save("audiofile.mp3")
    playsound("audiofile.mp3")
    say("Language Translated Sir, Your Translated Text appeear on your Screen Sir")
    print(Text)

def whatsapp():
    say("Tell me the number sir")
    num = int(input("Enter number:"))
    sleep(50)
    pnum = f"+91{num}"
    say("What message you want me to deliver sir")
    typemsg = takeCommand()
    say("Sure sir, I will send but first Tell me the timing sir...")
    say("On which hour should I send the message sir")

    hour = int(input("Enter Hour"))
    say("Tell me the minutes sir")
    mins = int(input("Enter Minutes"))
    pwt.sendwhatmsg(pnum, typemsg, hour, mins)
    say("Message send successfully")
#--------------------------Main Function------------------
if __name__ == '__main__':

    # print("pycharm")
    say("Hi, I am jarvis, your A I assistant , how can I assist you sir !")
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
            # break
            # todo: Add a feature to play a specific song

        if "play song" in query:
            say("sir what song you want")
            song= takeCommand()
            webbrowser.open(f"https://open.spotify.com/search/{song}")
            sleep(13)
            pyautogui.click()
            say('playing'+ song)
            # break

        if "send WhatsApp message for me" in query:
            whatsapp()
            # break
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is{strfTime}")
            # break
        if "open Excel".lower() in query.lower():
            os.system(f"start excel")
            # break
        if "open Word".lower() in query.lower():
            os.system(f"start winword")

        if "open PowerPoint".lower() in query.lower():
            os.system(f"start powerpnt")
            # break

        if "open Browser".lower() in query.lower():
            say("Sure Sir, first tell me the website")
            initial1="www."
            initial2=takeCommand()
            initial3=".com"
            web=initial1+initial2+initial3
            # web=input("Enter website sir: ")
            os.system(f"start chrome {web}")
            # break

        if "open camera" in query:
            os.system(f"start microsoft.windows.camera:")
            sleep(7)
            pyautogui.click()

        if "open Notepad" in query:
            os.system(f"start notepad")
            # break

        if "play video" in query:
            say("Which video you want to play Sir")
            text = takeCommand()
            pwt.playonyt(text)

        if "search for me Jarvis" in query:
            say("What do you want me to search Sir")
            text = takeCommand()
            pwt.search(text)
            # break

        if "could you please take a screenshot" in query:
            say("Sir,please tell me the name for the screenshot file")
            name=takeCommand()
            say("Please sir hold a second.I am taking a screenshot")
            time.sleep(7)
            img=pyautogui.screenshot()
            img.save(f'{name}.png')
            say("Done sir.")
            break
        if "set alarm" in query:
            say("Enter the time:")
            time=input("Enter the time:")
            while True:
                Time_Ac= datetime.datetime.now()
                now=Time_Ac.strftime("%H:%M:%S")
                if now==time:
                    say("Time To Wake up Sir! ")
                    playsound('downfall-21371.mp3')
                    usercomand=input("Enter stop to stop the alarm")
                    if usercomand=="stop":
                        exit(0)
                        # byee
                elif now>time:
                    break

        if "translate for me" in query:
            say("Tell me the line Sir")
            text=takeCommand()
            trans1= Translator()
            say("Now Choose the language sir..")
            ChooseLang()

        if "remember that" in query:
            rememberMsg=query.replace("remember that","")
            rememberMsg=rememberMsg.replace("jarvis","")
            say("You Tell me to Remind you that:"+rememberMsg)
            remember=open("data.txt","w")
            remember.write(rememberMsg)
            remember.close()
        if "what do you remember" in query:
            remember=open("data.txt",'r')
            say("You Tell me that"+remember.read())
            toast=ToastNotifier()
            speak=pyttsx3.init()
            speak.say("You Tell me that"+rememberMsg)
            toast.show_toast("Alert!,You Tell me that"+rememberMsg,duration=3)
            say("you rember me that"+remember.read())
            time.sleep(7)

        if "Google search" in query:
            import wikipedia as googleScrap
            query=query.replace("jarvis","")
            query=query.replace("Google search","")
            query=query.replace("google","")
            say("This is what I found on the web!")
            pywhatkit.search(query)
            try:
                result=googleScrap.summary(query,3)
                say(result)
            except:
                say("No Speakable data available!")

        if "temperature" in query:
            temperature()
        if "read book" in query:
            Reader()

        if "you need a break" in query:
            say("Ok sir,You"
                " can call me Anytime !")
            say("Just say wake up kit kat!")
            break


        if "stop" in query:
            say("ok sir thank you")
            exit()
















    
