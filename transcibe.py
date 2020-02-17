import speech_recognition as sr

r = sr.Recognizer()

def speech2text(filename):
    audiofile = sr.AudioFile(filename)

    with audiofile as source:
        audio = r.record(source)

    text= r.recognize_google(audio)
    print(text)

    return text
    
def microphone():
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print("time over thanks")

    text= r.recognize_google(audio)
    print(text)
    return text

if __name__== "__main__":
    filename= 'example/test1.wav'
    text= speech2text(filename)
    
    microphone()

    print("done")