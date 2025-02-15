import pyttsx3


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.getProperty('voice', voices[0].id)
  