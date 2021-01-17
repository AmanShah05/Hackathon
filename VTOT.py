import pyttsx3
import speech_recognition as sr
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

Height = 700
Width = 800

root = Tk()


def Display_Balloon():
    image1 = Image.open("Balloon.jpg")
    test = ImageTk.PhotoImage(image1)
    label = tkinter.Label(image=test)
    label.image = test
    label.place(x=150, y=190)


def Display_Waterfall():
    image1 = Image.open("Waterfall.jpg")
    test = ImageTk.PhotoImage(image1)
    label = tkinter.Label(image=test)
    label.image = test
    label.place(x=150, y=190)


def Display_Mountain():
    image1 = Image.open("Mountain.jpg")
    image2 = image1.resize((200, 200), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image2)
    label = tkinter.Label(image=test)
    label.image = test
    label.place(x=150, y=190)


def Fuction_No():
    Bcanvas = tk.Canvas(root, height=Height, width=Width)
    Bcanvas.pack()

    Bframe = tk.Frame(root, bg='#80c1ff')
    Bframe.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    DAB = tk.Button(Bframe, text='Balloon', font=('Courier', 18, 'bold'), command=Display_Balloon)
    DAB.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)
    HAPPY = tk.Button(Bframe, text='Waterfall', font=('Courier', 18, 'bold'), command=Display_Waterfall)
    HAPPY.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.1)
    SAD = tk.Button(Bframe, text='Mountain', font=('Courier', 18, 'bold'), command=Display_Mountain)
    SAD.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)

    Title = tk.Label(Bframe, text='CLICK ONE OF THE BUTTONS', font=('Courier', 24, 'bold'), bg='#80c1ff')
    Title.place(relx=0.1, rely=0.025, relwidth=0.8, relheight=0.1)


def Fuction_Yes():
    engine = pyttsx3.init()
    engine.say("Which of the following images would you like to buy? Waterfall, Mountain or the Balloon")
    engine.runAndWait()
    r = sr.Recognizer()
    print("Please Talk")
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        text: object = r.recognize_google(audio_data)
        print(text)

    canvas = tk.Canvas(root, height=Height, width=Width)
    canvas.pack()

    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    if text == "balloon" or text == "Balloon":
        Display_Balloon()
    elif text == "waterfall" or text == "Waterloo":
        Display_Waterfall()
    elif text == "mountain" or text == "Mountain":
        Display_Mountain()
    else:
        print("Didn't recognize what you said")


engine = pyttsx3.init()
engine.say("Would you like to use the Voice Recognition?")

engine.runAndWait()
r = sr.Recognizer()
print("Please Talk")
with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    try:
        text: object = r.recognize_google(audio_data)
    except:
        engine = pyttsx3.init()
        engine.say("This is not an option, please restart the program.")
        engine.runAndWait()
        sys.exit()

if text == "No" or text == "no":
    Fuction_No()
elif text == "Yes" or text == "yes":
    Fuction_Yes()
else:
    engine = pyttsx3.init()
    engine.say("This is not an option, please restart the program.")
    engine.runAndWait()
    sys.exit()

root.mainloop()
