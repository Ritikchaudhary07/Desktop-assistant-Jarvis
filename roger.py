import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import openai
from config import apikey
from googlesearch import search  # Import the search function from the googlesearch library



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def ai(prompt):
    openai.api_key=apikey

response = openai.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["text"])
if os


# ///////
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am ROGER SIR.  Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        if 'open google' in query:
            webbrowser.open("google.com")

        if 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        if 'play music' in query:
            music_dir = "C:\Users\ritik\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        if 'open code' in query:
            codePath = "C:\Users\ritik\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)


        if 'shutdown pc' in query:
                 speak("Are you sure you want to shutdown the computer?")
                 response = takeCommand().lower()
                 if 'yes' in response:
                     speak("Shutting down the computer. Goodbye!")
                     os.system("shutdown /s /t 1")  # This command will shut down the computer after a delay of 1 second.
                 else:
                    speak("Shutdown aborted. I will continue to assist you.")

        if "using artificial intelligence".lower() in query.lower():
             ai(prompt=query)

         
        if 'search on google' in query:
               speak("What would you like to search for?")
               search_query = takeCommand()
               speak(f"Searching on Google for {search_query}")
    
    # Perform the Google search and print the top 5 results
        for j, result in enumerate(search(search_query, num=5, stop=5, pause=2)):
               print(f"Result {j + 1}: {result}")
               speak(f"Result {j + 1}: {result}")



        
 

  
