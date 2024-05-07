import pyttsx3
from tkinter import Tk, Button, Label, Frame

def print_available_voices():
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()
    
    # Get list of available voices
    voices = engine.getProperty('voices')
    
    # Print information about each voice
    for i, voice in enumerate(voices):
        print(f"Voice {i + 1}:")
        print(f" - Name: {voice.name}")
        print(f" - Languages: {voice.languages}")
        

def read_proprietary_text(text, language='en', speed=100):
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)  

    # Get list of available voices
    voices = engine.getProperty('voices')
    
    # Select voices for English and French
    english_voice = None
    french_voice = None
    for voice in voices:
        if  "english" in voice.name.lower():
            english_voice = voice
        elif "french" in voice.name.lower():
            french_voice = voice
    
    # Set the selected voices
    if language == 'en' and english_voice:
        engine.setProperty('voice', english_voice.id)
    elif language == 'fr' and french_voice:
        engine.setProperty('voice', french_voice.id)
    else:
        print("No suitable voice found for the specified language. Default voice will be used.")
    
    # Queue the text for speech synthesis
    engine.say(text)
    
    # Process the queued commands and speak the text
    engine.runAndWait()

def increase_speed():
    global speed
    speed += 50
    if speed > 300:
        speed = 300
    speed_label.config(text=f"Speed: {speed}")
    
def decrease_speed():
    global speed
    speed -= 50
    if speed < 50:
        speed = 50
    speed_label.config(text=f"Speed: {speed}")
    
def read_text_with_adjusted_speed():
    global selected_text
    global selected_language
    global speed
    
    # Read the selected text with adjusted speed
    read_proprietary_text(selected_text, language=selected_language, speed=speed)

# Create GUI window
root = Tk()
root.title("Text-to-Speech")

# Initialize variables
speed = 100
selected_text = ""
selected_language = ""

# Create buttons
speed_frame = Frame(root)
speed_frame.pack(pady=10)

speed_label = Label(speed_frame, text=f"Speed: {speed}")
speed_label.pack(side="top")

increase_button = Button(speed_frame, text="Increase Speed", command=increase_speed)
increase_button.pack(side="left", padx=5)

decrease_button = Button(speed_frame, text="Decrease Speed", command=decrease_speed)
decrease_button.pack(side="right", padx=5)

read_button = Button(root, text="Read Text", command=read_text_with_adjusted_speed)
read_button.pack()

# Example usage
english_text = "This is an example text in English."
french_text = "Ceci est un texte exemple en français."
arabic_text = "هذا مثال لنص عربي."

# Set selected text and language
selected_text = english_text
selected_language = "en" 

# Run the GUI
root.mainloop()
