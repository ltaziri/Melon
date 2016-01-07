import random

print "Hello there!"

name = raw_input("What is your name?")

print "{}, I am thinking of a number from 1 to 100.".format(name)

secret_num = random.randint(1,100)

guess = int(raw_input("Can you guess it?"))

def no_number(guess):
    try:
        is_int(guess)
        return True
        guessing()
    except ValueError:
        return False
        print "That's not a number, silly!"
        guess = int(raw_input("Try again!"))

print secret_num

def guessing():
    while guess != secret_num:
        if guess > 100:
            print "I SAID the number is from 1 to 100!"
            guess = int(raw_input("Try again!"))
        elif guess < 0:
            print "I SAID the number is from 1 to 100!"
            guess = int(raw_input("Try again!"))
        elif guess < secret_num:
            print "Too Low!"
            guess = int(raw_input("Try again!"))
        elif guess > secret_num:
            print "Too High!"
            guess = int(raw_input("Try again!"))
        else:
            print "That's not a number!"
            guess = int(raw_input("Try again!"))

print "Congratualtions! {} is the correct number!".format(guess)