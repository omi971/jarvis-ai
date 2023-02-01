import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

voice_tone = 0
print(voices)
engine.setProperty('voice', voices[voice_tone].id)


def change_Voice(idx=0):
    global voice_tone
    if voice_tone == 0:
        voice_tone = 1
    else:
        voice_tone = 0

    print(voices)
    speak("Sir I am Changing the voice")
    engine.setProperty('voice', voices[voice_tone].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am JARVIS Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # r.dynamic_energy_threshold = True
        # r.dynamic_energy_adjustment_damping = 0.50
        # r.dynamic_energy_ratio = 2
        r.pause_threshold = 0.5
        # r.operation_timeout = 1

        audio = r.listen(source)
        # print(audio)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('omiindustriesbot@gmail.com', 'e!9f^KGx5LQJhq8')
    server.sendmail('omiindustriesbot@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    global nxt
    nxt = 0
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

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com/")

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("https://stackoverflow.com/")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/")

        elif 'open messenger' in query:
            speak("opening messenger")
            webbrowser.open("https://www.messenger.com//")

        elif 'play music' in query:
            music_dir = 'D:\\AODIO SONG\\My Music\\Music(GYM)'
            songs = os.listdir(music_dir)
            print(songs)
            # nxt = 0
            if 'next' in query:
                nxt += 1
                os.startfile(os.path.join(music_dir, songs[nxt]))
            else:
                os.startfile(os.path.join(music_dir, songs[nxt]))
            print("Nxt", nxt)
            print("Playing", songs[nxt])

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Nazmul Haque Omi\\AppData\\Local\\slack\\slack.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Okay Sir, Where do I send the message?")
                mail_num = takeCommand()

                mail_lst = ["ahsankoushik@gmail.com",
                            "nazmulhaqueomi971@gmail.com",
                            "nazmul.haque.omi@g.bracu.ac.bd",
                            "nazmulhaqueomi580@gmail.com"]

                to = mail_lst[int(mail_num)]
                # to = "wtfm962@gmail.com"

                # to = "Nazmulhaqueomi971@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir Omi. I am not able to send this email right now. Please try again later")

        elif "play games" in query:
            speak("Which game you want to play sir.!")
            game_name = takeCommand().lower()
            game_path = None
            if "black flag" in game_name:
                game_path = "J:\\ACBF\\AC4BFSP.exe"
                os.startfile(game_path)

        elif "close this" in query:
            t1 = int(datetime.datetime.now().second)

            speak("Sir I am Closing this")
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            pyautogui.keyUp("alt")

            t2 = int(datetime.datetime.now().second)
            speak("The Program Closed sir")
            time_1 = abs(t2-t1)
            speak(f"Time  Counted {time_1} seconds sir")
            print("Time:", time_1)

        elif 'change voice' in query:
            change_Voice()

        elif 'quit' in query:
            speak("Thank you sir")
            exit()
