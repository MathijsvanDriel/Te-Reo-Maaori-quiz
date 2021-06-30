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


print("Hi there!") 
time.sleep(1) 
print("What is your fantastic name?") 
n = input () 
print("Kia Ora " + n)  
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
   print("thats correct " + n)
   print("Lets see what other colours you know!") 
 else: 
   print("hmm.. you didnt seem to get that one quite right, the correct answer is 'whero'") 
   time.sleep(2) 
   print("Now tell me, what colour is red in Te Reo Maaori?")
   if red.lower() == 'whero': 
     print("Good job, try to remember that one for next time") 
     time.sleep(1.5) 
   print("what colour is yellow in Te Reo Maaori?")
  







elif played_before == "2": 
  print("no judgement here") 
  

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


