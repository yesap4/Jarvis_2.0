import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.getProperty('voice', voices[0].id)


def speak (audio):
    pass