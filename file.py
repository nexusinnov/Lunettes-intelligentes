

from gtts import gTTS
import pygame
from io import BytesIO

# Texte à lire en différentes langues
text_arabic = "هذا مثال لنص عربي"
text_french = "Ceci est un exemple de texte en français"
text_english = "This is an example of text in English"

# Création des objets gTTS pour chaque langue
tts_arabic = gTTS(text=text_arabic, lang='ar')
tts_french = gTTS(text=text_french, lang='fr')
tts_english = gTTS(text=text_english, lang='en')

# Lecture du flux audio en mémoire pour chaque langue
audio_streams = {}

for lang, tts_object in {'arabic': tts_arabic, 'french': tts_french, 'english': tts_english}.items():
    stream = BytesIO()
    tts_object.write_to_fp(stream)
    stream.seek(0)
    audio_streams[lang] = stream

# Initialisation de pygame pour la lecture audio
pygame.mixer.init()

# Lecture audio pour chaque langue
for lang, audio_stream in audio_streams.items():
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()
    # Attente jusqu'à la fin de la lecture
    while pygame.mixer.music.get_busy():
        continue
