
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("------------------------------------------------------------------------------")
choose_direction = input('''You\'re at a crossroad. Where do you want to go? Type "left or "right": ''')
direction = choose_direction.lower()

if direction == "right":
  print("You fell into a hole. Game Over")
elif choose_direction == "left":
  print("------------------------------------------------------------------------------")
  choose_path = input('''You\'ve come to a lake. There is an island in the middle of the lake. 
Type "wait" to wait for a boat or Type "swim" to swim across: ''')
  path = choose_path.lower() 
  if path == "swim":
    print("You're attacked by trout. Game Over")
  elif path == "wait":
    print("------------------------------------------------------------------------------")
    choose_door = input('''You arrive at the island unharmed. There is a house with 3 doors. \nOne red, one yellow and one blue. Which colour do you choose? ''')
    door = choose_door.lower()
    if door == "red":
      print("The room is full of fire. Game Over!")
    elif door == "yellow":
      print("You win!")
    elif door == "blue":
      print("You're eaten by beasts. Game Over!")
    else:
      print("You're attacked by zombies. Game Over!")
  else:
    print("You're attacked by monsters. Game Over!")     
else:
  print("You're attacked by dragons. Game Over!")

