# Created by Mathijs van Driel 
# Created on 27.6.2021 
# Version 1 
# Sequence 1
# Purpose:..

import time
def level (question): 
  valid=False 
  while not valid: 
    response = input (question) .lower() 

    if response =="3" or response == "three": 
      response = "3" 
      return response 
       
    elif response =="2" or response == "two": 
      response = "2" 
      return response  
      
    elif response =="1" or response == "one": 
      response = "1" 
      return response 
    else:
      print("Please select the one of the following")
      print("Please select a difficulty"  + "\n")
      print("1") 
      time.sleep(.5) 
      print("2") 
      time.sleep(.5) 
      print("3")  

# Sequence 2 
# Purpose: This sequence asks the user for a name and stores it as a variable
print("Hi there!") 
time.sleep(1) 
print("What is your fantastic name?") 
name = input () 
print("Kia Ora " + name)  
time.sleep(.5) 
print("Today we are going to learn Te Reo Maaori!") 
time.sleep(1.5)

played_before = level("What difficulty would fit you best, 1 being easy 2 being average 3 being difficult" + "\n") 

 
if played_before == "1": 
 print("Ok! Today we will be learning the basics of the language!") 
 time.sleep(1.5) 
 print("To start off, we will learn colours.") 
 time.sleep(1.5) 
 
 print("What colour is red in Te Reo Maori?")  
 red = input()
 if red.lower() == 'whero': 
   print("thats correct " + name)
   print("Lets see what other colours you know!") 
 else: 
   print("hmm.. you didnt seem to get that one quite right, the correct answer is 'whero'") 
   time.sleep(.5) 
   print("Try toremember that one for next time") 
   time.sleep(1.5) 
   
   print("what colour is yellow in Te Reo Maaori?")
   yellow = input()
 if yellow.lower() == 'kowhai': 
   print("Wow! You know your stuff!") 
   print("Lets keep going") 
 else: 
   print("The correct answer is Kowhai ") 
   
   
   print("what colour is green in Te Reo Maaori?")
   green = input() 
 if green.lower() == 'kakariki': 
   print("Correct") 
 else: 
     print("Green is Kakariki in Te Reo Maaori")  

     print("what colour is orange in Te Reo Maaori?")
   orange = input() 
 if orange.lower() == 'karaka': 
   print("Correct") 
 else: 
     print("The colour orange in te reo Maori is know as kowhai") 
  

  








elif played_before == "2": 
  print("You have selected the intermediate difficulty for this subject!") 

  

elif played_before == "3": 
  print("SHEEEEEEEEEESH") 

else: 
  print("Please select the one of the following")
  print("Please select a difficulty")
  print("1") 
  time.sleep(.5) 
  print("2") 
  time.sleep(.5) 
  print("3") 


