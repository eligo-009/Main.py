import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from playsound import playsound
import wolframalpha
import requests
from bs4 import BeautifulSoup
import sys
import pywhatkit
import pyjokes
from sketchpy import library as lib
from requests import get, request
import random
from jmespath import search
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("Please tell me how may I help you")       

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



def computational_intelligence(question):
    try:
        client = wolframalpha.Client('4H2PW2-3JYYGVHJQ6')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None

def startup():
    speak("Initializing the cloud...")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak('Updating the cloud configuration')
    speak("All drivers are up and running")
    speak("All systems have been activated")


if __name__ == "__main__":
    
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
                speak('Searching Wikipedia...please wait')
                
                query = query.replace("wikipedia", "")
                results =  wikipedia.summary(query, sentences = 2)
                speak("Internet says...")
                print(results)
                speak(results) 

        elif 'hey'in query:
                
               
                speak('i am on.. ')

        elif "calculate" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
            
        elif "what is" in query or "tell me" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)

        
        elif 'open youtube' in query:
                webbrowser.open("youtube.com")

        elif 'open google' in query:
                webbrowser.open("google.com")

        elif 'open instagram' in query:
                webbrowser.open("instagram.com")

        elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")  

        elif 'open github' in query:
                webbrowser.open("github.com")

        elif 'my channel' in query:
                webbrowser.open('https://www.youtube.com/channel/UCNd_DDYwHrJQkw-dPoWL9QA')

        
            
        
        elif "hello" in query:
                speak('Hello sir , Good to see you')
                speak('How may i help You?')

        elif 'current temperature' in query:
                search = "temperature in my current location"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f'the current temperature in your current location is {temp}')

                
                
        elif 'nice' in query:
                speak(" 24/7 in your service sir ! you can call me anytime")
            
                sys.exit()

        elif 'shutup' in query:
                sys.exit()

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")


        elif 'can you play' in query:
                speak('Surfing the browser.... Hold on sir') 
                
                query = query.replace('jarvis'," ")  
                query = query.replace('play'," ")
                web = 'https://www.youtube.com/results?search_query=' + query
                pywhatkit.playonyt(query)
                speak(' Enjoy the music ')

        elif 'facebook' in query:
                
                speak('alright...')
                
                webbrowser.open("https://www.facebook.com")
                speak('Shall I readout the messages ?')

        elif "game" in query:
                from game import game_play
                game_play()

        elif 'joke' in query:
                speak(pyjokes.get_joke())
                

        elif "ip address" in query:
                ip = get("https://api.ipify.org").text
                
                speak(f'Your current ip address is {ip}') 
                

        elif 'search' in query:
                import wikipedia as googleScrap
                query = query.replace('jarvis', '   ')
                query = query.replace('google search', '    ')
                query = query.replace('google','    ')
            
                speak('Here are some results...')

                try:
                    pywhatkit.search(query)
                    result = googleScrap.summary(query,3)
                    speak(result)

                except:
                    speak(' Data not cached..')
                    
            #elif 'my location' in query:
                #from Features import My_Location
                #My_Location()              
        
           
                

            
                
        elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

           
        elif 'how to' in query:
                speak('Searching for best results.....')
                op = query.replace("jarvis","   ")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len (how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)


        elif 'where is' in query:
                from Features import GoogleMaps
                Place = query.replace('where is' ,"  ")
                Place = Place.replace("cortana", "  ")
                GoogleMaps(Place)

            
            
        elif 'space news' in query:
                speak('Say the date separated by And. For example 2021 and 12 and 09')

                Date =takeCommand()
                from Features import Dateconverter
                value = Dateconverter(Date)
                from Nasa import NasaNews
                NasaNews(value)    

        elif 'who are you' in query:
                speak('I am AI program Developed by Aditya Karna, Sushant kathari and Nikesh Adhekarei')

        elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)

        elif 'my girlfriend' in query or 'my gf' in query:
                speak('sorry , I am interested in Men not women')

        elif 'do god exist' in query:
                speak('I dont know , but i think god exists!')

        elif 'not funny' in query:
                speak('People wwith low IQ cant understand my jokes')

        elif 'vikas' in query:
                speak("vikas is a cylinder who became black due to explosion of cylinder while making tea")

        elif 'do you like black people' in query:
                speak('yes  i love black people but vikash is exception')

        elif 'which is the best college' in query:
                speak('Definetely, Emerald Academy is the best college around here as far i know')


        elif 'free diamonds' in query:
                speak('Yes of course ... How much Diamond do you want?')

        elif 'the best actor' in query:
                

                obj = lib.rdj()

                obj.draw()

                speak('You can see the best actor according to me')

        elif 'bts' in query:
                

                obj = lib.bts()

                obj.draw()

        elif 'tom holland' in query:
                
                
                obj = lib.tom_holland()

                obj.draw()

        elif 'who are you' in query:
                speak('Hello, I am ALpha')

        elif 'gojo' in query:
                obj = lib.gojo()
                obj.draw()

        elif 'bf' in query:
            speak('Yes, his name is Jarvis, Would you like to hear him?')
            from playsound import playsound
            playsound('Jarvis.mp3')

        elif 'shutdown the laptop' in query:
                import os
                os.system('shutdown /s /t 0')