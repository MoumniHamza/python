willing_tocontinue = input(" Would you like to start the game type 'y' if you would like to or 'n' if you want to exit: ")

if willing_tocontinue == "y":
   print ("great let's get started")
else:
    exit(print("well thank you for stopping by see you next time"))

user_name = input(" Ok now it's time to get to know you , please enter your name:  ")

while user_name.isdigit() == True:
  
   print("Sorry we only accept valid names")
   user_name = input(" Ok now it's time to get to know you , please enter your name:  ")

print("welcome" , user_name, "its nice to have you here")

user_age = input ("how old are you "+user_name+ ": ") 
user_gender = input(" Are you a boy or a girl "+ user_name+" ?"+"(answer with boy or girl)" ": ")

while (user_gender != "girl") and (user_gender != "boy") == True:
  
   print("Sorry we only accept boy or girl")
   user_gender = input(" Are you a boy or a girl "+ user_name+" ?"+"(answer with boy or girl)" ": ")

print("Hum you are a", user_gender, "let me think about some options for you")

if int(user_age) <= 12 and user_gender == "boy":


   user_continue = input( user_age+" years old that's a great age "+user_name+ " ready for some fun ?(type 'y' or 'n'): ")
   if user_continue == "y":
      print("great let's get started")
   else:
      print("well thank you for stopping by see you next time")

   print("Allright " +user_name+" since you are " +user_age+" years old, those are the things we suggest you to do")
   things_todo = ["going to the movies" ,  "going to the restaurant"] 
   print(things_todo) 
   user_choice = input(" The choice is tough you can only pick one choice, are you ready "+user_name+" ? if not just press something else to exit"+ " you can either write one of the options or exit:  ")

   if  user_choice.lower() == "going to the movies":
      print("Ok you choose to go to the movies ", user_name, " let's go to the movies then")
      print("here we go ",user_name, " we arived to the movies")
   elif  user_choice.lower() == "going to the restaurant":
      print("Ok you choose to go to the restaurant ", user_name, " let's go to the restaurant then")
   else:
      print("It was nice meeting you ", user_name, "see you next time")

elif int(user_age) <= 12 and user_gender == "girl":


   user_continue = input( user_age+" years old that's a great age "+user_name+ " ready for some fun ?(type 'y' or 'n'): ")
   if user_continue == "y":
      print("great let's get started")
   else:
      print("well thank you for stopping by see you next time")

   print("Allright " +user_name+" since you are " +user_age+" years old, those are the things we suggest you to do")
   things_todo = ["going to the zoo" ,  "going to the library"] 
   print(things_todo) 
   user_choice = input(" The choice is tough you can only pick one choice, are you ready "+user_name+" ? if not just press something else to exit"+ " you can either write one of the options or exit:  ")

   if  user_choice.lower() == "going to the zoo":
      print("Ok you choose going to the zoo ", user_name, " let's go to the zoo then")
      print("here we go ",user_name, " we arived to zoo")
   elif  user_choice.lower() == "going to the library":
      print("Ok you choose to go to the library ", user_name, " let's go to the library then")
   else:
      print("It was nice meeting you ", user_name, "see you next time")