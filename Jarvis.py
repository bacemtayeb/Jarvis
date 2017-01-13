#This code was created by : Bacem Tayeb
# All rights reserved @2017
import speech
import datetime
import subprocess
import random
import os
import time
from os.path import abspath, exists

speech.say("Jarvis is Speaking .")

def fun1():
	var1=random.choice(("Hey","Hello","Good To see you","Hi"))
	spoken_text = speech.input()
	speech.say(spoken_text)
	if spoken_text in("Hi","Hello","Hey","Welcome","Good morning","Good afternoon"):
		speech.say(var1)
	elif spoken_text=="goodbye":
		exit()
	else:
		None

	
def commands():
	speech.say("What can I do for you ")
	les=random.choice(("Open browser","Open chrome","Open Mozilla","Start browser","Run browser"))
	phrase=speech.input()
	while 1==1 :
		for word in les:
			if word==phrase:
				print"Opening Browser"
				f_path = abspath("browser.bat")
				if exists(f_path):
					os.system("browser.bat")
		
		
		les1=("Who are you ?")
		if les1==phrase:
				speech.say("I'm Jarvis.")
				print"My name is Jarvis. I'm designed to answer your questions Sir .  "
			
		les2=("Tell me a joke")
		if les2==phrase:
			speech.say("I'm programmer , I have no life !")
		les3=random.choice(("Date","What's the date","Tell me the date","Show me the date"))
		for word in les3:
			print"Showing Time"
			if word==phrase:
				a=time.strftime('%X %x %Z')
				'16:08:12 05/08/03 AEST'
				print a
				speech.say(a)
		les4=random.choice(("Open Calculator","Use Calculator","Start Calculator","Show Calculator"))
		for word in les4:
			print"Opening Calculator"
			if word==phrase:
				os.system('start calc.exe')
		les5=("Close your eyes")
		if phrase==les5:
			f_path = abspath("eye.bat")
			if exists(f_path):
				os.system("eye.bat")
		else:
			None
			
		les7="Open youtube"
		if phrase==les7:
			speech.say("I will open Youtube")
			print"Opening Youtube"
			f_path = abspath("youtube.bat")
			if exists(f_path):
				os.system("youtube.bat")
				
		les8="Open Facebook"
		if phrase==les8:
			speech.say("I will open Facebook")
			print"Opening Facebook..."
			f_path = abspath("Facebook.bat")
			if exists(f_path):
				os.system("Facebook.bat")
				
		les9="Open Email"
		if phrase==les9:
			speech.say("I will open your email")
			print"Opening Email ..."
			f_path = abspath("Email.bat")
			if exists(f_path):
				os.system("Email.bat")
		
fun1()
commands()
