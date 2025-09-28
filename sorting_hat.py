# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

quest1 = int(input("Q1) Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n Your answer: "))
if quest1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif quest1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input")


quest2 = int(input("Q2) When I’m dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n Your answer: "))
if quest2 == 1:
  Hufflepuff += 2
elif quest2 == 2:
  Slytherin += 2
elif quest2 == 3:
  Ravenclaw += 2
elif quest2 == 4:
  Gryffindor += 2
else:
  print("Wrong input")

quest3 = int(input("Q2) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n Your answer: "))
if quest3 == 1:
  Slytherin += 4
elif quest3 == 2:
  Hufflepuff += 4
elif quest3 == 3:
  Ravenclaw += 4
elif quest3 == 4:
  Gryffindor += 4
else:
  print("Wrong input")

highest_num = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
win = ""
if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    win = "Gryffindor"
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    win = "Ravenclaw"
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    win = "Hufflepuff"
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    win = "Slytherin"

print("The points for Gryffindor: ", Gryffindor)
print("The points for Ravenclaw: ", Ravenclaw)
print("The points for Hufflepuff: ", Hufflepuff)
print("The points for Slytherin: ", Slytherin)
print("The most points: ", highest_num, win )