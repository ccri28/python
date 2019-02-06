from gtts import gTTS
import subprocess

text = """
    Ciao Nonno, come stai ? Domani vai a Milano
 """

tts=gTTS(text=text, lang="it")
tts.save("vocale_audio.mp3")

print("Operazione effettuato con successo! File audio creato")

#subprocess.run(["VLC media player","vocale_audio.mp3"])
