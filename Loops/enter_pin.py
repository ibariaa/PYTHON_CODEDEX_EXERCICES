#!/usr/bin/env python3

# In programming, a loop is used to repeat a block of code until a specified condition is satisfied. It's another incredibly powerful tool that's used a ton!

# People will often use the generic term “iterate” when referring to loops; iterate simply means “to repeat”.

# The first kind of loop that we are going to learn is the while loop. You can think of the while loop like a traffic circle.

# Each lap is one iteration! A car will iterate over and over again until it can't do so anymore.

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')
