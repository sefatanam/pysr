import speech_recognition as sr
import subprocess
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening . . . ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(format(text))
            if(text == "stop"):
                break
            else:
                if text == "open downloads" or text == "see my downloads":
                    subprocess.check_output("Downloads.bat")
                    break

                elif text == "open Torrent folder" or text == "open my movies folder":
                    subprocess.check_output("BiglyBt.bat")
                    break

                elif text == "open my project" or text == "project folder":
                    subprocess.check_output("Project.bat")
                    break

                else:
                    print("Not match with given instruction")

        except:
            print("I can't recognize you voice, Sir")
