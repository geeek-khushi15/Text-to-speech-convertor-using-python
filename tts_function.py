# tts_function.py
from gtts import gTTS
import os

def text_to_speech(mytext, language='en'):
    # Convert text to speech
    myobj = gTTS(text=mytext, lang=language, slow=False)
    
    # Save the audio file
    filename = "output.mp3"
    myobj.save(filename)
    
    # Play the converted file (uncomment for local use)
    # os.system("start " + filename)
    
    return filename
