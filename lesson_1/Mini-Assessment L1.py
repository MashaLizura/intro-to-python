# This program is a trivia game online
import time


print("Hello and Welcome to my wonderful trivia game.")
time.sleep(2)

print("Let's introduce each other first. My name is Ms. Trivia Robot!")
time.sleep(2)

print("What is your name?")
time.sleep(1)

name = input("Please type your name here: ")
for i in range(2):
    print("Processing...")
    time.sleep(1)

print(f"Welcome, {name}. It is a pleasure to meet you!")
time.sleep(2)
                                          
print(f"Let me tell you what we can do today, {name}.")
time.sleep(1)
print("We are going to make a deal.")
time.sleep(1)
print("I am going to ask you 3 questions and I'm going to buy you as many beers as many of them you will answer correctly.")
time.sleep(1)
print("Otherwise, I'll tel you a joke! I hope you are ready!")

wins = 0

loss = 0

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 1! " + "-" * 30)
print("-" * 70)

#### Let's get started with some trick questions

time.sleep(1)
print("What goes up as soon as the rain comes down?")
answer1 = input("Please type your answer here: ")

if answer1.lower() == 'umbrella':
    print("haha, that's correct. I guess you deserved your first bottle of beer!")
else:
    print("No silly")
    print("The answer is \"Umbrella\" :)")

if answer1.lower() == 'umbrella':
    wins += 1
else:
    loss += 1
    
print("Cool, let's keep going!")

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 2! " + "-" * 30)
print("-" * 70)


time.sleep(1)
print("What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats?")
answer2 = input("Please type your answer here: ")

if answer2.lower() == 'river':
    print("Wow, that's correct as well. Here is your beer!")
else:
    print("Oh-oh, no it's not right")
    print("The answer is \"River\"")

if answer2.lower() == 'river':
    wins += 1
else:
    loss += 1
    
print("Cool, let's keep going to our last question!")

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 3! " + "-" * 30)
print("-" * 70)


time.sleep(1)
print("I’m so fragile that if you say my name, you’ll break me. What am I?")

answer3 = input("Please type your answer here: ")

if answer3.lower() == 'silence':
    print("Well done! This is your beer")
else:
    print("No, unfortunately, it's not correct.")
    print("Silence! :)")
    
if answer3.lower() == 'silence':
    wins += 1
else:
    loss += 1
    
time.sleep(2)
print("Okay, let's tally thing up!")
time.sleep(2)
print("-" * 70)

if wins > 0:
    print("You answered correctly {} times, and you won {} bottles of beer.".format(wins,wins))
else:
    print("Oh-oh, now you have to listen to my joke.\n A grasshopper sits down at a bar. The bartender says, \"We have a drink named after you!\" The grasshopper replies, \"Who names a drink 'Steve?'\"")
    
    time.sleep(2)
    print(f"This was a lot of fun {name}, I hope you come visit me again soon. Take care!")



