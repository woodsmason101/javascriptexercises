import random
coin = ['heads','tails']
heads= 0
tails= 0

question=int(input('How many times do you want to flip a coin?\n'))
print ('total coin flips')
print ('================')
for x in range(question):
  computer=random.choice(coin)
  if computer == 'heads':
    heads += 1
  if computer == 'tails':
    tails += 1
print ('tails : ', tails)
print ('heads : ', heads)
