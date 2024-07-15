import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np
import pyttsx3
import wikipedia


chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Raaam: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def fetch_wikipedia_data(topic):
    try:
        result = wikipedia.summary(topic, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Could you be more specific?"
    except wikipedia.exceptions.PageError as e:
        return f"Could not find information on {topic}. Please provide a valid topic."


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


    
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

  

def search_wikipedia(query):
    result = wikipedia.summary(query, sentences=2)
    return result



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "search Wikipedia for" in query.lower():
            search_query = query.lower().replace("search Wikipedia for", "").strip()
            wikipedia_result = search_wikipedia(search_query)
            say(f"Here is some information about {search_query} from Wikipedia:")
            say(wikipedia_result)


        if "open wikipedia".lower() in query.lower():
            say("Sure, what topic would you like to know about?")
            topic_query = takeCommand()
            wikipedia_data = fetch_wikipedia_data(topic_query)
            say(wikipedia_data)
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = r"C:\Users\ritik\Music\Rockstar.mp3"
            os.system(f"open {musicPath}")

        if "the time" in query:
            musicPath = r"C:\Users\ritik\Music\Rockstar.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")


        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        if 'open google' in query:
            webbrowser.open("google.com")

        if 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        if "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        if "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        if "Jarvis Quit".lower() in query.lower():
            exit()

        if "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)


