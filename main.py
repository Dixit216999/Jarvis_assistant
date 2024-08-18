import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "7a597dc35a8747bd8f30aea55e5bf691"

def speak(text):
    engine.say(text)
    engine.runAndWait()

### This is paid service to integrate AI 

# def aiProcewss(command):
#     client = OpenAI(api_key="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",)

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful virtual assistant named Jarvis skilled in general tasks like Alexa, Siri and Google assistant."},
#             {
#                 "role": "user",
#                 "content": command
#             }
#         ]
#     )

    # return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open coursera" in c.lower():
        webbrowser.open("https://coursera.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open gfg" in c.lower():
        webbrowser.open("https://https://www.geeksforgeeks.org/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            #Extract the articlesw
            articles = data.get('articles',[])

            #Speak the headlines
            for article in articles :
                speak(article['title'])
    
    # else:
    #     #Let Open AI handle the request
    #     output = aiProcewss(c)
    #     speak(output)   # openAI is paid so to use you have to pay




if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()
        
    # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes My Lord")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated and waiting for your Command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("error; {0}".format(e)) 