import tkinter as tk
import time
import os
import sys
import subprocess
import datetime
import webbrowser
from time import strftime
from time import sleep
from tkinter import filedialog
import speech_recognition as sr
import requests
from tkinter.messagebox import showerror
from wikipedia import summary
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import requests
import pyttsx3

window = tk.Tk()
window.geometry("450x450")
window.title('main window')
Label(window,text="Virtual Assistant",font=("arial",20)).pack()
bgimage=PhotoImage(file="assistant.png")
Label(window,image=bgimage).pack()


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice=voices[1]
    engine.setProperty('voice', voice.id)
    engine.say(text)
    engine.runAndWait()
    
def getinput():
    text=''
    r=sr.Recognizer()
    g_input=False
    with sr.Microphone() as source:
        while g_input==False:
            try:
                r.energy_threshold=10000
                r.adjust_for_ambient_noise(source,1.2)
                speak("Listening.....")
                print ("Listening...")
                audio=r.listen(source)
                text=r.recognize_google(audio)
                print("You said: ",text)
                g_input=True
                
            except:
                speak("Sorry, I couldn't understand you")
                print ("Sorry, I couldn't understand you")
                g_input=False
    return text

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning. What can I do for you?")
        print("Hello,Good Morning. What can I do for you?")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon. What can I do for you?")
        print("Hello,Good Afternoon. What can I do for you?")
    else:
        speak("Hello,Good Evening. What can I do for you?")
        print("Hello,Good Evening. What can I do for you?")


        
def dateandtime():
    new=Toplevel(window)
    new.geometry("200x200")
    new.title("Date window")
    now=datetime.datetime.now()
    Year=now.strftime("%Y")
    Month=now.strftime("%m")
    Day=now.strftime("%d")
    Timeformat=now.strftime("%I")
    Minute=now.strftime("%M")
    Second=now.strftime("%S")
    Meridiems=now.strftime("%p")
    CurrentDate= Day +"/"+ Month+"/" + Year
    CurrentTime=Timeformat+":"+ Minute+":"+Second + Meridiems
    Label(new,text=CurrentDate).pack()
    Label(new,text=CurrentTime).pack()

    new.update()
    speak(("Cuurent Date is ", CurrentDate, "Current Time is ",CurrentTime))
    # sleep(2)
    
def website():
    global e
    def search():
        webbrowser.register("chrome",None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        website = e.get() 
        url="http://www."+website+".com"
        webbrowser.get("chrome").open(url)
        new.update()
        speak((website+"has been opened"))
    new=Toplevel(window)
    new.geometry("500x500")
    new.title("Website window")
    Label(new,text="Enter the name of website").pack()
    e = Entry(new)
    e.pack()
    Button(new,text='Search',command=search).pack()
    new.update()
    speak(("Enter the website you want to open and press Search"))
def opendocs():
    
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

    def explore(path):
        # explorer would choke on forward slashes
        path = os.path.normpath(path)

        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
   
    path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
    sys.path.append(path)

   
    subprocess.Popen('explorer "C:\temp"')
    new.update()
    speak("Opening Documents")
    

def weather():
    global a
    def Gen_report():
        city = a.get() 
        url = 'https://wttr.in/'+city
        try:
            data = requests.get(url)
            T = data.text
        except:
            T = "Error Occurred"

        Label(new,text=T).pack()
        new.update()
        speak(("The weather forecast of"+city+"has been opened"))
    
    new=Toplevel(window)
    new.geometry("500x500")
    new.title("Weather window")
    Label(new,text="Enter the name of City").pack()
    a = Entry(new)
    a.pack()
    Button(new,text='Search',command=Gen_report).pack()
    new.update()
    speak("Enter the city for which you want the weather forecast and press Search")
def wikipedia():
    def get_summary():
            try:
                answer.delete(1.0, END)
                answer.insert(INSERT, summary(keyword_entry.get()))
                new.update()
                speak(summary(keyword_entry.get()))
            except Exception as error:
                showerror("Error", error)
                new.update()
                speak("Error found")
    
    new=Toplevel(window)
    new.geometry("800x800")
    new.title("Wikipedia window")
    keyword_entry = Entry(new)
    keyword_entry.pack()
    search_button = Button(new, text="SEARCH",command=get_summary)
    search_button.pack()
    scroll = Scrollbar(new)
    answer = Text(new, yscrollcommand=scroll.set)
    answer.pack()
    scroll.pack()
    new.update()
    speak("Enter the topic you want to search on Wikipedia and press Search")
    
def bye():
    speak("Good Bye!")
    print ("Good bye!")
    window.destroy()
    
def audio_commands():
    statement=getinput()
    print("statement", statement)
    if "hi" in statement or "hello" in statement or "hey" in statement:
        wishMe()
    elif "date" in statement or "time" in statement:
        dateandtime()
    elif "files" in statement or "documents" in statement or "file manager" in statement or "docs" in statement:
        opendocs()
    elif "weather" in statement or "forecast" in statement or "temperature" in statement:
        weather()
    elif "search" in statement or "wikipedia" in statement:
        wikipedia()
    elif "bye" in statement or "goodbye" in statement or "close" in statement or "see you later" in statement:
        bye() 
    else:
        speak("Sorry, I cannot perform required function")

    
btn_date=Button(window,text ="Date and Time",command=dateandtime)
btn_date.pack()
btn_website=Button(window,text="Open a Website",command=website)
btn_website.pack()
btn_docs=Button(window,text="Open Documents",command=opendocs)
btn_docs.pack()
btn_weather=Button(window,text="Weather Forecast",command=weather)
btn_weather.pack()
btn_wikipedia=Button(window,text="Search from Wikipedia",command=wikipedia)
btn_wikipedia.pack()
record=PhotoImage(file="record.png")
btn_audio=Button(window,text="Record",image=record,command=audio_commands)
btn_audio.pack()
btn_close=Button(window,text="Close",command=window.destroy)
btn_close.place(x=350,y=400)
window.update()
speak("Welcome to your personal virtual assistant. How may I help you today?")

window.mainloop()
