# Created by Mathijs van Driel 
# Created on 27.6.2021 
# Version 1 
# Sequence 1
#Purpose: the purpose of this component is to ask the user what difficulty would suit them best, and the function allow repeatability when the user types an incorrect input

import time 

# This list stores all the questions in the easy level
list = [ "What colour is red in Te Reo Maori?", "What colour is yellow in Te Reo Maaori?","What colour is green in Te Reo Maaori?", "What colour is orange in Te Reo Maaori?", "What colour is black in Te reo Maaori?"]

#function
def played_before (question): 
  valid=False 
  while not valid: 
    response = input (question) .lower() 

    if response =="yes" or response == "y": 
      response = "yes" 
      return response 
       
    elif response =="no" or response == "n": 
      response = "no" 
      return response  

    else:
      print("please type yes or no"  + "\n") 
    
      
 


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
      print("Please select a difficulty"  + "\n")
      print("1 is easy") 
      time.sleep(.5) 
      print("2 is intermediate") 
      time.sleep(.5) 
      print("3 is advanced")  

# Sequence 2 
#main routine
# Purpose: This sequence asks the user for a name and stores it as a variable
print("Hi there!") 
time.sleep(1) 
print("What is your fantastic name?") 
name = input () 
print("Kia Ora " + name)  
time.sleep(.5) 
print("Today we are going to learn Te Reo Maaori!") 
time.sleep(1.5)

played_program = played_before ("Have you played this quiz before " + name + '\n') 
if played_program == "yes": 
  print("You can move on!") 

elif played_program == "no":  
  print("the Te Reo Maaori quiz is a is a quick test to help children and students imporve thier knowlege of the native language of New Zealand. With three difficulties to choose from this quiz offers a variety of possibities to best fit you.") 
else:
  print("please type yes or no"  + "\n") 
# Sequence 3 
# Purpose: This sequence asks the user a series of questions at an easy level 
user_difficulty = level("What difficulty would fit you best, 1, 2 or 3" + "\n") 

if played_before == "1": 
 print("Ok! Today we will be learning the basics of the language!") 
 time.sleep(1.5) 
 print("To start off, we will learn colours.") 
 time.sleep(1.5) 
 
 print(list[0]) 
 red = input() 

 #if user types whero then program continues to next question
 if red.lower() == 'whero': 
   print("thats correct " + name)
   print("Lets see what other colours you know!") 

#else: inform the user of the correct answer and continue to the next question
 else:  
   print("hmm.. you didnt seem to get that one quite right, the correct answer is 'whero'") 
 #if user types kowhai then program continues to next question   
 print(list[1]) 
 yellow = input()
 if yellow.lower() == 'kowhai': 
    print("Wow! You know your stuff!") 
    print("Lets keep going")
 else: 
#else: inform the user of the correct answer and continue to the next question
    print("The correct answer is Kowhai ") 
#if user types kakariki then program continues to next question
 print(list[2])   
 green = input() 
 if green.lower() == 'kakariki': 
    print("Correct") 
  #else: inform the user of the correct answer and continue to the next question
 else: 
   print("The correct answer is kakariki")
#if user types karaka then program continues to next question 
 print(list[3])   
 orange = input() 
 if orange.lower() == 'karaka': 
    print("Correct") 
 else: 
#else: inform the user of the correct answer and continue to the next question
    print("The colour orange in te reo Maori is know as karaka")  
#if user types pango then program continues to next question
 print(list[4])   
 black = input() 
 if black.lower() == 'pango': 
    print("Correct") 
 else: 
#else: inform the user of the correct answer and continue to the next question
    print("The colour black in te reo Maori is know as pango")   
    
    
    print("Thanks for playing!") 
# Sequence 3: 
# This sequence asks questions at the intermediate difficulty 
# Multiple choice selection
elif played_before == "2": 
  print("You have selected the intermediate difficulty for this subject!")  
  
  print("Which word has the meaning of 'Children'") 
#if user types d or D then program continues to next question
  Children = input("\nA. Tama \nB. Poro \nC. Poroiki\nD. Tamariki\n").lower()
  if Children =="d": 
    print("Correct, well done " + name) 
  else: 
#else: inform the user of the correct answer and continue to the next question
    print("Incorrect, the correct answer was D. Tamariki?")

  print("What is the maaori word for 'car'") 
  #if user types a or A then program continues to next question
  car = input("\nA. Motuka \nB. Ruaturu \nC. Kahina \nD. Onorere\n").lower()
  if car =="a": 
    print("Correct, well done " + name) 
  else: 
#else: inform the user of the correct answer and continue to the next question
    print("Incorrect, the correct answer was A. Motuka")

  print("What is the maaori word for 'New Zealand?'") 
  #if user types b or B then program continues to next question
  Aotearoa = input("\nA. Motu \nB. Aotearoa \nC. Nenuna \nD. Anaterura\n").lower()
  if Aotearoa =="b":
    print("Correct, well done " + name) 
  else: 
#else: inform the user of the correct answer and continue to the next question
    print("Incorrect, the correct answer was B. Aotearoa") 

  print("What is the maaori word for 'Man?'") 
#if user types c or C then program continues to next question
  man = input("\nA. Waahine \nB. Werata \nC. Tapu \nD. Tangata\n").lower()
  if man =="c": 
    print("Correct, well done " + name) 
  else: 
#else: inform the user of the correct answer and continue to the next question
    print("Incorrect, the correct answer was C. Tapu ") 

  print("What is the maaori word for 'Time?'") 
  #if user types a or A then program continues to next question
  Wa = input("\nA. Wā \nB. Mā \nC. Tā \nD. Ngā\n").lower()
  if Wa.lower =="a": 
    print("Correct, well done " + name) 
  else: 
#else: inform the user of the correct answer and continue to the next question
    print("Incorrect, the correct answer was A. Wā ") 
#thank user for playing
    print("Thanks for playing")
# Sequence 4: this sequence asks the user questions at an advanced difficulty 
# Multiple choice selection
elif played_before == "3": 
  print("You have selected the Advanced difficulty for this subject!") 
  print("What is the second line of our national anthem?") 

  Anthem = input("\nA. Manaakitia mai \nB. O ngā iwi mātou rā\nC. Kia tau tō atawhai\nD. E Ihowā Atua" + "\n")
  #if user types b or O nga iwi matou ra then program continues to next question 
  if Anthem.lower() =="b" or 'O nga iwi matou ra' : 
    print("Correct, well done " + name)
  else: 
#else: inform the user of the correct answer and continue to the next question
    print("The correct answer was B. O ngā iwi mātou rā" )  
  
  print("If it's Ua outside it is what?") 
#if user types c or C then program continues to next question
  Ua = input("\nA.Foggy \nB.Sunny\nC.Rainy\nD.Thunderstorm" + "\n")
  if Ua.lower =='c' or "Rainy": 
    print("Correct, well done " + name) 

  else: 
#else: inform the user of the correct answer and continue to the next question
    print("The correct answer was C. Rainy" )  
  
  print("If you were going for a hīkoi you are...") 
#if user types b or B then program continues to next question

  hikoi = input("\nA.Going to the toilet \nB.Going for a walk\nC.Going for a swim\nD.Going for a shop" + "\n")
  if hikoi.lower =='b': 
    print("Correct, well done " + name)
  else: 
#else: inform the user of the correct answer and continue to the next question
    print("The correct answer was B. Going for a walk")  
  
  print("If someone asked you to open the door in Te Reo - what would they say?") 
#if user types d or D then program continues to next question

  door = input("\nA.Horoia ō ringaringa \nB.Kuhu mai ki roto\nC.Haere atu\nD.Huakina te kūaha" + "\n")
  if door.lower =='d':  
    print("Correct, well done " + name) 
  else:  
#else: inform the user of the correct answer and continue to the next question
    print("Incorrect; the correct answer was D. Huakina te kūaha") 
    #thank user for playing the quiz 
    print("Thanks for playing")

