#This is an Input/Output AI Chatbot based on Manual Rules

import os
import csv
import time
import win32com.client as wincl
speaker = wincl.Dispatch("SAPI.SpVoice")
os.system('color 2f') # sets the background to blue
import speech_recognition as sr
import subprocess as sp

#make Python speaker
#we've choosed to use keyboard to input replies, beacause speechrecognition requires a good internet connection

#launch face emotion recognition module
extProc = sp.Popen(['python','real_time_video.py']) # runs myPyScript.py 

disc=[0,0,0,0]#c,d,i,s

def calculate_DISC(var):
	global disc
	var=var.upper()
	char = "A"# by default A
	if var.count("A",0,len(var)):
		char = "A"
		disc[0]+=1
	if var.count("B",0,len(var)):
		char = "B"
		disc[1]+=1
	if var.count("C",0,len(var)):
		char = "C"
		disc[2]+=1
	if var.count("D",0,len(var)):
		char = "D"
		disc[3]+=1

def listen():
	var=""
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		var = r.recognize_google(audio)
		print("\n",var)
	except sr.UnknownValueError:
		print('good!')
		speaker.Speak('good!')
	except sr.RequestError as e:
		print('good!')
		speaker.Speak('good!')
	return var


def optimizeMetrics():
	global disc
	sum = 0
	for i in range(4):
	 sum+=disc[i]
	if(sum<200):
		minpos=0
		minval=200
		for i in range(4):
			if(disc[i]<minval):
				minval=disc[i]
				minpos=i
		disc[minpos]+=(200-sum)
	elif (sum>200):
		maxpos=0
		maxval=0
		for i in range(4):
			if(disc[i]>maxval):
				maxval=disc[i]
				maxpos=i
		disc[maxpos]+=(200-sum)

#start the conversation
time.sleep(15)

print('Hello! I am kathréftis') #greeting
speaker.Speak('Hello! I am kathréftis')

#keep going the conversation
print('Whats your name?') #ask
speaker.Speak('Whats your name?')
Name = input() #save answer

print('Im glad to meet you, ' + Name + '!!') #reply
speaker.Speak('Im glad to meet you, ' + Name + '!!')

#keep going the conversation
#print('How old are you?') #ask
#speaker.Speak('How old are you?')
#age = input()
#speaker.speak("Good!");

print("I'm going to ask you a list of questions, just choose the reply by letter ")
speaker.Speak("I'm going to ask you a list of questions, just choose the reply by letter ")
	
#Question 1

print('In your work enviroment, the most important to you...') #ask
speaker.Speak('In your work enviroment, it is most important to you...')

print("A) To get things done and to see results.")
speaker.Speak('A. To get things done and to see results."')#C

print("B) To know exactly what is expected of you and to finish one task before moving to another.")
speaker.Speak('B. To know exactly what is expected of you and to finish one task before moving to another.')#D

print("C) To feel that your co-workers admire you and to be free from rigid rules.")
speaker.Speak('C. To feel that your co-workers admire you and to be free from rigid rules.')#I

print("D) To help co-workers and to be in a peaceful environment.")
speaker.Speak('D. To help co-workers and to be in a peaceful environment.')#S

var = input()#listen()
calculate_DISC(var)

print('In your work enviroment, the least important to you...') #ask
speaker.Speak('In your work enviroment, the least important to you...')

print("A) To feel that your co-workers admire you and to be free from rigid rules.")
speaker.Speak('A. To feel that your co-workers admire you and to be free from rigid rules.')#C

print("B) To help co-workers and to be in a peaceful environment.")
speaker.Speak('B. To help co-workers and to be in a peaceful environment.')#D

print("C) To get things done and to see results.")
speaker.Speak('C. To get things done and to see results."')#I

print("D) To know exactly what is expected of you and to finish one task before moving to another.")
speaker.Speak('D. To know exactly what is expected of you and to finish one task before moving to another.')#S

var = input()#listen()
calculate_DISC(var)


#Question2
print('When someone offers an opinion or conclusion and you disagree, you are most likely to...') #ask
speaker.Speak('When someone offers an opinion or conclusion and you disagree, you are most likely to...')

print("A) Ask for more information.") #C
speaker.Speak("A. Ask for more information.")
print("B) Tell them that you disagree.") #D
speaker.Speak("B. Tell them that you disagree.")
print("C) Say something humorous.") #I
speaker.Speak("C. Say something humorous.")
print("D) Nod and say nothing.") #S
speaker.Speak("D. Nod and say nothing.")

Reply = input() #listen()
calculate_DISC(Reply)

print('When someone offers an opinion or conclusion and you disagree, you are least likely to...') #ask
speaker.Speak('When someone offers an opinion or conclusion and you disagree, you are least likely to...')

print("A) Say something humorous.") #I
speaker.Speak("A. Say something humorous.")
print("B) Nod and say nothing.") #S
speaker.Speak("B. Nod and say nothing.")
print("C) Ask for more information.") #C
speaker.Speak("C. Ask for more information.")
print("D) Tell them that you disagree.") #D
speaker.Speak("D. Tell them that you disagree.")

Reply = input() #listen()
calculate_DISC(Reply)
#Question3
print("When you are working on a team and we encounter a difficulty of some kind, you are most likely to say...")
speaker.speak("When  you are working on a team and we encounter a difficulty of some kind,  you are most likely to say...")

print("A) Let's make a decision!")
speaker.speak("A. Let's make a decision!")#C
print("B) Let's consider this more carefully? Do we have all of the data we need?")
speaker.speak("B. Let's consider this more carefully? Do we have all of the data we need?")#D
print("C) How do you feel? You'd like to make sure that everyone is comfortable.")
speaker.speak("C. How do you feel? You'd like to make sure that everyone is comfortable.")#I
print("D) Lighten up! Just go with the flow!")
speaker.speak("D. Lighten up! Just go with the flow!")#S

Reply = input() #listen()
calculate_DISC(Reply)

print("When you are working on a team and we encounter a difficulty of some kind, you are least likely to say...")
speaker.speak("When  you are working on a team and we encounter a difficulty of some kind,  you are least likely to say...")

print("A) How do you feel? you'd like to make sure that everyone is comfortable.")
speaker.speak("A. How do you feel? you'd like to make sure that everyone is comfortable.")
print("B) Lighten up! Just go with the flow!")
speaker.speak("B. Lighten up! Just go with the flow!")
print("C) Let's make a decision!")
speaker.speak("C. Let's make a decision!")
print("D) Let's consider this more carefully? Do we have all of the data we need?")
speaker.speak("D. Let's consider this more carefully? Do we have all of the data we need?")

Reply = input() #listen()
calculate_DISC(Reply)

#Question4
print("Your attitude towards detail work, like research and data analysis, is most often...")
speaker.speak("Your attitude towards detail work, like research and data analysis, is most often...")

print("A) Great. I enjoy research and analysis.")#C
speaker.speak("A. Great. I enjoy research and analysis.")
print("B) If it will get better and faster results, you'll do it.")#D
speaker.speak("B. If it will get better and faster results, you'll do it.")
print("C) If it will make others think more highly of you, you'll do it.")#I
speaker.speak("C. If it will make others think more highly of you, you'll do it.")
print("D) If it will help other people or make things easier, you'll do it.")#S
speaker.speak("D. If it will help other people or make things easier, you'll do it.")

Reply = input() #listen()
calculate_DISC(Reply)

print("Your attitude towards detail work, like research and data analysis, is least often...")
speaker.speak("Your attitude towards detail work, like research and data analysis, is least often...")

print("A) If it will make others think more highly of you, you'll do it.")#I
speaker.speak("A. If it will make others think more highly of you, you'll do it.")
print("B) If it will help other people or make things easier, you'll do it.")#S
speaker.speak("B. If it will help other people or make things easier, you'll do it.")
print("C) Great. I enjoy research and analysis.")#C
speaker.speak("C. Great. I enjoy research and analysis.")
print("D) If it will get better and faster results, you'll do it.")#D
speaker.speak("D. If it will get better and faster results, you'll do it.")


Reply = input() #listen()
calculate_DISC(Reply)

#Question5
print("When you are at an event with many people you have not yet met present, you are most likely to...")
speaker.speak("When you are at an event with many people you have not yet met present, you are most likely to...")

print("A) Seek a good vantage point to observe the event and sit quietly unless someone speaks to you.")#C
speaker.speak("A. Seek a good vantage point to observe the event and sit quietly unless someone speaks to you.")
print("B) Go to the people you need to speak with to fulfill your purpose for attending.")#D
speaker.speak("B. Go to the people you need to speak with to fulfill your purpose for attending.")
print("C) Meet and talk with as many people as possible before the event is over.")#I
speaker.speak("C. Meet and talk with as many people as possible before the event is over.")
print("D) Find a small group of people with whom you are already comfortable and speak with them in quiet conversation.")#S
speaker.speak("D. Find a small group of people with whom you are already comfortable and speak with them in quiet conversation.")

Reply = input() #listen()
calculate_DISC(Reply)

print("When you are at an event with many people you have not yet met present, you are least likely to...")
speaker.speak("When you are at an event with many people you have not yet met present, you are least likely to...")

print("A) Meet and talk with as many people as possible before the event is over.")#I
speaker.speak("A. Meet and talk with as many people as possible before the event is over.")
print("B) Find a small group of people with whom you are already comfortable and speak with them in quiet conversation.")#S
speaker.speak("B. Find a small group of people with whom you are already comfortable and speak with them in quiet conversation.")
print("C) Seek a good vantage point to observe the event and sit quietly unless someone speaks to you.")#C
speaker.speak("C. Seek a good vantage point to observe the event and sit quietly unless someone speaks to you.")
print("D) Go to the people you need to speak with to fulfill your purpose for attending.")#D
speaker.speak("D. Go to the people you need to speak with to fulfill your purpose for attending.")


Reply = input() #listen()
calculate_DISC(Reply)

#Question6

print("The way you see yourself most is...")
speaker.speak("The way you see yourself most is...")

print("A) Logical, factual, and correct.")#C
speaker.speak("A. Logical, factual, and correct.")
print("B) Doing, driving, and accomplishing")#D
speaker.speak("B. Doing, driving, and accomplishing")
print("C) Friendly, fun, and persuasive.")#I
speaker.speak("C. Friendly, fun, and persuasive.")
print("D) Patient, kind, and helpful.")#S
speaker.speak("D. Patient, kind, and helpful.")

Reply = input() #listen()
calculate_DISC(var)

print("The way you see yourself least is...")
speaker.speak("The way you see yourself least is...")

print("A) Friendly, fun, and persuasive.")#I
speaker.speak("A. Friendly, fun, and persuasive.")
print("B) Patient, kind, and helpful.")#S
speaker.speak("B. Patient, kind, and helpful.")
print("C) Logical, factual, and correct.")#C
speaker.speak("C. Logical, factual, and correct.")
print("D) Doing, driving, and accomplishing")#D
speaker.speak("D. Doing, driving, and accomplishing")


Reply = input() #listen()
calculate_DISC(Reply)

#Question7

print("When you hear about a coming change, you are most likely to think...")
speaker.speak("When you hear about a coming change, you are most likely to think...")

print("A) Is there a good reason behind it?")#C
speaker.speak("A. Is there a good reason behind it?")
print("B) What will it do to results and speed?")#D
speaker.speak("B. What will it do to results and speed?")
print("C) How does it affect you?")#I
speaker.speak("C. How does it affect you?")
print("D) How does it affect everyone involved?")#S
speaker.speak("D. How does it affect everyone involved?")

Reply = input() #listen()
calculate_DISC(var)

print("When you hear about a coming change, you are least likely to think...")
speaker.speak("When you hear about a coming change, you are least likely to think...")

print("A) How does it affect you?")#I
speaker.speak("A. How does it affect you?")
print("B) How does it affect everyone involved?")#S
speaker.speak("B. How does it affect everyone involved?")
print("C) Is there a good reason behind it?")#C
speaker.speak("C. Is there a good reason behind it?")
print("D) What will it do to results and speed?")#D
speaker.speak("D. What will it do to results and speed?")


Reply = input() #listen()
calculate_DISC(Reply)

#Question8

print("The most accurate way to describe your approach to work is...")
speaker.speak("The most accurate way to describe your approach to work is...")

print("A) Plan your work and work your plan.")#C
speaker.speak("A. Plan your work and work your plan.")
print("B) Get it done. What's next?")#D
speaker.speak("B. Get it done. What's next?")
print("C) Who will do this with me? Is there anyone to talk with while I work?")#I
speaker.speak("C. Who will do this with me? Is there anyone to talk with while I work?")
print("D) How would you like for me to do this?")#S
speaker.speak("D. How would you like for me to do this?")

Reply = input() #listen()
calculate_DISC(Reply)

print("The least accurate way to describe your approach to work is...")
speaker.speak("The least accurate way to describe your approach to work is...")

print("A) Who will do this with me? Is there anyone to talk with while I work?")#I
speaker.speak("A. Who will do this with me? Is there anyone to talk with while I work?")
print("B) How would you like for me to do this?")#S
speaker.speak("B. How would you like for me to do this?")
print("C) Plan your work and work your plan.")#C
speaker.speak("C. Plan your work and work your plan.")
print("D) Get it done. What's next?")#D
speaker.speak("D. Get it done. What's next?")


Reply = input() #listen()
calculate_DISC(Reply)

#Question9

print("The type of work activities that you enjoy the most involve...")
speaker.speak("The type of work activities that you enjoy the most involve...")

print("A) Working alone and focusing on the task at hand to create excellence.")#C
speaker.speak("A. Working alone and focusing on the task at hand to create excellence.")
print("B) Fast-paced, rapidly changing tasks that create progress.")#D
speaker.speak("B. Fast-paced, rapidly changing tasks that create progress.")
print("C) Interacting with many people to create new ideas and energy.")#I
speaker.speak("C. Interacting with many people to create new ideas and energy.")
print("D) Comfortable and predictable tasks that support the team.")#S
speaker.speak("D. Comfortable and predictable tasks that support the team.")

Reply = input() #listen()
calculate_DISC(var)


print("The type of work activities that you enjoy the least involve...")
speaker.speak("The type of work activities that you enjoy the least involve...")

print("A) Interacting with many people to create new ideas and energy.")#I
speaker.speak("A. Interacting with many people to create new ideas and energy.")
print("B) Comfortable and predictable tasks that support the team.")#S
speaker.speak("B. Comfortable and predictable tasks that support the team.")
print("C) Working alone and focusing on the task at hand to create excellence.")#C
speaker.speak("C. Working alone and focusing on the task at hand to create excellence.")
print("D) Fast-paced, rapidly changing tasks that create progress.")#D
speaker.speak("D. Fast-paced, rapidly changing tasks that create progress.")


Reply = input() #listen()
calculate_DISC(Reply)

#Question10

print("When you receive a phone call, you are most interested in")
speaker.speak("When you receive a phone call, you are most interested in")

print("A) What they want you to do.")#C
speaker.speak("A. What they want you to do.")
print("B) Why they called you.")#D
speaker.speak("B. Why they called you. ")
print("C) Talking with the person who called.")#I
speaker.speak("C. Talking with the person who called.")
print("D) How you can help.")#S
speaker.speak("D. How you can help.")

Reply = input() #listen()
calculate_DISC(Reply)

print("When you receive a phone call, you am least interested in")
speaker.speak("When you receive a phone call, you are least interested in")

print("A) Talking with the person who called.")#I
speaker.speak("A. Talking with the person who called.")
print("B) How you can help.")#S
speaker.speak("B. How you you help.")
print("C) What they want you to do.")#C
speaker.speak("C. What they want you to do.")
print("D) Why they called you.")#D
speaker.speak("D. Why they called you. ")


Reply = input() #listen()
calculate_DISC(Reply)

#Question 11

print("The thing someone could say that would have the most positive impact on you is")
speaker.speak("The thing someone could say that would have the most positive impact on you is")

print("A) You get a lot done")#C
speaker.speak("A. You get a lot done")
print("B) You do excellent work.")#D
speaker.speak("B. You do excellent work.")
print("C) You are fantastic!")#I
speaker.speak("C. You are fantastic!")
print("D) I really appreciate you.")#S
speaker.speak("D. I really appreciate you.")

Reply = input() #listen()
calculate_DISC(Reply)

print("The thing someone could say that would have the least positive impact on you is")
speaker.speak("The thing someone could say that would have the least positive impact on you is")

print("A) You are fantastic!")#I
speaker.speak("A. You are fantastic!")
print("B) I really appreciate you.")#S
speaker.speak("B. I really appreciate you.")
print("C) You get a lot done")#C
speaker.speak("C. You get a lot done")
print("D) You do excellent work.")#D
speaker.speak("D. You do excellent work.")

Reply = input() #listen()
calculate_DISC(Reply)

#Question 12

print("The projects or tasks that you enjoy the most allow you to")
speaker.speak("The projects or tasks that you enjoy the most allow you to")

print("A) Do what I already know how to do at my own pace.")#C
speaker.speak("A. Do what I already know how to do at my own pace.")
print("B) Achieve big results and overcome a challenge.")#D
speaker.speak("B. Achieve big results and overcome a challenge.")
print("C) Work with many different people on a wide range of tasks to keep things interesting.")#I
speaker.speak("C. Work with many different people on a wide range of tasks to keep things interesting.")
print("D) Collect and evaluate information to build plans or systems.")#S
speaker.speak("D. Collect and evaluate information to build plans or systems.")

Reply = input() #listen()
calculate_DISC(Reply)

print("The projects or tasks that you enjoy the least allow you to")
speaker.speak("The projects or tasks that you enjoy the least allow you to")

print("A) Work with many different people on a wide range of tasks to keep things interesting.")#I
speaker.speak("A. Work with many different people on a wide range of tasks to keep things interesting.")
print("B) Collect and evaluate information to build plans or systems.")#S
speaker.speak("B. Collect and evaluate information to build plans or systems.")
print("C) Do what I already know how to do at my own pace.")#C
speaker.speak("C. Do what I already know how to do at my own pace.")
print("D) Achieve big results and overcome a challenge.")#D
speaker.speak("D. Achieve big results and overcome a challenge.")

Reply = input() #listen()
calculate_DISC(Reply)

disc[1] = round((disc[1]/12)*100)# Dominance
disc[2] = round((disc[2]/12)*100)# influence
disc[3] = round((disc[3]/12)*100)# steadiness
disc[0] = round((disc[0]/12)*100)# Conscientiousness

optimizeMetrics()

csvData = [[str(Name),''],['D', str(disc[1])], ['C', str(disc[0])], ['I', str(disc[2])], ['S', str(disc[3])]]

csv.register_dialect('disc', delimiter = ',', lineterminator = '\n')

with open('disc.csv', 'w') as f:
	writer = csv.writer(f, dialect='disc')
	writer.writerows(csvData)

f.close()

print("Thank you for you time !, and have a nice day !")
speaker.speak("Thank you for you time !, and have a nice day !")

sp.Popen.terminate(extProc) # closes the emotion detection process

os.system('python outPutCreator.py')
