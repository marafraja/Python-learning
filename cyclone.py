
height = int(input("Whats your height:  "))
credits = int(input("How many credits do you have:  "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")

elif height < 137 and credits >= 10:
  print("You are not enough tall to ride")

elif height >=137 and credits < 10:
  print("You dont have enough credits")

else:
  print("You have not met their requirements")