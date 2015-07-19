import random

user = raw_input("Choose your weapon: ")
comp = random.choice( ['rock','paper','scissors'] )

print 'the user (you) chose', user
print 'the comp (I) chose', comp

if user == 'rock':
    print 'Ha! I really chose paper -- I WIN!'
elif user == 'paper':
    print 'Ha! I really chose scissors -- I WIN!'
else:
    print 'Ha! I really choose rock -- I WIN!'