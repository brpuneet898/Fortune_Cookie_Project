# This is a simple fortune cookie project, made to showcase the random library functions.

# First of all we have to import the random library.
import random

lucky_no = random.randint(1,100)
fortune_no = random.randint(1,3)
probability = round(random.random(), 2)

fortune_text = ''

if fortune_no == 1:
  fortune_text = "You will have a great day!"
if fortune_no == 2:
  fortune_text = "Today will be tough...but worth it!"
if fortune_no == 3:
  fortune_text = "Never give up, you're a hero!"

print(f'{fortune_text} Your Lucky Number for the day is: {lucky_no}! The probability of your day going good is: {probability}!')
