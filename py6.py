import random
import sys
counter=0
print("Welcome to hangman")
print ("________      ")
print ("|             ")
print ("|             ")
print ("|             ")
print ("|             ")
print ("|             ")
print ("====")
word = (random.choice(open('wordbank.txt').read().split()).strip())

guess = list('_'*len(word))

while list(word) != guess:
  print(' '.join(guess))  
  letters = input("guess one letter please!").upper()
  if letters not in word:
    if counter == 0:
      print ("________      ")
      print ("|      |      ")
      print ("|             ")
      print ("|             ")
      print ("|             ")
      print ("|             ")
      print ("====")
    if counter == 1:
      print ("________      ")
      print ("|      |      ")
      print ("|      0       ")
      print ("|             ")
      print ("|             ")
      print ("|             ")
      print ("====")
      print ("Incorrect")
    if counter == 2:
      print ("________      ")
      print ("|      |      ")
      print ("|      0      ")
      print ("|     /|      ")
      print ("|             ")
      print ("|             ")
      print ("====")
    if counter == 3:
      print ("________      ")
      print ("|      |      ")
      print ("|      0       ")
      print ("|     /|\       ")
      print ("|             ")
      print ("|             ")
      print ("====")
    if counter == 4:
      print ("________      ")
      print ("|      |      ")
      print ("|      0       ")
      print ("|     /|\        ")
      print ("|     /       ")
      print ("|             ")
      print ("====")

    if counter == 5:
      print ("________      ")
      print ("|      |      ")
      print ("|      0       ")
      print ("|     /|\       ")
      print ("|     / \       ")
      print ("|             ")
      print ("====")
      print("Game Over!!!")
      sys.exit()
    counter += 1
  else:
    i = 0
    while i < len(word):
        if list(word)[i] == letters:
          guess[i] = letters
        i += 1
print('You\'re right! it\'s ' + word + '.')
sys.exit()
