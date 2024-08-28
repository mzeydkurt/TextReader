from gtts import gTTS
import playsound3

# Metni belirleyin
text = "Hi, How Are You ?"

# TTS objesini oluşturun
tts = gTTS(text=text, lang='en')

# Ses dosyasını kaydedin
tts.save("output1.mp3")

# Ses dosyasını oynatın
playsound3.playsound("output1.mp3")
