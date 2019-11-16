#!/usr/bin/python3

#Program title
print ("--------------------")
print ("        F-BOX       ")
print ("--------------------")

#Menu title
print ("Menu \n choose a number \n 1.Calculator \n 2.game(guess the number) \n 0.about")
#menu options
num1 = input("number:")

#main body(Program)
if num1 == "1":

#Calculator
#Calculator title
  print ("--------------------")
  print ("     Calculator     ")
  print ("--------------------")
#number and question(Cal)
  first = input("First number:")
  second = input("Second number:")
  i = input("Are you sure?(y/n)")

#Main body(Cal)
  if i == "y":
    print ("Please input a number: \n 1:means a+b \n 2:means a-b \n 3:means a*b \n 4:means a/b")
    num2 = input("number:")
    firstnum = int(first)
    secondnum = int(second)
    if num2 == "1":
      print (firstnum+secondnum)
    elif num2 == "2":
      print (firstnum-secondnum)
    elif num2 == "3":
      print (firstnum*secondnum)
    elif num2 == "4":
      print (firstnum/secondnum)
  else:
    if i == "n":
      print ("abort...")

#END(Cal)

elif num1 == "2":

#guess the number
#title of the game
  print ("----------Welcome----------")

#number(random)
  import random
  randnum = random.randint(0,50)
  numx = input("Please guess a number:")
  num3 = int(numx)
  if randnum == num3:
    print ("wow,you guseeed it!")
  else:
    if num3 < randnum:
      print ("Sorry,the number is smaller than correct answer,try again!")
    else:
      print ("Sorry,The number is larger than correct answer,try again!")
  time = 0
  while randnum != num3 and time < 3:
    numx = input("Please guess a number")
    num3 = int(numx)
    if randnum == num3:
      print ("wow,you guessed it!")
    else:
      time += 1
      if num3 < randnum:
        print ("Sorry,the number is smaller than correct answer,try again!")
      else:
        print ("Sorry,the number is larger than correct answer,try again!")
  print ("GAME OVER!")
#END(game)

elif num1 == "0":
#About F-BOX
  print ("###############")
  print ("  About F-BOX  ")
  print ("###############")
  print ("Developer:@Kalpa")
  print ("Contact: \n Email:ying0448219@gmail.com \n QQ:945040714")
  print ("version:0.1.1(beta)")

