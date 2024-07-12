import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import tkinter as tk
from tkinter import messagebox
import random
import string

print("Starting Virtual Assistant!")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
  engine.say(text)
  engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour)
  print(hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning")
  elif hour >= 12 and hour < 18:
    speak("Good Afternoon")
  else:
    speak("Good Evening")
  speak("How may I help you?")

def takeCommand():
  r = sr.Recognizer()

  choice = var.get()

  if choice == 1:
    with sr.Microphone() as source:
      print("Listening...")
      audio = r.listen(source)

    try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='en-in')
      print(f"User said: {query}\n")
      return query

    except Exception as e:
      speak("Say that again please")
      print("Say that again please")
      return None

  elif choice == 2:
    query = text_entry.get()
    return query

  else:
    print("Invalid choice. Please choose 1 or 2.")
    return None

def processQuery(query):
  if query == None:
    return

  elif 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

  elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")

  elif 'open google' in query.lower():
    webbrowser.open("google.com")

  elif 'time' in query.lower():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")
    print(f"The time is {time}")

  elif 'open vmware' in query.lower():
    path = "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"
    os.startfile(path)

  else:
    speak("Sorry, I can't perform that action yet. How else can I help you?")
    print("Sorry, I can't perform that action yet. How else can I help you?")

def generateCaptcha():
  captcha = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
  return captcha

def checkCaptcha(captcha, entry):
  if captcha == entry:
    return True
  else:
    return False

def main():
  root = tk.Tk()
  root.title("Virtual Assistant")

  captcha = generateCaptcha()
  tk.Label(root, text="Enter the captcha: " + captcha).pack()
  captcha_entry = tk.Entry(root, width=50)
  captcha_entry.pack()

  def submitCaptcha():
    if checkCaptcha(captcha, captcha_entry.get()):
      tk.Label(root, text="Choose input method:").pack()
      global var
      var = tk.IntVar()
      tk.Radiobutton(root, text="Speak", variable=var, value=1).pack()
      tk.Radiobutton(root, text="Type", variable=var, value=2).pack()

      global text_entry
      text_entry = tk.Entry(root, width=50)
      text_entry.pack()

      tk.Button(root, text="Submit", command=lambda: processQuery(takeCommand())).pack()
      speak("Hi, I am your virtual assistant!")
      wishMe()
    else:
      messagebox.showerror("Error", "Invalid captcha. Please try again.")

  tk.Button(root, text="Submit Captcha", command=submitCaptcha).pack()

  root.mainloop()

if __name__ == "__main__":
  main()