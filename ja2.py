import time
import pyttsx3  #text to speech
import datetime  # for date and time
import os   #intract with operating system
import cv2    # for camera vison
import random   #   for random selection
import requests  #http data fetch
import wikipedia
import webbrowser
import socket
from cv2 import cv2
import pywhatkit as kit     # for whatsapp message
import smtplib  # this module is used to send email to anyone : pip install secure-smptlib
import sys
import pyjokes        #for jocks
import speech_recognition as sr
import docx
import psutil   # google translation
import gtts




#voice
engine = pyttsx3.init('sapi5')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voices=engine.getProperty('voice')
engine.setProperty('voice',voice_id)

# text to speech
def speak(audio):  # converts in audio
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}")

    except Exception as e:
        print("Say that again please...")
        return "none"

    return query


def tellDay():

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
         day_of_the_week = Day_dict[day]
        # print(day_of_the_week)
         speak("Today is " + day_of_the_week)



# wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")


    elif hour >= 12 and hour <= 18:
        speak("good afternoon")

    else:
        speak("good evening")


    assname = ("AI assistant  Mohit Mudgal sir ")
    speak(f"I am your {assname}")
    tellDay()
    speak("How can i help you")




#sendemail
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ramu@gmail.com', '')
    server.sendmail('2019pietcsnivesh116@poornima.org', to, content)
    server.close()


if __name__ == '__main__':

    # takecommand()
    wish()


    while True:
        # if 1:
        query = takecommand().lower()
        # logic building for task     

        if "open notepad" in query:
            speak("opening notepad sir")
            npath = "C:\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open chrome" in query:
            speak("opening google chrome")
            gpath = "C:\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(gpath)


        elif "open adobe reader" in query:
            speak("opening adobe reader")
            apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader XI"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif 'play music' in query or "play song" in query:

            n = random.randint(1,10)
            print(n)
            speak("Here you go with music")
            # music_dir = "C:\\downloaded apps\\pythonProject AI assistant\\songs"
            music_dir = "W:\\python\\jarvis\\songs"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[n]))

        elif 'window camp' in query:
            os.system("start microsoft.windows.camera:")





        # online task

        elif "wikipedia" in query:# speak :-wikipedia and(what you want to search) together
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)


        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            z = takecommand().lower()
            if " fine " in query:
                speak("thats good sir")
            else:
                speak("all will be good sir")



        elif "who are you" in query:
            speak("I am your virtual assistant created by Mohit Mudgal")


        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("AI assistant ")



        # ip address and computer name
        elif "hostname" in query:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("your computer name  is :" + hostname)
            print("your ip address is :" + IPAddr)
            speak(f"Your Computer Name is:{hostname}")
            speak(f"Your Computer IP Address is:{IPAddr}")



        elif "open google" in query:
            speak("sir , what should  I serach on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")


        elif "send message" in query:                          #whattsapp
            speak("what msg do you want to send")
            m = takecommand().lower()   #  take message
            kit.sendwhatmsg("+918696891700", m, 21, 29)# time will be in 24 hr clock that is for 8:50pm = 20,50
            speak("message sent")
             # there should be gap of 2 minutes to send message



        elif "open youtube" in query:
            speak("tell me video which you want to play on youtube")
            sm = takecommand().lower()
            kit.playonyt(sm)  # this function works as a play songs on youtube



        elif "email to nivesh" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "niveshsoni9251@gmail.com"
                sendemail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send the email")



        elif "shut up" in query:
            speak("thanks for using me , have a good day")
            sys.exit()


        # to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "close adobe reader" in query:
            speak("okay sir, closing adobe reader")
            os.system("taskkill /f /im AcroRd32.exe")
        elif "close google chrome" in query:
            speak("closing chrome")
            os.system("taskkill /f /im chrome.exe")
        elif "close eclipse" in query:
            speak("closing eclipse")
            os.system("taskkill /f /im eclipse.exe")



        # to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'F://songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))


        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 1")
        elif "restart the system" in query:
            os.system("shutdown /r /t 1")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        elif "weather" in query:
            from datetime import datetime
            api_key = '88525598d371dba3025e6b852e211052'
            speak("tell me the city name: ")
            location = takecommand().lower()

            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            # create variables to store and display data
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            pressure_wind = api_data['main']['pressure']
            print("-------------------------------------------------------------")
            speak("Weather Stats for - {}  at date and time {}".format(location.upper(), date_time))
            print("-------------------------------------------------------------")
            speak("Current temperature is: {:.2f} deg C".format(temp_city))
            speak(f"Current weather desc  : {weather_desc}")
            speak(f"Current Humidity :{hmdt} {'%'}")
            speak(f"Current wind speed    :{wind_spd} {'kmph'}" )
            speak(f"current pressure is :{pressure_wind} {'atm'} ")



        elif "open word" in query:
            doc=docx.Document()
            parag=doc.add_paragraph("hello")
            doc.save("mohit.docx")
            os.system("start mohit.docx")



        elif "open camp"  in query:
            import cv2
            from time import sleep

            key = cv2.waitKey(1)
            webcam = cv2.VideoCapture(0)
            sleep(2)
            while True:
                speak('press s  to save image')
                try:
                    check, frame = webcam.read()
                    print(check)  # prints true as long as the webcam is running
                    print(frame)  # prints matrix values of each framecd
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)
                    if key == ord('s'):
                        cv2.imwrite(filename='saved_img.jpg', img=frame)
                        webcam.release()
                        print("Processing image...")
                        img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)

                        print("Resizing image to 28x28 scale...")

                        print("Resized...")
                        img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                        print("Image saved!")
                        speak("image saved")
                        break

                    elif key == ord('q'):
                        webcam.release()
                        cv2.destroyAllWindows()
                        break

                except(KeyboardInterrupt):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break



        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            fn = 'W:\\assi'
            p = os.popen('attrib +h ' + fn)
            t = p.read()
            p.close()
            speak("sir all the files  in this folder are now hidden")



        elif "show hidden file" in query:
            fn =  'W:\\assi'
            p = os.popen('attrib -h ' + fn)
            t = p.read()
            p.close()
            speak("sir all the files  in this folder are shown now ")




        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage >= 75:
                speak("we have enough power to continue our work")
            elif percentage >= 40 and percentage <= 75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage <= 15 and percentage <= 30:
                speak("we dont have enough power to work,please connect to charging")
            elif percentage <= 15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")




        elif "language" in query :
            speak("what you want to conver to hindi")
            from googletrans import Translator
            translater =Translator()
            ab=takecommand().lower()
            tr=translater.translate(f"{ab}",dest='hindi')
            speak(tr)
            print(tr.text)





        elif "open pycharm" in query :
            speak("opening pycharm")
            ppath ="E:\python\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(ppath)


        elif "open class" in query :
            speak("opening fifth sem")
            ppath="W:\ENGINEERING\\5th sem"
            os.startfile(ppath)


