import cv2
from time import sleep
import time
import pyttsx3
import datetime
import os
import cv2
import random
import requests
import wikipedia
import webbrowser
import socket
from cv2 import cv2
import pywhatkit as kit
import smtplib  # this module is used to send email to anyone : pip install secure-smptlib
import sys
import pyjokes
import speech_recognition as sr
import docx
import psutil

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
        speak("Say that again please...")
        return "none"

    return query



key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
while True:
    query = takecommand().lower()
    try:
        check, frame = webcam.read()
        print(check)  # prints true as long as the webcam is running
        print(frame)  # prints matrix values of each framecd
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)

        if key == ord('play' in query):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray, (28, 28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")

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