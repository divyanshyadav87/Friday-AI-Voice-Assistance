import speech_recognition as sr
import edge_tts
import asyncio
import tempfile
import uuid
import os
import webbrowser
import pygame
import time
import requests
import google.generativeai as genai
import datetime
import pyjokes


pygame.mixer.init()
newsapi = "60d34017dcb849638b7cef7a3f269b95"
genai.configure(api_key="AIzaSyAFWY3spl5n_k1ASXqmEKXVR82LLr2mWv4")
model = genai.GenerativeModel("gemini-1.5-flash")




async def edge_speak_async(text, voice="en-IN-NeerjaNeural", rate="+35%"):
    filename = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}.mp3")
    tts = edge_tts.Communicate(text, voice=voice, rate=rate)
    await tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def speak(text, voice="en-IN-NeerjaNeural"):
    asyncio.run(edge_speak_async(text, voice))


def get_date():
    now = datetime.datetime.now()
    date = now.strftime("%A, %d %B %Y")
    # time = now.strftime("%I:%M %p")
    speak(f"Todays date is {date}")

def get_time():
    now = datetime.datetime.now()
    # date = now.strftime("%A, %d %B %Y")
    time = now.strftime("%I:%M %p")
    speak(f"the time is {time}.")

def get_joke():
    joke = pyjokes.get_joke()
    speak(joke)

import requests

def get_weather(city="Delhi"):
    api_key = "8e88b99a638fdf353304e6f9c1c1deb5"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("main"):
        temp = response["main"]["temp"]
        condition = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp}°C with {condition}.")
    else:
        speak("Sorry, I couldn't fetch the weather right now.")


def processCommand(command):
    command = command.lower()
    print("Processing Command:", command)

    if command.lower() in ["open youtube", "open you tube", "open utube", "open u tube" , "youtube kholo" , "youtube khol do" , "youtube kholna" , "youtube kholne" , "youtube khol", "youtube khol de" , "youtube khol do"     , "youtube khol de do" , "youtube",  "utube", "u tube", "youtube" ]:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif command.lower() in ["open google", "google kholo", "google khol do", "google kholna", "google kholne", "google khol", "google khol de", "google khol do" , "google khol de do" , "google", "googel", "gogle","goglee", "googel", "googel" ,"gogle" , "goglee" , "googel" , "googel" , "gogle" , "goglee" , "googel"]:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif command.lower() in ["open gmail", "gmail kholo", "gmail khol do", "gmail kholna", "gmail kholne", "gmail khol", "gmail khol de", "gmail khol do" , "gmail khol de do" , "gmail", "g mail", "g-mail", "gmaail", "gmaail", "gmaail", "mail", "mail", "meil", "meil", "meil", "meil", "open g mail","mel kholo","male kholo", "open g-mail", "open gmaail", "open gmaail", "open gmaail", "open mail", "open meil", "open meil", "open meil", "open meil", "mail khol", "mail khol do", "mail kholna", "mail kholne", "mail kholo", "meil khol", "meil khol do", "meil kholna", "meil kholne" , "email khol", "email khol do", "email kholna", "email kholne" , "email kholo", "open email", "open email", "open email", "open email"]:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif command.lower() in ["facebook kholo", "facebook khol do","open facebook", "facebook kholna", "facebook kholne", "facebook khol", "facebook khol de", "facebook khol do" , "facebook khol de do" , "facebook", "face book", "face-book", "facebok", "facebok", "facebok", "book", "book", "buk", "buk", "buk", "buk", "open face book", "open face-book", "open facebok", "open facebok", "open facebok", "open book", "open buk", "open buk", "open buk", "open buk"]:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com") 
    elif command.lower() in ["instagram kholo", "instagram khol do", "instagram kholna", "instagram kholne", "instagram khol", "instagram khol de", "instagram khol do" , "instagram khol de do" , "instagram", "insta", "insta", "insta", "insta", "gram", "gram", "gram", "gram", "open insta", "open insta", "open insta", "open insta", "open gram", "open gram", "open gram", "open gram"]:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif command.lower() in ["linkedin kholo", "open linkedin","linkedin khol do", "linkedin kholna", "linkedin kholne", "linkedin khol", "linkedin khol de", "linkedin khol do" , "linkedin khol de do" , "linkedin", "link din", "link-din", "linkdin", "linkdin", "linkdin", "din", "din", "din", "din", "open link din", "open link-din", "open linkdin", "open linkdin", "open linkdin", "open din", "open din", "open din", "open din"]:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif command.lower() in ["chatgpt kholo","chat","chat gpt kholo", "chatgpt khol do","gpt kholo", "chatgpt kholna","set gpt kholo","sad CPT kholo", "chatgpt kholne", "chatgpt khol", "chatgpt khol de", "chatgpt khol do" , "chatgpt khol de do" , "chatgpt", "chat gpt", "chat-gpt", "chat gpt", "chat gpt", "chat gpt", "gpt", "gpt", "gpt", "gpt", "open chat gpt", "open chat-gpt", "open chat gpt", "open chat gpt", "open chat gpt", "open gpt", "open gpt", "open gpt", "open gpt"]:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
    elif command.lower() in ["date batao", "tell me date", "date", "aaj date kya hai"]:
        get_date()
    elif command.lower() in ["time batao", "time kya hua", "time", "tell me time"]:
        get_time()
    elif command.lower() in ["joke", "joke batao", "joke sunao", "tell me a joke","tel mi an joke"]:
        get_joke()
    elif command.lower() in ["weather","mausam kya hai","mausam","vedar batao","tell me weather","vedar","mausam batao"]:
        get_weather()
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif command.lower() in ["news", "News", "tell me news","news batao"]:
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=60d34017dcb849638b7cef7a3f269b95")
        data = r.json()
        articles = data.get("articles", [])
        speak("Reading the latest news Headlines One by one.")
        i = 0
        while i < len(articles):
            speak(articles[i].get("title"))

            # Listen for "next" or "stop"
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for 'next' or 'stop' command...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=1)

            try:
                user_command = recognizer.recognize_google(audio, language='en-IN').lower()
                print("Heard:", user_command)

                if user_command in ["stop", "bus karo","chup ho jao"]:
                    speak("Stopping news reading...")
                    break
                elif user_command in ["next", "agli","aage","koi aur",]:
                    i += 1 
                else:
                    print("Say 'next' for the next headline or 'stop' to stop.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't heard...")
                i+=1
            except sr.RequestError:
                speak("Network error...")


    elif command.lower() in ["exit", "quit", "stop", "bye","bye-bye","so jao", "goodbye", "shut down", "turn off", "deactivate friday", "deactivate friend", "deactivate friend", "deactivate friday", "deactivate friday", "deactivate friday", "deactivate friday" , "close friday", "close friend", "close friend", "close friday", "close friday", "close friday", "close friday" , "terminate friday", "terminate friend", "terminate friend", "terminate friday", "terminate friday", "terminate friday", "terminate friday" , "end friday", "end friend", "end friend", "end friday", "end friday", "end friday", "end friday", "band karo" , "band kar do" , "band karna" , "band karne" , "band kar", "band kar de" , "band kar do"     , "band kar de do" , "exit", "quit", "stop", "bye", "goodbye", "shut down", "turn off", "close", "close", "close", "close", "terminate", "terminate", "terminate", "terminate", "end", "end", "end", "end", "off", "chup ho jao", "chup ho ja", "chup raho", "chup", "chup ekdamchu"]:
        speak("Shutting down. Goodbye Sir...")
        return False  
    else:
        response = model.generate_content(command)
        response_text = response.text.replace("**", "")
        speak(response_text)

    return True 

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    speak("Initializing Friday...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for activation...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=1.5)

            word = recognizer.recognize_google(audio, language='en-IN')
            print("Heard:", word)

            if word.lower() in ["Friday", "friday", "friend", "friend", "friday", "friday", "friday", "friday", "activate friday", "activate friend", "activate friend", "activate friday", "activate friday", "activate friday", "activate friday" , "wake up friday", "wake up friend", "wake up friend", "wake up friday", "wake up friday", "wake up friday", "wake up friday", "start friday", "start friend", "start friend", "start friday", "start friday", "start friday", "start friday"]:
                speak("Yes Sir...") 
                active = True

                while active:
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = recognizer.listen(source, timeout=None, phrase_time_limit=1.5)

                    try:
                        command = recognizer.recognize_google(audio, language='en-IN')
                        print("Command:", command)
                        active = processCommand(command)
                    except sr.UnknownValueError:
                        speak("Sorry, I didn't heard")
                    except sr.RequestError:
                        speak("Network error...")

        except Exception as e:
            print("Error:", e)
