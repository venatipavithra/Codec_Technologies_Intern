import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use your mic for input
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")