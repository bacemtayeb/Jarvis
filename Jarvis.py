import speech
import datetime
import subprocess
import random
import os
import time
from os.path import abspath, exists

speech.say(Jarvis is speaking ")

def fun():
	var1=random.choice(("Good morning Sir","Hello","Good To see you"))
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
	les=("Open browser","Open chrome","Open Mozilla","Start browser","Run browser")
	phrase1=speech.input()
	for phrase1 in les:
		f_path = abspath("a.bat")
		if exists(f_path):
			os.system("a.bat")
		break
		
def fun1():
	les3=("Date","What's the date","Tell me the date","Show me the date")
	phrase1=speech.input()
	for phrase1 in les3:
		print"Showing Time"
		a=time.strftime('%X %x %Z')
		'16:08:12 05/08/03 AEST'
		print a
		speech.say(a)
		break
		
def fun2():
	les2=("Tell me a joke")
	phrase3=speech.input()
	for phrase3 in les2:
		speech.say("I'm programmer, I have no life !")
		break
	
def fun3():
	les5=("Close your eyes")
	phrase4=speech.input()
	for phrase4 in les5:
		f_path = abspath("eye.bat")
		if exists(f_path):
			os.system("eye.bat")
		else:
			None
		break

def fun4():
	les7="Open youtube"
	phrase5=speech.input()
	for phrase5 in les7:
		speech.say("I will open Youtube")
		print"Opening Youtube"
		f_path = abspath("youtube.bat")
		if exists(f_path):
			os.system("youtube.bat")
		break
	
def fun5():
	les8="Open Facebook"
	phrase6=speech.input()
	for phrase6 in les8:
		speech.say("I will open Facebook")
		print"Opening Facebook..."
		f_path = abspath("Facebook.bat")
		if exists(f_path):
			os.system("Facebook.bat")
		break
def fun6():
	les9="Open Email"
	phrase7=speech.input()
	for phrase7 in les9:
		speech.say("I will open your email")
		print"Opening Email ..."
		f_path = abspath("Email.bat")
		if exists(f_path):
			os.system("Email.bat")
		else:
			None
		break
		
fun()
commands()
fun1()
fun2()
fun3()
fun4()
fun5()
fun6()
