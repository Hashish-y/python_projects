import os
import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr 
import time
from gtts import gTTS 

def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)

while True:
	r=sr.Recognizer()

	with sr.Microphone() as source:
		print("Please speak..!!")
		audio=r.listen(source)
		try:
			text=r.recognize_google(audio)
			if text=="stop":
				break
			else:
				window=Tk()
				window.geometry("750x600")
				try:
					app_id = "WEVY59-4E3R3WGT6E"
					client=wolframalpha.Client(app_id)
					answer=next(res.results).text

					label1=Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font='times 15 bold')
					label1.pack()
					window.after(5000,lambda: window.destroy())
					mainloop()
				except Exception as e:
					print("No results from Wolfram|Alpha. Trying wikipedia...")
					answer = wikipedia.summary(text)
					print("Answer from Wikipedia:")
					print(answer)
					speak(answer)
					label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
					label1.pack()
					window.after(50000000, lambda: window.destroy())
					mainloop()
		except Exception as e:
			print(e)
			answer = "Sorry we cannt hear you"
			print(answer)
