from gtts import gTTS

print("\nCreazione file audio in corso ...")

text = """ Ciao a tutti bella raga, tutto rego? """
tts = gTTS(text=text, lang="it")
tts.save("vocale.mp3")

print("\nFile audio creato con successo!")

