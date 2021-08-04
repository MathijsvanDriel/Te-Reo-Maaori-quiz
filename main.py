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

played_before = level("What difficulty would fit you best, 1,  2 or 3" + "\n") 

 
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
   print("Try to remember that one for next time") 
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
    print("The colour orange in te reo Maori is know as karaka") 
  


elif played_before == "2": 
  print("You have selected the intermediate difficulty for this subject!")  
  print("Which word has the meaning of 'Children'") 

  Children = input("\nA. Tama \nB. Poro \nC. Poroiki\nD.Tamariki" + "\n")

  if Children.lower =='D': 
    print("Correct, well done " + name)

  else: 
    print("Incorrect the correct answer was D. Tamariki")") 



elif played_before == "3": 
  print("You have selected the Advanced difficulty for this subject!") 
  print("What is the second line of our national anthem?") 

  Anthem = input("\nA. Manaakitia mai \nB. O ngā iwi mātou rā\nC. Kia tau tō atawhai\nD. E Ihowā Atua" + "\n")

  if Anthem.lower() =="B" or 'O nga iwi matou ra' : 
    print("Correct, well done " + name)

  else: 
    print("The correct answer was B. O ngā iwi mātou rā" )

  print("If it's Ua it is what?") 

  Ua = input("\nA.Foggy \nB.Sunny\nC.Rainy\nD.Thunderstorm" + "\n")

  if Ua.lower =='C' or "Rainy": 
    print("Correct, well done " + name)

  else: 
    print("The correct answer was C. Rainy" )  

  
  print("If you were going for a hīkoi you are...") 

  hikoi = input("\nA.Going to the toilet \nB.Going for a walk\nC.Going for a swim\nD.Going for a shop" + "\n")

  if hikoi.lower =='B': 
    print("Correct, well done " + name)

  else: 
    print("The correct answer was B. Going for a walk")  

  print("If someone asked you to open the door in Te Reo - what would they say?") 

  door = input("\nA.Horoia ō ringaringa \nB.Kuhu mai ki roto\nC.Haere atu\nD.Huakina te kūaha" + "\n")

  if door.lower =='D': 
    print("Correct, well done " + name)

  else: 
    print("Incorrect; the correct answer was D. Huakina te kūaha")

