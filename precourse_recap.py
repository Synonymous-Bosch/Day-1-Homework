name = 'Steven'
age = 39
favourite_cheese = 'cheddar'

def someone_loves(name, age, favourite_cheese):
     they_love = name + ', who is ' + str(age) + ' years old, loves ' + favourite_cheese + '!'
     return they_love

print(someone_loves('Steven', 39, 'mature cheddar'))