import pyttsx3
import speech_recognition as sr
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

Height = 700
Width = 800

root = Tk()
image = Image.open('FBackground.jpg')
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo_image)
label.pack()


def Display_Pizza():
    image1 = Image.open("Pizza.jpg")
    image2 = image1.resize((500, 300), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image2)
    label = tkinter.Label(image=test)
    label.image = test
    label.place(x=400, y=250)


def Display_Burger():
    image1 = Image.open("Burger.jpg")
    image2 = image1.resize((500, 300), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image2)
    label = tkinter.Label(image=test)
    label.image = test
    label.place(x=400, y=250)


def Display_Pasta():
    image1 = Image.open("Pasta.jpeg")
    image2 = image1.resize((500, 300), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image2)
    label = tkinter.Label(image=test)
    label.image = test
    label.place(x=400, y=250)


def Fuction_No():
    Bcanvas = tk.Canvas(root, height=Height, width=Width)
    Bcanvas.pack()

    DAB = tk.Button(root, text='Pizza', font=('Courier', 18, 'bold'), command=Display_Pizza)
    DAB.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)
    HAPPY = tk.Button(root, text='Burger', font=('Courier', 18, 'bold'), command=Display_Burger)
    HAPPY.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.1)
    SAD = tk.Button(root, text='Pasta', font=('Courier', 18, 'bold'), command=Display_Pasta)
    SAD.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)

    Title = tk.Label(root, text='CLICK TO PREVIEW OR BUY', font=('Courier', 24, 'bold'), bg='grey')
    Title.place(relx=0.1, rely=0.025, relwidth=0.8, relheight=0.1)


def Fuction_Yes():
    engine = pyttsx3.init()
    engine.say("Which of the following food items would you like to buy? Pizza, Burger or the Pasta")
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

    if text == "Pizza" or text == "pizza":
        Display_Pizza()
    elif text == "Burger" or text == "burger":
        Display_Burger()
    elif text == "Pasta" or text == "pasta":
        Display_Pasta()
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
