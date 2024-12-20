#!/usr/bin/env python3

# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:
# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin


Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

answer1 = int(input("Q1) Do you like Dawn or Dusk?\n     1) Dawn\n     2) Dusk\nEnter your answer (1-2): "))

if answer1 == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif answer1 == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong input.")

print("\n")

answer2 = int(input("Q2) When I'm dead, I want people to remember me as:\n    1) The Good\n    2) The Great\n    3) The Wise\n    4) The Bold\nEnter your answer (1-4): "))

if answer2 == 1:
  Hufflepuff = Hufflepuff + 2
elif answer2 == 2:
  Slytherin = Slytherin + 2
elif answer2 == 3:
  Ravenclaw = Ravenclaw + 2
elif answer2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print("Wrong input.")

print("\n")

answer3 = int(input("Q3) Which kind of instrument most pleases your ear?\n    1) The violin\n    2) The trumpet\n    3) The piano\n    4) The drum\nEnter your answer (1-4) : "))

if answer3 == 1:
  Slytherin = Slytherin + 4
elif answer3 == 2:
  Hufflepuff = Hufflepuff + 4
elif answer3 == 3:
  Ravenclaw = Ravenclaw + 4
elif answer3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print("Wrong input.")

print("\n")

print("Gryffindor's score: ", Gryffindor)
print("Slytherin's score: ", Slytherin)
print("Ravenclaw's score: ", Ravenclaw)
print("Hufflepuff's score: ", Hufflepuff)
