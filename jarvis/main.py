import pyttsx3
import  speech_recognition as sr
import webbrowser
import datetime

def Speechtotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("We are listening to your instruction")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            # print(data)
            return data
        except sr.UnknownValueError:
            print(" Try again......")

def texttospeech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',125)
    engine.say(text)
    engine.runAndWait()

# texttospeech("welcome to Nedula")
# text = Speechtotext()
# texttospeech(text)

if __name__ == '__main__':
    if Speechtotext().lower() == "hi ruchi":
        texttospeech("Hi Shivam")
        while
    #     use this to add chatgpt https://www.youtube.com/watch?v=Vurdg6yrPL8
    else:




