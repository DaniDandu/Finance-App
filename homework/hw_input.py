#This exercises are for the input function
#you can play a little with the function here https://www.w3schools.com/python/ref_func_input.asp

#ex1
def sum():
    print("x = ")
    x = int(input())
    print("y = ")
    y = int(input())
    print("Suma este: ", x + y)
# take 2 numbers from the user
# print the sum back
print("ex1")
# sum()


#ex2
def the_biggest():
    print("x = ")
    x = int(input())
    print("y = ")
    y = int(input())
    print("z = ")
    z = int(input())
    max = 0
    if x > max:
        max = x
    if y > max:
        max = y
    if z > max:
        max = z
    print("The biggest number is: ", max)
# take 3 numbers from the user
# print the biggest one
print("ex2")
#the_biggest()


#ex3
def drink():
    print("what is your name?")
    name = input()
    print("how old are you?")
    age = int(input())
    if age > 18:
        print(name, "is allowed to drink")
    else:
        print(name, "isn't allowed to drink")
#ask the user's name
#ask him his age
# print if he is allowed to drink
print("ex3")
#drink()

#ex4
def sentence():
    print("Enter 5 words:")
    word_1 = input()
    word_2 = input()
    word_3 = input()
    word_4 = input()
    word_5 = input()
    text = word_1 + " " + word_2 + " " + word_3 + " " + word_4 + " " + word_5
    print(text)
#ask the user for at least 5 words
#put them in a sentence
print("ex4")
#sentence()

#ex5
import random
x = random.randint(0, 9) #this will pick a random number between 0 and 9
def game(x):
    print("enter a number between 0 and 9")
    y = int(input())
    print("the number was: ", x)
    if x == y:
        print("you guessed the number")
    else:
        print("you didn't guess the number")
#create a guessing game, the user must tell a number between 0 and 9 and you must tell him if he guessed it
print("ex5")
game(x)
