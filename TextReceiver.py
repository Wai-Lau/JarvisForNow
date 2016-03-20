import json
#the next two are just for here
import pyaudio
import time
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
print("done listening")

# recognize speech using Google Speech Recognition
try:
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # otherwise `r.recognize_google(audio)`
	phrase = r.recognize_google(audio)
	words = phrase.split(" ")
	for word in words:
		print("-"+word)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

#this part for receiving JSON
'''
receivedJSON = open('textReceived.txt', 'r')
receivedText = json.loads(receivedJSON.read())
listOfWords = receivedText['QueryResult']['mrec_results']['transcriptions']
print(listOfWords[0])
'''

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("WayUp.wav")
pygame.mixer.music.play()
time.sleep(30)