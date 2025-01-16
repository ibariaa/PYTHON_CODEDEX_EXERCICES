#!/usr/bin/env python3

#Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies. 🐝

#Though this challenge may appear simple to experienced coders, it is designed to weed out 90% of job candidates who cannot apply their coding knowledge to a new problem creatively. Want to give it a try?

#Create a fizz_buzz.py program that outputs numbers from 1 to 100.

#Here's the catch:

#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz" instead of the number.
#Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".


for i in range(1, 100, 1):
  if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)
