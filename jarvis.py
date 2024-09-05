import pyttsx3
import speech_recognition as sr
import pyaudio
import wave
import array as arr  
import datetime
import os
import random
from requests import get
import wikipedia
import pyautogui
import time
import requests
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import instaloader
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def record_audio(duration=5, fs=44100):
    chunk = 1024  # Record in chunks of 1024 samples
    format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    rate = fs
    filename = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename

def takecommand():
    try:
        filename = record_audio()
        
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio = r.record(source)
        
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        query = query.lower()
        return query

    except Exception as e:
        if isinstance(e, sr.UnknownValueError):
            speak("Could not understand audio, please try again.")
            return takecommand()
        else:
            speak("Error occurred, please try again.")
            return takecommand()

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good morning, it's {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon, it's {tt}")
    else:
        speak(f"Good evening, it's {tt}")
    speak("I am your virtual assistant. Please tell me how may I help you")

def pdf_reader():
    book = open('C:\\Users\\prash\\OneDrive\\Desktop\\Mini\\final documentation.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    speak(f"Total number of pages in this book is {pages}")
    speak("Sir, please enter the page number I have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.pages[pg]
    text = page.extract_text()
    speak(text)

def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c2dd7d36b0c84565b5339a416bd2d9e3"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for i, ar in enumerate(articles):
        head.append(ar["title"])
        if i < len(day):
            speak(f"Today's {day[i]} news is: {head[i]}")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('22r21a67f5@mlrit.ac.in', 'Prashanth@67F5')
    server.sendmail('22r21a67f5@mlrit.ac.in', to, content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        if "open excel" in query:
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(npath)

        elif "open flowchart" in query:
            fpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Flowgorithm.lnk"
            os.startfile(fpath)

        elif "open powerpoint" in query:
            ppath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(ppath)

        elif "open my powerpoint" in query:
            mppath = "C:\\Users\\kpv25\\Downloads\\computer tech (1).pptx"
            os.startfile(mppath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play music" in query:
            mpath = "C:\\Users\\kpv25\\Music\\Glass_Animals_-_Heat_Waves_valvabox.com.mp3"
            os.startfile(mpath)

        elif "my ip address" in query:
           
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif "window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("Please wait, fetching the latest news")
            news()

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 12:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "thank you" in query:
            speak("It's my pleasure. Do you have any other work?")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "internet speed" in query:
            webbrowser.open("https://fiber.google.com/speedtest/")

        elif "open weather browser" in query:
            webbrowser.open("https://www.accuweather.com")

        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send a message to umar" in query:
            kit.sendwhatmsg("+919866865268", "this is testing protocol", 15, 22)

        elif "wish prashant" in query:
            kit.sendwhatmsg("+918790585413", "happy birthday", 19, 40)

        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "i love you" in query:
            speak("You taught me the real meaning of love. One look at your face sets my world straight!")

        elif "flirt with me" in query:
            speak("Do you have a name, or can I call you mine?")

        elif "pick up line" in query:
            speak("Can I follow you? Because my mom told me to follow my dreams")

        elif "open code" in query:
            os.startfile("C:\\Users\\shesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "email to a person" in query:
            try:
                speak("Enter email id: ")
                to = str(input())
                speak("What should I say?")
                content = takecommand().lower()
                sendEmail(to, content)
                speak("Email has been sent...")

            except Exception as e:
                print(e)
                speak("Couldn't send mail")

        elif "read pdf" in query:
            pdf_reader()

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("Sir, Please enter the correct username.")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir, here is the profile of the user {name}")
            time.sleep(5)
            speak("Would you like to download the profile picture of this account?")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir, profile picture is saved in our main folder.")
            else:
                pass

        elif "where am i" in query or "where are we" in query:
            speak("Wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir, I think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir, due to network issue I am not able to find where we are.")
                pass

        if "sleep" in query or "no" in query:
            speak("Going to sleep sir, have a great day.")
            sys.exit()
