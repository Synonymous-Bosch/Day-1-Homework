#! Python3

# Setting variables

name = 'Steven'
age = 39
favourite_cheese = 'cheddar'

# Defining a function to ask the user their name, age, and favourite cheese.

def someone_loves():
     print("Hi! What's your name?")
     name = input()
     print('Cool! How old are you?')
     age = input()
     print("That's genuinely fantastic. Now the rub. What is your favourite cheese?")
     cheese = input()
     # Use of operators to concatenate inputs into sassy response
     they_love = "Let me see if I've got this straight. " + name + ', who is ' + str(age) + ' years old, loves ' + favourite_cheese + '? What a poser.'
     print(they_love)

someone_loves()