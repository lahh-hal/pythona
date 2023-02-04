import speech_recognition as sr
import webbrowser
import subprocess
import time
import platform

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

while True:
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Say 'Hey, Hal' to start speech recognition")
        audio_text = r.listen(source)

    # recognize_google method will throw a request to the API
    # and will get the response
    text = r.recognize_google(audio_text)
    print("You said: " + text)

    # Start speech recognition only if the user says "Hey, Hal"
    if text == "Hey Hal":
        time.sleep(3)
        print("Talk")
        with sr.Microphone() as source:
            audio_text = r.listen(source)
        print("Time over, thanks")

        # recognize_google method will throw a request to the API
        # and will get the response
        text = r.recognize_google(audio_text)
        print("Text: "+ text)

        # Check if the user is asking to open an application
        if "open" in text:
            words = text.split()
            app_name = words[0]

            if platform.system() == 'Darwin':  # macOS
                subprocess.call(["open", "-a", app_name])
            elif platform.system() == 'Windows':  # Windows
                subprocess.call([app_name + ".exe"])
            else:  # Linux and other platforms
                subprocess.call(["xdg-open", app_name])
        # Search for the transcribed text on Google or YouTube
        elif text.lower() == "youtube":
            if platform.system() == 'Darwin':  # macOS
                webbrowser.open("https://www.youtube.com/results?search_query=" + text)
            elif platform.system() == 'Windows':  # Windows
                webbrowser.open("https://www.youtube.com/results?search_query=" + text, new=1)
            else:  # Linux and other platforms
                webbrowser.open("https://www.youtube.com/results?search_query=" + text)
        else:
            if platform.system() == 'Darwin':  # macOS
                webbrowser.open("https://www.google.com/search?q=" + text)
            elif platform.system() == 'Windows':  # Windows
                webbrowser.open("https://www.google.com/search?q=" + text, new=1)
            else:  # Linux and other platforms
                webbrowser.open("https://www.google.com/search?q=" + text)
    else:
        print("Speech recognition not started")
