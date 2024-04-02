import pyttsx3


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


# Print available voices
print_available_voices()


def read_proprietary_text(text, language='en'):
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()

    # Get list of available voices
    voices = engine.getProperty('voices')

    # Select voices for English and French
    english_voice = None
    french_voice = None
    for voice in voices:
        if "english" in voice.name.lower():
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


# Example usage
english_text = "This is an example text in English."
french_text = "Ceci est un texte exemple en français."
arabic_text = "هذا مثال لنص عربي "

read_proprietary_text(english_text, language='en')
read_proprietary_text(french_text, language='fr')
read_proprietary_text(arabic_text, language="ar")