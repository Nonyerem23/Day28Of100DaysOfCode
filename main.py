import os, time, random

def rollDice(side):
     result = random.randint(1,side)
     return result
def health():
   health = (random.randint(1, 6) * random.randint(1, 12) / 2) + 10
   return health
def strength():
   strength = (random.randint(1, 6) * random.randint(1, 12) / 2) + 12
   return strength

print("BATTLE TIME")

name1 = input("Name your legend: ")
type1 = input("Character Type (Human, Elf, Wizard, Orc): ")
print()
print(name1)
print(type1)
health2 = health()
strenght2 = strength()
print("HEALTH: ", health2)
print("STRENGTH: ", strenght2)
print()
print("Who are they battling?")
print()

name2 = input("Name your legend: ")
type2 = input("Character Type (Human, Elf, Wizard, Orc): ")
print()
print(name2)
print(type2)
health3 = health()
strenght3 = strength()
print("HEALTH: ", health3)
print("STRENGTH: ", strenght3)
print()


round = 1
winner = None
while True:
    time.sleep(1)
    os.system("clear")
    print("BATTLE TIME")
    print()
    print("The battle begins!")

    c1Dice = rollDice(6)
    c2Dice = rollDice(6)

    difference = abs(strenght2 - strenght3)

    if c1Dice > c2Dice:
      health3 -= difference
      if round==1:
        print(name1, "wins the first blow")
      else:
        print(name1, "wins round", round)

    elif c2Dice > c1Dice:
      health2 -= difference
      if round==1:
        print(name2, "wins the first blow")
      else:
        print(name2, "wins round", round)

    else:
      print("There sword clash and they draw round", round)

      print()
      print(name1)
      print("HEALTH: ", health2)
      print()
      print(name2)
      print("HEALTH: ", health3)
      print()


      if health2 <= 0:
        print(name1, "has died")
        winner = name2
        break
      elif health3 <= 0:
        print(name2, "has died")
        winner = name1
        break
      else:
        print("And they're both standing for the next round") 
        round += 1


    time.sleep(1)
    os.system("clear")
    print("Battle time")
    print()
    print(winner, "has won in", round, "rounds")
