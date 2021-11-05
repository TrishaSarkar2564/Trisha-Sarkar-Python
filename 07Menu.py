def hello_world():
  print("Helloworld")

def goodbye_world():
  print("Hello World")
  input("------> Program paused - press enter to continue")
  print("Goodbye World")

def goodbye_person():
  print('Hello')
  username = input("What is your name ? ")
  print("Goodbye " + username)

def good_teacher():
  TeachName = input("Teacher name (try Mr Horan) " )
  if TeachName == "Mr Horan":
    print ("You are lucky, he is a great teacher.")
  else:
    print (TeachName + " is an ok teacher")

def for_loop():
  for x in range(1, 500):
    print(x)

def while_loop():
  x=0
  while x == 0:
    subject = input("What is the name of this subject ")
    if subject == "IST":
        print(" ")
        print(" ")
        print("Congratulations!!")
        print(" ")
        print(" ")
        print(" ")
        break
    else:
        print("Not Correct - try again")

def menu():
  print(" ------------------------------------------------")
  print("|                                                |")
  print("|    07Menu                                      |")
  print("|    Name : Trisha Sarkar                        |")
  print("|    Version : 01                                |")
  print("|                                                |")
  print(" ------------------------------------------------")
  print(" ")
  print("1. Hello World")
  print("2. Goodbye World")
  print("3. Goodbye Person")
  print("4. Good Teacher")
  print("5. forLoop")
  print("6. whileLoop")
  print("7. string Loop")
  print("8. Convert to ascii")
  print("9. Encode a string")
  print("x. To Exit")

def start_text():
  print("")
  print("----Start of Output ---------------------------")
  print("")

def end_text():
  print("")
  print("----End of Output ---------------------------")
  print("")
  print("")
  print("")
  input("Press Enter to continue")

number = input(Enter an option )
  while number != "x":
    if number == "1":
       start_text()
       hello_world()
       end_text()
    elif number == "2":
      start_text()
      goodbye_world()
      end_text()
    elif number == "3":
      start_text()
      goodbye_person()
      end_text()
    elif number == "4":
      start_text()
      good_teacher()
      end_text()
    elif number == "5":
      start_text()
      for_loop()
      end_text()
    elif number == "6":
      start_text()
      while_loop()
      end_text()
    else :
      start_text()
      print("invalid option")
      end_text()
    elif number == "x"
      start_text()
      end_text()
        break